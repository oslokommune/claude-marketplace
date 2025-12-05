# Testing Framework Dockerfile
# Based on .devcontainer/Dockerfile with tmux and test configuration

FROM node:20

ARG TZ=Europe/Oslo
ENV TZ="$TZ"

ARG CLAUDE_CODE_VERSION=latest

# Install basic development tools, iptables/ipset, and tmux
RUN apt-get update && apt-get install -y --no-install-recommends \
  less \
  git \
  procps \
  sudo \
  fzf \
  zsh \
  man-db \
  unzip \
  gnupg2 \
  gh \
  iptables \
  ipset \
  iproute2 \
  dnsutils \
  aggregate \
  jq \
  nano \
  vim \
  curl \
  tmux \
  && apt-get clean && rm -rf /var/lib/apt/lists/*

# Ensure default node user has access to /usr/local/share
RUN mkdir -p /usr/local/share/npm-global && \
  chown -R node:node /usr/local/share

ARG USERNAME=node

# Persist bash history
RUN SNIPPET="export PROMPT_COMMAND='history -a' && export HISTFILE=/commandhistory/.bash_history" \
  && mkdir /commandhistory \
  && touch /commandhistory/.bash_history \
  && chown -R $USERNAME /commandhistory

# Set `DEVCONTAINER` environment variable
ENV DEVCONTAINER=true

# Create workspace, config, and test directories
RUN mkdir -p /workspace /home/node/.claude /transcripts /artifacts && \
  chown -R node:node /workspace /home/node/.claude /transcripts /artifacts

WORKDIR /workspace

# Install git-delta
ARG GIT_DELTA_VERSION=0.18.2
RUN ARCH=$(dpkg --print-architecture) && \
  wget "https://github.com/dandavison/delta/releases/download/${GIT_DELTA_VERSION}/git-delta_${GIT_DELTA_VERSION}_${ARCH}.deb" && \
  sudo dpkg -i "git-delta_${GIT_DELTA_VERSION}_${ARCH}.deb" && \
  rm "git-delta_${GIT_DELTA_VERSION}_${ARCH}.deb"

# Set up non-root user
USER node

# Install global packages
ENV NPM_CONFIG_PREFIX=/usr/local/share/npm-global
ENV PATH=$PATH:/usr/local/share/npm-global/bin

# Set the default shell to zsh
ENV SHELL=/bin/zsh

# Set the default editor
ENV EDITOR=nano
ENV VISUAL=nano

# Install zsh-in-docker
ARG ZSH_IN_DOCKER_VERSION=1.2.0
RUN sh -c "$(wget -O- https://github.com/deluan/zsh-in-docker/releases/download/v${ZSH_IN_DOCKER_VERSION}/zsh-in-docker.sh)" -- \
  -p git \
  -p fzf \
  -a "source /usr/share/doc/fzf/examples/key-bindings.zsh" \
  -a "source /usr/share/doc/fzf/examples/completion.zsh" \
  -a "export PROMPT_COMMAND='history -a' && export HISTFILE=/commandhistory/.bash_history" \
  -x

# Install Claude Code
RUN npm install -g @anthropic-ai/claude-code@${CLAUDE_CODE_VERSION}

# Install UV (Python package manager)
RUN curl -LsSf https://astral.sh/uv/install.sh | sh
ENV PATH="/home/node/.local/bin:$PATH"

# Install AWS CLI
RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
RUN unzip awscliv2.zip
USER root
RUN ./aws/install
USER node

# Copy plugins to the Claude plugins directory
# This will be done via volume mount in docker-compose/orchestrator
# to allow for easy updates without rebuilding

# Create Claude Code directory structure to skip first-run wizard
RUN mkdir -p /home/node/.claude/plugins/marketplaces/origo \
  /home/node/.claude/debug \
  /home/node/.claude/projects \
  /home/node/.claude/shell-snapshots \
  /home/node/.claude/statsig \
  /home/node/.claude/todos

# Copy Claude configuration files into the image
# This provides the base configuration including enabled plugins
# Note: System prompt is passed via --system-prompt flag in test_runner.py
COPY --chown=node:node settings.json /home/node/.claude/settings.json

# Create statsig stable_id file to skip first-run wizard
# This file signals that Claude has been initialized before
# Use a realistic numeric suffix like the actual wizard creates
RUN echo '"00000000-0000-0000-0000-000000000000"' > /home/node/.claude/statsig/statsig.stable_id.1234567890 && \
  chown -R node:node /home/node/.claude

# Set up tmux configuration for test automation
RUN echo "set -g mouse on" > /home/node/.tmux.conf && \
  echo "set -g history-limit 10000" >> /home/node/.tmux.conf && \
  echo "set -g default-terminal 'screen-256color'" >> /home/node/.tmux.conf

USER node
WORKDIR /workspace

# Entry point will be set by orchestrator
CMD ["/bin/bash"]
