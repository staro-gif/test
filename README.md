# Cloud Task Scaffold

このディレクトリは、GitHub Actions 上で定期実行できる最小構成です。

## 含まれるもの

- `.github/workflows/cloud-task.yml`
  - 手動実行 (`workflow_dispatch`)
  - 毎日 09:00 JST 実行 (`cron`)
- `scripts/task.py`
  - 実タスクの入口
- `.env.example`
  - 必要になりそうな環境変数の雛形

## 想定する使い方

1. このディレクトリを GitHub リポジトリとして管理する
2. GitHub に push する
3. 必要な secrets / variables を GitHub Actions に設定する
4. `scripts/task.py` に本来の処理を書く

## 最短セットアップ

この Mac では、現時点で Apple Command Line Tools が未設定のため `git` が動きません。
先に以下を 1 回だけ実行します。

```bash
xcode-select --install
```

インストール完了後に、次を実行します。

```bash
cd "/Users/cova/Documents/旅行マーケティング"
git init
git add .
git commit -m "Add cloud task scaffold"
git branch -M main
git remote add origin https://github.com/<your-account>/<your-repo>.git
git push -u origin main
```

## ローカル実行

```bash
python3 scripts/task.py
```

## GitHub Actions での設定

必要に応じて GitHub リポジトリの `Settings > Secrets and variables > Actions` に以下を追加します。

- `TASK_ENDPOINT`
- `TASK_API_KEY`
- `TASK_NAME`

`TASK_NAME` は variable、`TASK_ENDPOINT` と `TASK_API_KEY` は secret に入れる想定です。

## スケジュール

`.github/workflows/cloud-task.yml` は UTC で指定します。

- `0 0 * * *` = 毎日 09:00 JST

必要ならこの後で、実際の処理内容に合わせて以下のどれかへ寄せられます。

- GitHub Actions のまま運用
- Google Cloud Run Jobs
- AWS Lambda + EventBridge
- cron を持つ VPS / コンテナ
