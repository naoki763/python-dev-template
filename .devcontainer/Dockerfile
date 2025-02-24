FROM mcr.microsoft.com/devcontainers/python:3.12-bookworm

# devcontainer環境にuvをインストール
RUN curl -LsSf https://astral.sh/uv/install.sh | sh && \
    mv ~/.local/bin/uv /usr/local/bin/uv && \
    chmod +x /usr/local/bin/uv && \
    uv --version

# devcontainer環境に Task をインストール
RUN curl -LsSf https://taskfile.dev/install.sh | sh -s -- -b /usr/local/bin && \
    chmod +x /usr/local/bin/task && \
    task --version

# devcontainer環境に Docker Compose をインストール
RUN curl -SL "https://github.com/docker/compose/releases/latest/download/docker-compose-linux-x86_64" -o /usr/local/bin/docker-compose && \
    chmod +x /usr/local/bin/docker-compose

# mise（バージョン管理ツール）をインストール
RUN curl -fsSL https://mise.run | sh && \
    ln -s /root/.local/bin/mise /usr/local/bin/mise && \
    mise --version

# PATH を適切に設定
ENV PATH="/root/.local/bin:${PATH}"