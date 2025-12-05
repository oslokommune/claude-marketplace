#!/usr/bin/env python3
# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "docker",
# ]
# ///

"""
Docker Manager - Manage test containers

Handles Docker container lifecycle for test execution:
- Build test image
- Create and configure containers
- Volume mounting
- Cleanup
"""

import docker
from pathlib import Path
from typing import Optional, Dict, Any
from dataclasses import dataclass


@dataclass
class ContainerConfig:
    """Configuration for a test container"""
    name: str
    plugins_dir: Path
    transcript_dir: Path
    artifacts_dir: Path
    env_vars: Optional[Dict[str, str]] = None
    env_file: Optional[Path] = None  # Path to .env file to load


class DockerManager:
    """Manage Docker containers for testing"""

    def __init__(self, dockerfile_path: Path):
        """
        Initialize Docker manager

        Args:
            dockerfile_path: Path to the Dockerfile
        """
        self.dockerfile_path = Path(dockerfile_path)
        self.dockerfile_dir = self.dockerfile_path.parent
        self.client = docker.from_env()
        self.image_name = "claude-plugin-test"
        self.image_tag = "latest"

    def build_image(self, force_rebuild: bool = False) -> bool:
        """
        Build the test Docker image

        Args:
            force_rebuild: Force rebuild even if image exists

        Returns:
            True if successful
        """
        try:
            # Check if image exists
            image_full_name = f"{self.image_name}:{self.image_tag}"

            if not force_rebuild:
                try:
                    self.client.images.get(image_full_name)
                    print(f"Image {image_full_name} already exists")
                    return True
                except docker.errors.ImageNotFound:
                    pass

            print(f"Building image {image_full_name}...")

            # Build the image
            image, logs = self.client.images.build(
                path=str(self.dockerfile_dir),
                dockerfile=self.dockerfile_path.name,
                tag=image_full_name,
                rm=True,
                pull=False  # Don't pull base images every time
            )

            # Print build logs
            for log in logs:
                if 'stream' in log:
                    print(log['stream'], end='')

            print(f"Successfully built {image_full_name}")
            return True

        except Exception as e:
            print(f"Error building image: {e}")
            return False

    def create_container(self, config: ContainerConfig) -> Optional[Any]:
        """
        Create a test container with proper configuration

        Args:
            config: Container configuration

        Returns:
            Docker container object, or None if error
        """
        try:
            # Prepare volume mounts
            # Note: settings.json is now baked into the Docker image
            volumes = {
                str(config.plugins_dir.absolute()): {
                    'bind': '/home/node/.claude/plugins/marketplaces/origo',
                    'mode': 'ro'
                },
                str(config.transcript_dir.absolute()): {
                    'bind': '/home/node/.claude/projects',
                    'mode': 'rw'
                },
                str(config.artifacts_dir.absolute()): {
                    'bind': '/artifacts',
                    'mode': 'rw'
                }
            }

            # Prepare environment variables
            environment = config.env_vars or {}

            # Load environment variables from env_file if provided
            if config.env_file and config.env_file.exists():
                with open(config.env_file) as f:
                    for line in f:
                        line = line.strip()
                        # Skip empty lines and comments
                        if not line or line.startswith('#'):
                            continue
                        # Parse KEY=VALUE format
                        if '=' in line:
                            key, value = line.split('=', 1)
                            # Remove quotes if present
                            value = value.strip().strip('"').strip("'")
                            environment[key.strip()] = value

            # Create container
            container = self.client.containers.create(
                image=f"{self.image_name}:{self.image_tag}",
                name=config.name,
                volumes=volumes,
                environment=environment,
                detach=True,
                tty=True,
                stdin_open=True,
                user="node",
                working_dir="/workspace",
                # Keep container running
                command="/bin/bash"
            )

            return container

        except Exception as e:
            print(f"Error creating container: {e}")
            return None

    def start_container(self, container) -> bool:
        """
        Start a container

        Args:
            container: Docker container object

        Returns:
            True if successful
        """
        try:
            container.start()
            return True
        except Exception as e:
            print(f"Error starting container: {e}")
            return False

    def stop_container(self, container, timeout: int = 10) -> bool:
        """
        Stop a container gracefully

        Args:
            container: Docker container object
            timeout: Timeout in seconds

        Returns:
            True if successful
        """
        try:
            container.stop(timeout=timeout)
            return True
        except Exception as e:
            print(f"Error stopping container: {e}")
            return False

    def remove_container(self, container, force: bool = True) -> bool:
        """
        Remove a container

        Args:
            container: Docker container object
            force: Force removal even if running

        Returns:
            True if successful
        """
        try:
            container.remove(force=force)
            return True
        except Exception as e:
            print(f"Error removing container: {e}")
            return False

    def cleanup_container(self, container_name: str) -> None:
        """
        Clean up a container by name (stop and remove)

        Args:
            container_name: Name of the container
        """
        try:
            container = self.client.containers.get(container_name)
            self.stop_container(container)
            self.remove_container(container)
        except docker.errors.NotFound:
            # Container doesn't exist, nothing to clean up
            pass
        except Exception as e:
            print(f"Error cleaning up container: {e}")

    def list_test_containers(self) -> list:
        """
        List all test containers (running or stopped)

        Returns:
            List of container objects
        """
        try:
            # Get all containers with our image
            containers = self.client.containers.list(
                all=True,
                filters={'ancestor': f"{self.image_name}:{self.image_tag}"}
            )
            return containers
        except Exception as e:
            print(f"Error listing containers: {e}")
            return []

    def cleanup_all_test_containers(self) -> int:
        """
        Stop and remove all test containers

        Returns:
            Number of containers cleaned up
        """
        containers = self.list_test_containers()
        count = 0

        for container in containers:
            try:
                self.stop_container(container)
                self.remove_container(container)
                count += 1
            except Exception as e:
                print(f"Error cleaning up container {container.name}: {e}")

        return count


if __name__ == "__main__":
    # Simple test
    import sys
    from pathlib import Path

    if len(sys.argv) < 2:
        print("Usage: docker_manager.py <dockerfile_path>")
        sys.exit(1)

    dockerfile = Path(sys.argv[1])

    if not dockerfile.exists():
        print(f"Dockerfile not found: {dockerfile}")
        sys.exit(1)

    manager = DockerManager(dockerfile)

    print("Building image...")
    if manager.build_image():
        print("✓ Image built successfully")
    else:
        print("✗ Failed to build image")
        sys.exit(1)

    print(f"\nTest containers: {len(manager.list_test_containers())}")
