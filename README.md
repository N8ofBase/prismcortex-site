# prismcortex.net

The Prism Cortex Solutions website: technology and game solutions, built with love.

- `site/` is the static site that Amplify publishes. Don't edit it by hand.
- `generator/build.py` builds every page in `site/`. Edit it, then run `python3 generator/build.py`.
- `amplify.yml` tells AWS Amplify to publish `site/` with no build step. Every push to `main` redeploys the site.
- `amplify-redirects.json` sends old Square URLs to their new pages. Paste it into Amplify under Hosting, then Rewrites and redirects.
- `docs/GO-LIVE.md` has the steps for pointing prismcortex.net at Amplify.
