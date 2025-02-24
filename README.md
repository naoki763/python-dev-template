# Dev Container セットアップガイド

この README では、開発環境用の Dev Container のセットアップ方法と使用方法について説明します。

## 前提条件

Dev Container を使用する前に、以下がインストールされていることを確認してください。

- [Docker](https://www.docker.com/get-started)
- [VS Code](https://code.visualstudio.com/)
- [Dev Containers 拡張機能](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)

## セットアップ手順

### 1. VS Code でプロジェクトを開く

```sh
code .
```

### 2. Dev Container で再オープン

1. コマンドパレットを開く（`Ctrl + Shift + P` または `Cmd + Shift + P` (macOS)）。
2. **「Reopen in Container」** を選択。
3. VS Code が `devcontainer.json` および `docker-compose.yml` を使用してコンテナをビルドし、起動します。

## Dev Container の設定

### `devcontainer.json`
このファイルは Dev Container のセットアップを定義し、以下の設定を含みます。
- Docker Compose ファイルとサービスの指定
- VS Code 拡張機能のインストール
- Python 環境の設定
- ポストスタートコマンドの実行（仮想環境のセットアップなど）

### `docker-compose.yml`
このファイルは Dev Container を実行するために必要なサービスやボリュームを定義します。
- ホストのワークスペースをコンテナにマウント
- コンテナ内で Docker を利用できるよう設定

## ワークスペースフォルダ

コンテナ内のルートワークスペースディレクトリは以下のように設定されています。

```json
"workspaceFolder": "/workspace"
```

プロジェクトファイルが正しくこのディレクトリにマウントされていることを確認してください。

## インストールされる VS Code 拡張機能

Dev Container では以下の拡張機能が自動的にインストールされます。

- Python (`ms-python.python`)
- Ruff Linter (`charliermarsh.ruff`)
- Prettier (`esbenp.prettier-vscode`)
- Docker (`ms-azuretools.vscode-docker`)
- Docker Compose (`p1c2u.docker-compose`)

## Dev Container 内でのコマンド実行

コンテナ内では、通常のターミナルコマンドを実行できます。便利なコマンドの例を紹介します。

```sh
# Python バージョンの確認
python --version

# 仮想環境を有効化
source .venv/bin/activate

# 依存関係のインストール
uv sync
```

## トラブルシューティング

### コンテナが起動しない

- Docker が起動していることを確認してください。
- 以下のコマンドでログを確認できます。
  ```sh
  docker-compose logs -f
  ```

### 拡張機能がインストールされない

- VS Code の `Extensions` タブから手動でインストールしてください。

## Dev Container の停止と再起動

コンテナを停止するには以下のコマンドを実行します。
```sh
docker-compose down
```

再起動するには以下のコマンドを実行します。
```sh
docker-compose up -d
```

## まとめ

これで、開発用の Dev Container のセットアップと設定が完了しました。快適な開発をお楽しみください！🚀

