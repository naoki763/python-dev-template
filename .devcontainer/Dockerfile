FROM mcr.microsoft.com/devcontainers/python:3.12-bookworm

USER vscode

#devcontainer環境にuvをインストール
RUN curl -LsSf https://astral.sh/uv/install.sh | sh
#uvのパスを通す
ENV PATH="/home/vscode/.local/bin:${PATH}"

WORKDIR /home/vscode
RUN uv venv
