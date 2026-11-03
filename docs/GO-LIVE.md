# Put the new site live at prismcortex.net

The plan is to host the site on **AWS Amplify**, the same way I Crit You Not! is hosted. Every push to GitHub redeploys the site. Static hosting costs about $0–2 a month.

## What you do, and what Claude does

| Step | Who | Time |
|---|---|---|
| 1. Create an empty GitHub repo named `prismcortex-site` | You | 1 min |
| 2. Push the site and its generator to the repo | Claude | done for you |
| 3. Save two files from Square | You | 5 min |
| 4. Connect the repo to Amplify and check the test link | You | 10 min |
| 5. Point prismcortex.net at Amplify | You | 15 min, then up to an hour to take effect |
| 6. Turn off the Square Online site | You | 5 min |

## 1. Create the repo
On github.com, create a **new repository** called `prismcortex-site` under N8ofBase. Leave it empty, with no README. Tell Claude when it exists.

## 3. Save these from Square before you switch
These two files live on Square. The first will break when the domain moves, and the second disappears when you turn off the Square site.
- **I Crit You Not! rulebook PDF:** go to prismcortex.net/icyn, click Download, and send the PDF to Claude. Claude will put it in the site so the links keep working.
- **The "board game music" video** on the old home page: download it from Square Online, under Website > Media, and put it on YouTube. Then send Claude the YouTube link.

## 4. Connect Amplify
1. In the AWS Console, open **Amplify**, choose **Create new app**, then **GitHub**, and pick `N8ofBase/prismcortex-site` with the `main` branch.
2. Build settings: Amplify detects the `amplify.yml` in the repo and publishes the `site/` folder. There's no build step.
3. Click **Deploy**. Open the `https://main.xxxx.amplifyapp.com` test link and click through every page.
4. Go to **Hosting**, then **Rewrites and redirects**, choose **Manage redirects**, then **Open text editor**. Paste the contents of `amplify-redirects.json` and save. This sends old links like `/icyn` and `/chooselove` to their new homes.

## 5. Point the domain
1. In the Amplify app, go to **Hosting**, then **Custom domains**, then **Add domain**, and enter `prismcortex.net`.
2. Set up the root `prismcortex.net` and `www` to show the site. Have `www` redirect to the root.
3. **If the domain's DNS is in Route 53**, Amplify adds the records for you. Just approve.
   **If it isn't**, for example if the DNS is at Square or another registrar, Amplify shows you a verification CNAME and the records to add. Add them where the domain's DNS is managed.
4. Square Online is currently attached to the domain. In Square, go to **Website**, then **Domains**, and disconnect prismcortex.net from the Square site. Do this first if Square manages your DNS, or Amplify can't verify the domain.
5. **Don't touch these records:**
   - the **MX** and email **TXT** records, which run n8gr8@ email
   - the `icyn` record, for I Crit You Not!
   - the `bbg` record, for the Bearded Board Games link

   Amplify changes only the root and `www`.
6. Amplify issues the HTTPS certificate on its own. It usually takes 15–60 minutes.

## 6. After it's live
- Check prismcortex.net, the old `/icyn` link, and an email to n8gr8@prismcortex.net.
- In Square, downgrade the **Online** site plan to Free, or unpublish the site. Keep your Square account, since the POS and card payments use it.
- Submit `https://prismcortex.net/sitemap.xml` in Google Search Console. This is optional, but it helps Google pick up the new pages.

## Rollback
If anything looks wrong, reconnect the domain to Square Online and remove it from Amplify. The old site comes back within the hour.
