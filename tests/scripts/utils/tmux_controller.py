#!/usr/bin/env python3
# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "docker",
# ]
# ///

"""
Tmux Controller - Control tmux sessions and inject answers

Manages tmux sessions within Docker containers and sends keypresses
to inject answers into Claude Code sessions.
"""

import time
from typing import Optional, List
from dataclasses import dataclass


@dataclass
class Answer:
    """Represents an answer to inject"""
    header: str
    value: str


class TmuxController:
    """Control tmux sessions in Docker containers"""

    def __init__(self, container, session_name: str = "claude"):
        """
        Initialize tmux controller

        Args:
            container: Docker container object
            session_name: Name of the tmux session
        """
        self.container = container
        self.session_name = session_name

    def create_session(self, command: Optional[str] = None, env_vars: Optional[dict] = None) -> bool:
        """
        Create a new tmux session

        Args:
            command: Optional command to run in the session
            env_vars: Optional environment variables to set

        Returns:
            True if successful
        """
        try:
            # Build environment prefix if env_vars provided
            env_prefix = ""
            if env_vars:
                env_parts = [f"{k}={v}" for k, v in env_vars.items()]
                env_prefix = " ".join(env_parts) + " "

            # Create new detached session with command
            if command:
                # Use sh -c to properly handle environment variables
                full_command = f'{env_prefix}{command}'
                cmd = f"tmux new-session -d -s {self.session_name} sh -c '{full_command}'"
            else:
                cmd = f"tmux new-session -d -s {self.session_name}"

            result = self.container.exec_run(cmd, user="node")
            return result.exit_code == 0
        except Exception as e:
            print(f"Error creating tmux session: {e}")
            return False

    def session_exists(self) -> bool:
        """Check if the tmux session exists"""
        try:
            cmd = f"tmux has-session -t {self.session_name} 2>/dev/null"
            result = self.container.exec_run(cmd, user="node")
            return result.exit_code == 0
        except Exception:
            return False

    def send_keys(self, keys: str, literal: bool = False) -> bool:
        """
        Send keys to the tmux session

        Args:
            keys: Keys to send
            literal: If True, send keys literally without interpretation

        Returns:
            True if successful
        """
        try:
            # Escape special characters for shell
            escaped = keys.replace('"', '\\"').replace("$", "\\$").replace("`", "\\`")

            # Use -l flag for literal input
            literal_flag = "-l " if literal else ""

            cmd = f'tmux send-keys -t {self.session_name} {literal_flag}"{escaped}"'
            result = self.container.exec_run(cmd, user="node")
            return result.exit_code == 0
        except Exception as e:
            print(f"Error sending keys: {e}")
            return False

    def send_enter(self) -> bool:
        """Send Enter key"""
        return self.send_keys("Enter", literal=False)

    def send_text(self, text: str) -> bool:
        """
        Send text literally (without tmux key interpretation)

        Args:
            text: Text to send

        Returns:
            True if successful
        """
        return self.send_keys(text, literal=True)

    def send_answers(self, answers: List[Answer], wait_time: float = 0.5) -> bool:
        """
        Send answers to questions

        Note: This is a simplified implementation. The actual implementation
        would need to understand Claude Code's question UI format.

        Args:
            answers: List of Answer objects
            wait_time: Time to wait between inputs (seconds)

        Returns:
            True if all answers sent successfully
        """
        try:
            for answer in answers:
                # Send the answer value
                if not self.send_text(answer.value):
                    return False

                time.sleep(wait_time)

                # Press Enter to confirm
                if not self.send_enter():
                    return False

                time.sleep(wait_time)

            return True
        except Exception as e:
            print(f"Error sending answers: {e}")
            return False

    def send_prompt(self, prompt: str) -> bool:
        """
        Send a prompt to Claude Code

        Args:
            prompt: The prompt text to send

        Returns:
            True if successful
        """
        try:
            # Wait a bit for Claude Code to be ready
            time.sleep(1)

            # Send the prompt text
            if not self.send_text(prompt):
                return False

            # Wait a bit before sending Enter
            time.sleep(0.5)

            # Press Enter to submit
            if not self.send_enter():
                return False

            return True
        except Exception as e:
            print(f"Error sending prompt: {e}")
            return False

    def get_pane_content(self) -> Optional[str]:
        """
        Get the current content of the tmux pane

        Returns:
            Pane content as string, or None if error
        """
        try:
            cmd = f"tmux capture-pane -t {self.session_name} -p"
            result = self.container.exec_run(cmd, user="node")

            if result.exit_code == 0:
                return result.output.decode('utf-8', errors='ignore')
            return None
        except Exception as e:
            print(f"Error getting pane content: {e}")
            return None

    def kill_session(self) -> bool:
        """Kill the tmux session"""
        try:
            cmd = f"tmux kill-session -t {self.session_name}"
            result = self.container.exec_run(cmd, user="node")
            return result.exit_code == 0
        except Exception:
            return False

    def wait_for_text(
        self,
        text: str,
        timeout: float = 30,
        poll_interval: float = 0.5
    ) -> bool:
        """
        Wait for specific text to appear in the pane

        Args:
            text: Text to wait for
            timeout: Maximum time to wait (seconds)
            poll_interval: How often to check (seconds)

        Returns:
            True if text found within timeout
        """
        elapsed = 0
        while elapsed < timeout:
            content = self.get_pane_content()
            if content and text in content:
                return True

            time.sleep(poll_interval)
            elapsed += poll_interval

        return False


if __name__ == "__main__":
    # This would be used from the orchestrator with a real Docker container
    print("TmuxController is a library module")
    print("Usage: from tmux_controller import TmuxController")
