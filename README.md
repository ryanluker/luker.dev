![Blog CI](https://github.com/ryanluker/luker.dev/actions/workflows/CI.yml/badge.svg?branch=main)

Git repository and discussion area for my personal blog.

### Install UV
https://docs.astral.sh/uv/getting-started/installation/#installation-methods
```
pipx install uv
```

### Local build and serve
```
uv install
uv run render.py
```

### Publish
```
uv run render
```

### Cloudflare Pages
```
Build command:
exit 0

Build output directory:
/public

Root directory:
/

Build comments on pull requests:
Enabled
```
