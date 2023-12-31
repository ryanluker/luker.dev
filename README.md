Git repository and discussion area for my personal blog.

### Install
wget https://github.com/getzola/zola/releases/download/v0.12.2/zola-v0.12.2-x86_64-unknown-linux-gnu.tar.gz

tar -xf zola-v0.12.2-x86_64-unknown-linux-gnu.tar.gz

### Local build and serve
https://www.getzola.org/documentation/getting-started/cli-usage/#serve  
`zola serve`

### URL Staleness checkings
`zola check`

### Cloudflare Pages
```
Build command:
zola build

Build output directory:
/public

Root directory:
/

Build comments on pull requests:
Enabled
```
`ZOLA_VERSION` -> 0.12.2
