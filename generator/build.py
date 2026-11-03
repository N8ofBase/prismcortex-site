import pathlib
OUT = pathlib.Path(__file__).resolve().parent.parent / "site"
OLD = "https://www.prismcortex.net"
NAV = [("index.html","Home"),("games.html","Game Node"),("pos.html","POS Node (Beta)"),("solutions.html","Web Node (Beta)"),("videos.html","Video Node"),("music.html","Music Node"),("behind-the-brain.html","Behind the Brain"),("contact.html","Contact")]

def yt(vid, title):
    return f'<iframe loading="lazy" style="aspect-ratio:16/9;width:100%;border:0;border-radius:12px" src="https://www.youtube-nocookie.com/embed/{vid}" title="{title}" allow="encrypted-media; picture-in-picture" allowfullscreen></iframe>'

def vid(name, title, vertical=False):
    mw = "max-width:300px;margin:0 auto;" if vertical else ""
    return f'<video controls playsinline preload="none" poster="media/{name}.jpg" style="width:100%;{mw}display:block;border-radius:12px;aspect-ratio:{"9/16" if vertical else "16/9"};background:#000" src="media/{name}.mp4" title="{title}"></video>'

ICYN_PLAY = "https://icyn.prismcortex.net"
EMAIL = "n8gr8@prismcortex.net"
_defs,_paths = open(__file__.rsplit("/",1)[0]+"/brain_paths.txt").read().split("|||")
BRAIN = f'<svg width="0" height="0" style="position:absolute" aria-hidden="true"><defs>{_defs}<linearGradient id="pc-grad" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#ff4fd8"/><stop offset=".45" stop-color="#7a5cff"/><stop offset=".8" stop-color="#22d3ee"/><stop offset="1" stop-color="#facc15"/></linearGradient><symbol id="pc-brain" viewBox="70 150 475 525">{_paths}</symbol></defs></svg>'
NODES = [
 ("game","Game Node","#ff4fd8","games.html","I Crit You Not! online, plus board games with Bearded Board Games."),
 ("pos","Point of Sale Node","#facc15","pos.html","Bearded POS and custom registers for small shops."),
 ("web","Web Node","#22d3ee","solutions.html","Websites, online stores and companion apps."),
 ("video","Video Node","#7a5cff","videos.html","Tutorials, trailers, music videos and meditations."),
 ("music","Music Node","#3ddc97","music.html","Choose Love and board game songs."),
]
def node_graph():
    # node1 layout: one big hub, satellites on spokes; the hub is the node2 circuit brain
    pos=[(168,93),(432,93),(493,320),(102,303),(300,460)]
    cx,cy=300,250
    out=[f'<svg class="nodegraph" viewBox="0 -10 600 560" role="img" aria-label="The Cortex connected to five nodes: Game, Point of Sale, Web, Video and Music">']
    for (k,n,c,h,d),(x,y) in zip(NODES,pos):
        out.append(f'<line class="spoke" data-node="{k}" x1="{cx}" y1="{cy}" x2="{x}" y2="{y}" stroke="{c}" stroke-width="5" stroke-linecap="round"/>')
    out.append(f'<circle cx="{cx}" cy="{cy}" r="112" fill="var(--bg2)" stroke="url(#pc-grad)" stroke-width="5"/>')
    out.append(f'<use href="#pc-brain" x="{cx-78}" y="{cy-86}" width="156" height="172" fill="url(#pc-grad)"/>')
    for (k,n,c,h,d),(x,y) in zip(NODES,pos):
        out.append(f'<a href="{h}" class="sat" data-node="{k}"><circle cx="{x}" cy="{y}" r="46" fill="{c}"/><circle cx="{x}" cy="{y}" r="22" fill="var(--bg)"/><circle cx="{x}" cy="{y}" r="9" fill="{c}"/>'
                   f'<text x="{x}" y="{y+72 if y>250 else y-60}" text-anchor="middle" fill="var(--ink)" font-family="Space Grotesk, Inter, sans-serif" font-weight="700" font-size="22">{n.replace("Point of Sale","POS")}</text></a>')
    out.append('</svg>')
    return "".join(out)

BANNER='<section class="banner"><div class="banner-photo"><img src="img/n8-banner.jpg" alt="N8 grinning with his N8 guitar, waving, in front of glowing Cortex nodes and faint game art from I Crit You Not! and Bearded Board Games"><span class="hi">Hi, I&rsquo;m N8. Let&rsquo;s play.</span></div></section>'

def page(fname, title, desc, body, head=""):
    nav = "".join(f'<a href="{h}"{" aria-current=page" if h==fname else ""}>{t}</a>' for h,t in NAV)
    html = f'''<!doctype html>
<html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}"><meta property="og:site_name" content="Prism Cortex Solutions">
<meta name="theme-color" content="#0b0b12">
<link rel="icon" href="favicon.ico" sizes="any"><link rel="icon" type="image/png" href="favicon.png"><link rel="apple-touch-icon" href="img/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&family=Space+Grotesk:wght@600;700&display=swap">
<link rel="stylesheet" href="styles.css">
{head}
</head><body>
{BRAIN}
<header class="site"><div class="wrap">
<a class="logo" href="index.html"><img src="img/logo.png" alt="Prism Cortex Solutions" height="44" style="height:44px;width:auto"></a>
<button class="menu-btn" aria-label="Menu" onclick="document.querySelector('nav.main').classList.toggle('open')">☰</button>
<nav class="main">{nav}</nav>
</div></header>
<main>
{body}
</main>
<footer class="site"><div class="wrap">
<div><strong>Prism Cortex Solutions</strong><br>Technology &amp; game solutions, built with love.<br>Designed by a human, built with AI. <a href="solutions.html#ai">How we work</a><br><a href="mailto:{EMAIL}">{EMAIL}</a><br>Choose Love.</div>
<div>Explore<br><a href="games.html">Game Node</a> · <a href="pos.html">POS Node (Beta)</a> · <a href="solutions.html">Web Node</a> · <a href="videos.html">Video Node</a> · <a href="music.html">Music Node</a> · <a href="inspiration.html">Inspiration</a> · <a href="behind-the-brain.html">Behind the Brain</a></div>
<div>Friends<br><a href="https://beardedboardgames.com">beardedboardgames.com</a><br><a href="https://bbg.prismcortex.net">bbg.prismcortex.net</a></div>
<div>Become a Prismatic Fanatic<br><a href="contact.html">Join the email list →</a><br>© 2026 Prism Cortex Solutions</div>
</div></footer>
<script>(function(){{var g=document.querySelector('.nodegraph');if(!g)return;function on(k){{g.classList.add('focus');document.querySelectorAll('[data-node="'+k+'"]').forEach(function(e){{e.classList.add('on')}})}}function off(){{g.classList.remove('focus');document.querySelectorAll('[data-node].on').forEach(function(e){{e.classList.remove('on')}})}}document.querySelectorAll('[data-node]').forEach(function(e){{e.addEventListener('mouseenter',function(){{on(e.dataset.node)}});e.addEventListener('mouseleave',off)}})}})();</script>
</body></html>'''
    (OUT/fname).write_text(html, encoding="utf-8")

# ---------------- HOME ----------------
page("index.html","Prism Cortex Solutions | Technology & Game Solutions",
"Prism Cortex Solutions builds apps, websites, point-of-sale systems and board games. Home of I Crit You Not!, Bearded POS, and Choose Love.",
f'''
<section class="hero"><div class="wrap">
<img src="img/logo.png" alt="Powered by Prism Cortex Solutions" style="width:min(680px,100%);margin-bottom:28px">
<span class="eyebrow">Technology · Games · Music</span>
<h1>Bright ideas,<br><span class="grad">refracted into real things.</span></h1>
<p class="lead">Prism Cortex Solutions is a technology and game studio. We build apps, websites and point-of-sale systems for small businesses, and we design, print and release board games people actually want to play again.</p>
<div class="btns"><a class="btn primary" href="#nodes">Explore the nodes</a><a class="btn" href="contact.html">Start a project</a></div>
</div></section>
{BANNER}
<section class="alt nodes" id="nodes"><div class="wrap">
<span class="eyebrow">The Cortex</span>
<h2>What we're building</h2>
<p class="muted">One brain, many nodes. Every project we make plugs into one of them, and each node shares what it learns with the others.</p>
<div class="nodes-grid">
<div class="graph">{node_graph()}</div>
<div class="node-list">
 <article class="node" data-node="game" style="--c:#ff4fd8"><span class="term"></span><div><img class="node-logo" src="img/icyn-logo.png" alt="I Crit You Not! logo"><span class="tag">Online Game</span><h3>Game Node</h3>
  <p><strong>I Crit You Not!</strong> An 8-round duel of the mighty D20, playable in your browser. Fight the computer, pass and play with a friend, take on the Starvos boss, or challenge anyone online with a join code in ranked duels.</p>
  <p>Board games are created and released with Bearded Board Games at <a href="https://beardedboardgames.com">beardedboardgames.com</a> (see <a href="https://bbg.prismcortex.net">bbg.prismcortex.net</a>).</p>
  <a class="more" href="games.html">Enter the Game Node →</a></div></article>
 <article class="node" data-node="pos" style="--c:#facc15"><span class="term"></span><div><span class="tag">Point of sale · Beta</span><h3>Point of Sale Node <span class="beta">BETA</span></h3>
  <p><strong>Bearded POS</strong>, now in beta, is being built to run the register for Bearded Board Games: cash, card and split payments, barcode scanning, inventory, refunds, end-of-day drawer counts and Beard Bucks loyalty. The same core powers custom systems for other local shops.</p>
  <a class="more" href="pos.html">Build your POS →</a></div></article>
 <article class="node" data-node="web" style="--c:#22d3ee"><span class="term"></span><div><span class="tag">Web · Beta</span><h3>Web Node <span class="beta">BETA</span></h3>
  <p>Websites, online stores, crowdfunding pages and companion apps for creators and small businesses. Designed, built and supported locally.</p>
  <a class="more" href="solutions.html">Explore the Web Node →</a></div></article>
 <article class="node" data-node="video" style="--c:#7a5cff"><span class="term"></span><div><span class="tag">Video</span><h3>Video Node</h3>
  <p>Learn-to-play tutorials, game trailers, music videos like the captioned <em>Choose Love</em>, and guided meditations.</p>
  <a class="more" href="videos.html">Watch the Video Node →</a></div></article>
 <article class="node" data-node="music" style="--c:#3ddc97"><span class="term"></span><div><span class="tag">Music</span><h3>Music Node</h3>
  <p>Our anthem <em>Choose Love</em>, board game music that combines our two favorite things, and the songs that started it all.</p>
  <a class="more" href="music.html">Listen to the Music Node →</a></div></article>
</div></div>
</div></section>

<section><div class="wrap feature">
<div>
<span class="eyebrow">Board game creation &amp; release</span>
<h2>From prototype to the table</h2>
<p class="muted">Prism Cortex is a creative partner behind <strong>Bearded Board Games</strong> from St. Louis: quick, fun games that are easy to teach and hard to put down. Fences, Locked Out and more are out now, and Pack Lash, Mine &amp; Find and Soccer Blocker are on the way.</p>
<ul class="ticks"><li>Game design, playtesting and rulebooks</li><li>Print &amp; play, production and launch</li><li>Release and sales at beardedboardgames.com</li></ul>
<div class="btns"><a class="btn primary" href="https://beardedboardgames.com">Visit beardedboardgames.com</a><a class="btn" href="https://bbg.prismcortex.net">bbg.prismcortex.net</a></div>
</div>
<div class="logo-wall"><img class="bbg" src="img/bbg-logo.png" alt="Bearded Board Games logo"><img src="img/game-fences.jpg" alt="Fences cover" loading="lazy"><img src="img/game-locked-out.jpg" alt="Locked Out cover" loading="lazy"><img src="img/game-pack-lash.jpg" alt="Pack Lash cover" loading="lazy"><img src="img/game-mine-find.jpg" alt="Mine &amp; Find cover" loading="lazy"><img src="img/game-soccer-blocker.jpg" alt="Soccer Blocker cover" loading="lazy"><img src="img/icyn-logo.png" alt="I Crit You Not! cover" loading="lazy"></div>
</div></section>

<section class="alt"><div class="wrap feature">
<div><img src="img/choose-love.jpg" alt="Choose Love: a rainbow brain flowing into a rainbow heart" style="border-radius:var(--r)"></div>
<div>
<span class="eyebrow">Music Node</span>
<h2>Choose Love</h2>
<p class="muted">Music has always been part of the Prism Cortex story, from the anthem <em>Choose Love</em> to board game music that combines our two favorite things: music and gaming.</p>
<div class="btns"><a class="btn" href="music.html">Listen to the music</a></div>
</div>
</div></section>

<section><div class="wrap">
<p class="quote">“Combining my 2 favorite things, music and gaming.”</p>
<p class="muted">Who&rsquo;s behind the brain? Meet N8, the musician, game designer and dreamer who runs Prism Cortex, in <a href="behind-the-brain.html">Behind the Brain</a>.</p>
</div></section>
''')

# ---------------- WEB NODE ----------------
WEB_PROJECTS=[("starter","Starter site",599,"Up to 5 pages, phone-friendly, contact form, basic search setup, one round of changes."),
 ("business","Business site",1199,"Up to 12 pages with your store or booking, email sign-up, two rounds of changes."),
 ("game","Browser game prototype",1500,"A playable 1v1 browser game built from your rules, like I Crit You Not!"),
 ("app","Custom web app",2500,"Logins, data and dashboards. Starting price; quoted up front after a free call.")]
WEB_ADDONS=[("store","Online store",300),("booking","Booking &amp; calendar",200),("pages","5 more pages",200),("brand","Logo &amp; brand kit",250),("multi","Online multiplayer &amp; accounts",1000),("rules","Rulebook &amp; print-and-play layout",349)]
WEB_HOST=[("none","No hosting (you host it)",0),("host","Host",15),("care","Care",39),("server","Game server",49)]
proj="".join(f'<label class="opt"><input type="radio" name="proj" value="{k}" data-price="{v}"{" checked" if i==0 else ""}><span><strong>{n}</strong><em>{d}</em></span><b>from ${v:,}</b></label>' for i,(k,n,v,d) in enumerate(WEB_PROJECTS))
adds="".join(f'<label class="opt"><input type="checkbox" value="{k}" data-price="{v}"><span><strong>{n}</strong></span><b>+${v:,}</b></label>' for k,n,v in WEB_ADDONS)
host="".join(f'<label class="opt"><input type="radio" name="host" value="{k}" data-price="{v}"{" checked" if k=="care" else ""}><span><strong>{n}</strong></span><b>{"$"+str(v)+"/mo" if v else "$0"}</b></label>' for k,n,v in WEB_HOST)
page("solutions.html","Web Node | Prism Cortex Solutions",
"Websites, browser games, online stores and hosting from Prism Cortex Solutions, with a plain pricing guide.",
f"""
<section class="hero"><div class="wrap">
<span class="beta-pill-dark">BETA</span>
<span class="eyebrow">Web Node</span>
<h1>Websites and games that <span class="grad">think fast</span></h1>
<p class="lead">We design, build and host websites, online stores, browser games and web apps for creators and small businesses. Plain prices, no surprises.</p>
<p class="beta-line">The Web Node is in beta: I&rsquo;m taking on a small number of founding clients while I build out the service, at founding-client prices.</p>
<div class="btns"><a class="btn primary" href="#estimate">Estimate your project</a><a class="btn" href="contact.html">Start a project</a></div>
</div></section>

<section class="alt"><div class="wrap">
<h2>Pricing guide</h2>
<p class="muted">Starting prices for most projects. Anything unusual is quoted in writing before work begins.</p>
<div class="beta-offer"><span class="beta">BETA</span><p><strong>Founding client pricing.</strong> While Prism Cortex Solutions is in beta, the first 10 clients get <strong>25% off any build</strong> and keep their hosting rate locked for 12 months. In return, we ask for honest feedback and permission to show your project.</p></div>
<div class="price-cols">
 <div class="pcard"><h3>Web design</h3><ul class="plist">
  <li><span>Starter site<em>up to 5 pages</em></span><b>$599</b></li>
  <li><span>Business site<em>up to 12 pages, store or booking</em></span><b>$1,199</b></li>
  <li><span>Custom web app<em>logins, data, dashboards</em></span><b>from $2,500</b></li>
  <li><span>Online store add-on</span><b>$300</b></li>
  <li><span>Logo &amp; brand kit</span><b>$250</b></li></ul></div>
 <div class="pcard"><h3>Game design</h3><ul class="plist">
  <li><span>Browser game prototype<em>playable 1v1 from your rules</em></span><b>from $1,500</b></li>
  <li><span>Online multiplayer &amp; accounts</span><b>from $1,000</b></li>
  <li><span>Rulebook &amp; print-and-play layout</span><b>$349</b></li>
  <li><span>Playtest &amp; design consult</span><b>$50/hr</b></li></ul></div>
 <div class="pcard"><h3>Hosting &amp; care</h3><ul class="plist">
  <li><span>Host<em>hosting, security certificate, daily backups</em></span><b>$15/mo</b></li>
  <li><span>Care<em>Host plus updates, uptime checks and 1 hour of changes a month</em></span><b>$39/mo</b></li>
  <li><span>Game server<em>multiplayer, sign-in and stats; heavy traffic billed at cost</em></span><b>$49/mo</b></li>
  <li><span>Anything else</span><b>$50/hr</b></li></ul></div>
</div>
<p class="muted fine">No contracts on hosting. You own your domain, your code and your content, and we hand everything over if you leave.</p>
</div></section>

<section id="estimate"><div class="wrap">
<h2>Estimate your project</h2>
<div class="est">
 <div class="est-opts">
  <fieldset><legend>1. What are we building?</legend>{proj}</fieldset>
  <fieldset><legend>2. Add-ons</legend>{adds}</fieldset>
  <fieldset><legend>3. Hosting</legend>{host}</fieldset>
 </div>
 <aside class="est-out" aria-live="polite">
  <p class="lbl">Your estimate</p>
  <p class="big" id="est-once">$599</p><p class="sub">one time, regular price</p>
  <p class="beta-price" id="est-beta"></p>
  <p class="big2" id="est-month">$39/mo</p>
  <ul id="est-lines"></ul>
  <a class="btn primary" id="est-send" href="mailto:{EMAIL}">Email me this estimate</a>
  <p class="sub">A starting estimate. We confirm the final price in writing after a free call.</p>
 </aside>
</div>
</div></section>

<section class="alt" id="ai"><div class="wrap feature">
<div>
<span class="eyebrow">How we work</span>
<h2>Designed by a human, built with AI</h2>
<p class="muted">Prism Cortex Solutions is one St. Louis maker working with AI tools. I plan every project, make the design calls, and test and review everything before it ships. AI helps me write code, copy and tests faster, which keeps prices fair for small businesses.</p>
<ul class="ticks"><li>You talk to a person, start to finish</li><li>Every line that ships is reviewed and tested</li><li>Your data is never used to train anyone's AI model</li></ul>
</div>
<div class="shot">Human ideas × AI speed</div>
</div></section>

<section><div class="wrap">
<h2>Built by the Web Node</h2>
<div class="grid">
 <div class="card"><span class="tag">Online Game</span><h3>I Crit You Not!</h3><p>A browser duel with computer, pass and play, boss and online modes.</p><a class="more" href="{ICYN_PLAY}">Play at icyn.prismcortex.net →</a></div>
 <div class="card"><span class="tag">Point of sale · Beta</span><h3>Bearded POS</h3><p>Register, inventory, customers and an online store for an independent board game shop. In beta.</p><a class="more" href="pos.html">See the POS →</a></div>
 <div class="card"><span class="tag">Website</span><h3>prismcortex.net</h3><p>This site, rebuilt from a Square Online store into a fast static site.</p></div>
</div>
</div></section>
<script>
(function(){{
var root=document.getElementById('estimate');if(!root)return;
function money(n){{return '$'+n.toLocaleString('en-US')}}
function name(i){{return i.closest('label').querySelector('strong').textContent}}
function render(){{
 var p=root.querySelector('input[name=proj]:checked'),h=root.querySelector('input[name=host]:checked');
 var adds=[].slice.call(root.querySelectorAll('input[type=checkbox]:checked'));
 var once=+p.dataset.price+adds.reduce(function(t,i){{return t+ +i.dataset.price}},0),mo=+h.dataset.price;
 root.querySelector('#est-once').textContent=money(once);
 var beta=Math.round(once*0.75);root.querySelector('#est-beta').innerHTML='<span class=beta>BETA</span> Founding client: <strong>'+money(beta)+'</strong>';
 root.querySelector('#est-month').textContent=mo?money(mo)+'/mo':'No monthly fee';
 var lines=[[name(p),money(+p.dataset.price)]].concat(adds.map(function(i){{return [name(i),'+'+money(+i.dataset.price)]}}));
 if(mo)lines.push([name(h)+' hosting',money(mo)+'/mo']);
 root.querySelector('#est-lines').innerHTML=lines.map(function(l){{return '<li><span>'+l[0]+'</span><span>'+l[1]+'</span></li>'}}).join('');
 var body=lines.map(function(l){{return l[0]+': '+l[1]}}).join('\\n')+'\\n\\nEstimate: '+money(once)+' one time (founding client price '+money(Math.round(once*0.75))+')'+(mo?' + '+money(mo)+'/mo':'');
 root.querySelector('#est-send').href='mailto:{EMAIL}?subject='+encodeURIComponent('Project estimate: '+name(p))+'&body='+encodeURIComponent(body);
}}
root.addEventListener('change',render);render();
}})();
</script>
""")

# ---------------- GAMES ----------------
games = [
 ("Fences","Out now","Our flagship tile-and-fence game, with The Ranch, Seasons, a 5–6 player expansion and Premium Print &amp; Play.","https://beardedboardgames.com/fences"),
 ("Locked Out","Out now","Quick to teach, hard to put down.","https://beardedboardgames.com/locked-out"),
 ("Pack Lash","Coming soon","Part of the Bearded Bundle for the 2026 holiday season. Reserve a VIP spot.","https://beardedboardgames.com/pack-lash"),
 ("Mine &amp; Find","Coming soon","Dig in and find the treasure.","https://beardedboardgames.com/mine-find"),
 ("Soccer Blocker","Coming soon","Soccer on a tabletop. Version Zero limited edition already exists.","https://beardedboardgames.com/soccer-blocker"),
 ("Fences: The Roll &amp; Write","Coming 2027","Fences reimagined as a roll &amp; write.","https://beardedboardgames.com/fences-the-roll-write"),
]
IMG={"Fences":"game-fences.jpg","Locked Out":"game-locked-out.jpg","Pack Lash":"game-pack-lash.jpg","Mine &amp; Find":"game-mine-find.jpg","Soccer Blocker":"game-soccer-blocker.jpg"}
cards = "".join(f'<div class="card">{"<img class=cover src=img/"+IMG[n]+" alt=\""+n+" cover\" loading=lazy>" if n in IMG else ""}<span class="tag{"" if s=="Out now" else " soon"}">{s}</span><h3>{n}</h3><p>{d}</p><a class="more" href="{u}">Details →</a></div>' for n,s,d,u in games)
pc = [("D20 On The Money","A dice game where the d20 decides your fortune."),
      ("Jibe Card Game","A fast card game.")]
pcards = "".join(f'<div class="card"><span class="tag">Prism Cortex original</span><h3>{n}</h3><p>{d}</p></div>' for n,d in pc)
page("games.html","Game Node | Prism Cortex Solutions",
"Board game creation and release with Bearded Board Games of St. Louis: Fences, Locked Out, Pack Lash, Mine & Find, Soccer Blocker and more.",
f'''
<section class="hero"><div class="wrap">
<span class="eyebrow">Game Node</span>
<h1>Games made <span class="grad">to be played again</span></h1>
<p class="lead">We make I Crit You Not! for the browser, and we design, test, print and release board games with Bearded Board Games, a St. Louis studio led by Adam Collins, Tim Forbis and Nate Sloan. Releases and the shop live at beardedboardgames.com.</p>
<div class="btns"><a class="btn primary" href="https://beardedboardgames.com">Shop at beardedboardgames.com</a><a class="btn" href="https://bbg.prismcortex.net">Board games at bbg.prismcortex.net</a></div>
</div></section>
{BANNER}
<section class="alt" id="icyn"><div class="wrap feature">
<div>
<img src="img/icyn-logo.png" alt="I Crit You Not! logo" style="width:180px;margin-bottom:12px">
<span class="tag">Online Game</span>
<h2>I Crit You Not!</h2>
<p class="muted"><a href="{ICYN_PLAY}">icyn.prismcortex.net</a> · An 8-round duel of the mighty D20. Roll for speed and luck, read the scroll tables, land crits and dodge fumbles.</p>
<ul class="ticks"><li>Duel the computer or pass and play with a friend</li><li>Boss mode against Starvos, with its own soundtrack</li><li>Online duels by join code, refereed by the server so nobody can predict a roll</li><li>Ranked results and stats when you sign in</li></ul>
<div class="btns"><a class="btn primary" href="{ICYN_PLAY}">Play I Crit You Not!</a><a class="btn" href="{OLD}/uploads/b/d5d189d0-c0a1-11ee-95ea-8f865d85c14c/abf933e0-3191-11f0-b222-ef4a5eb2a275.pdf">Tabletop rulebook (PDF)</a></div>
</div>
<div>{yt("RUon07ukD30","Learn to play I Crit You Not! with Lettuce Talk Games")}</div>
</div></section>
<section><div class="wrap">
<div class="bbg-head"><img src="img/bbg-logo.png" alt="Bearded Board Games logo"><div><h2>Bearded Board Games lineup</h2><p class="muted">Quick, fun games from St. Louis that are easy to teach and hard to put down.</p></div></div>
<div class="grid">{cards}</div>
<p class="muted" style="margin-top:24px">🎁 <strong>The Bearded Bundle 2026:</strong> three new games for the 2026 holiday season. <a href="https://beardedboardgames.com/bb2026-vip">Sign up for 10% off</a>.</p>
</div></section>
''')

# ---------------- MUSIC ----------------
songs = [
 ("zofZiOmZw18","Choose Love","The heart of Prism Cortex. Choose Love."),
 ("E_wMmvCAAPA","My New Favorite Color","With POSTCARD."),
 ("3OhY0q5Mrtc","Savior Dreams","Music, lyrics and vocals by Nate Sloan. Performed and recorded by POSTCARD."),
 ("svt7yAM3WMc","The Mourning of Glory","Music, lyrics and vocals by Nate Sloan. Performed and recorded by POSTCARD."),
 ("WnqBvopaF5s","Snow","Inspired by Game of Thrones. Winter is coming."),
 ("JRUbnQxDSbw","N8's Blue Christmas",""),
]
LOCAL_SONGS={"3OhY0q5Mrtc":"savior-dreams","svt7yAM3WMc":"mourning-of-glory","WnqBvopaF5s":"snow"}
def _song(v,t,d):
    if v in LOCAL_SONGS:
        extra = ' <a href="https://www.youtube.com/watch?v=WnqBvopaF5s">Hear the full song on YouTube</a>.' if v=="WnqBvopaF5s" else ""
        return f'<div class="card"><h3>{t}</h3>{"<p>"+d+extra+"</p>" if (d or extra) else ""}{vid(LOCAL_SONGS[v],t)}</div>'
    return f'<div class="card"><h3>{t}</h3>{"<p>"+d+"</p>" if d else ""}{yt(v,t)}</div>'
srows = "".join(_song(v,t,d) for v,t,d in songs)
page("music.html","Music Node | Prism Cortex Solutions",
"Choose Love and board game parody songs from Prism Cortex.",
f'''
<section class="hero"><div class="wrap">
<span class="eyebrow">Music Node</span>
<h1><span class="grad">Choose Love</span></h1>
<img src="img/choose-love.jpg" alt="Choose Love: a rainbow brain flowing into a rainbow heart" style="border-radius:var(--r);margin-bottom:28px;width:min(900px,100%)">
<p class="lead">Songs from the Prism Cortex brain, from our anthem to board game parodies that combine our two favorite things, music and gaming.</p>
</div></section>
<section><div class="wrap feature">
<div><video controls playsinline preload="metadata" poster="media/choose-love-poster.jpg" style="width:100%;max-width:400px;border-radius:var(--r);display:block;margin:0 auto" src="media/choose-love.mp4"></video></div>
<div><span class="eyebrow">Watch with lyrics</span><h2>Choose Love</h2><p class="muted">Sing along with the captioned version of our anthem. Every word, right on screen.</p><div class="btns"><a class="btn" href="https://www.youtube.com/watch?v=zofZiOmZw18">Watch on YouTube</a></div></div>
</div></section>
<section class="alt"><div class="wrap">
<h2>Board game parody songs</h2>
<p class="muted">Songs about the games we love. <!-- TODO: add parody song titles + YouTube links --></p>
<div class="card"><h3>Board game music?</h3><p>Combining my 2 favorite things, music and gaming.</p>
<video controls style="width:100%;border-radius:12px" src="https://customer-ugajlzvkncemhxjh.cloudflarestream.com/abab3b5b0d9ae6782cf1544283d5dcc3/manifest/video.m3u8"></video>
<p class="muted" style="font-size:.85rem;margin-top:8px">Tip: upload this video to YouTube so it plays in every browser.</p></div>
</div></section>
<section><div class="wrap">
<h2>Songs</h2>
<div class="grid">{srows}</div>
</div></section>
''')

# ---------------- BEHIND THE BRAIN ----------------
def sec(title, inner, open_=False):
    return f'<details class="archive"{" open" if open_ else ""}><summary>{title}</summary>{inner}</details>'
products = """<ul class="ticks">
<li>I Crit You Not! $25 · I Crit You Not! Market $20</li><li>D20 On The Money $25 · D20 OTM Market $20</li>
<li>Fences $25 · Fences: The Ranch $25 · Fences: Seasons $5 · 5–6 Player Expansion $5 · Premium Print &amp; Play $8</li>
<li>Soccer Blocker Version Zero Limited Edition $30 · Mine Find $20 · Locked Out $20 · Jibe Card Game $10 · Pickleball $30</li>
<li>Pack Lash VIP Reservation $1</li><li>Project Lightbringer Mission 1: The Universe Medallion $5</li>
<li>Donation $2–100</li></ul>"""
# Old-site archive, hidden for now: still generated, but not linked or indexed.
page("archive.html","Behind the Brain Archive | Prism Cortex Solutions",
"The original Prism Cortex: board games with dice-rolling action, Project Lightbringer stories, inspiration, meditations, videos and merch.",
f'''
<section class="hero"><div class="wrap">
<span class="eyebrow">Behind the Brain</span>
<h1>Where <span class="grad">Prism Cortex</span> began</h1>
<p class="lead">Before Prism Cortex Solutions, there was Prism Cortex: board games with D&amp;D-style dice-rolling action, inspirational quotes, music, videos and writings. Everything from the original site is kept here. Choose Love!</p>
</div></section>
<section><div class="wrap">
{sec("Game Node", "<p>The original home of our games: I Crit You Not!, D20 On The Money, Mine Find, Soccer Blocker, Fences, Locked Out, Jibe and more.</p>"+yt("bhRmHTEea-A","D-20 On The Money trailer"), True)}
{sec("I Crit You Not! Quickstart, Rulebook &amp; Extras", f'<h3>Quickstart</h3><p>Learn to play I Crit You Not! with Sweaty Lettuce.</p>{yt("RUon07ukD30","ICYN tutorial")}<h3 style="margin-top:20px">Rulebook</h3><p><a href="{OLD}/uploads/b/d5d189d0-c0a1-11ee-95ea-8f865d85c14c/abf933e0-3191-11f0-b222-ef4a5eb2a275.pdf">Download the ICYN rulebook (PDF)</a></p><h3>Extras: The Lucklympics</h3>{yt("03IveFrhfCw","ICYN Lucklympics Edition")}')}
{sec("D20 Rules: D20 On The Money", "<p>D20 On The Money, available for online orders.</p>")}
{sec("Soccer Blocker", "<p>Soccer Blocker Version Zero Limited Edition. Now heading to release with Bearded Board Games.</p>"+'<video controls style="width:100%;border-radius:12px" src="https://customer-ugajlzvkncemhxjh.cloudflarestream.com/6cb268af2c95b2ff58e326e9cbacdd11/manifest/video.m3u8"></video>')}
{sec("Mine Find", "<p>Mine Find, now Mine &amp; Find from Bearded Board Games.</p>")}
{sec("Project Lightbringer", '<p>Our story universe, where you become a Lightbringer on the planet Talus. Read the prologue, <em>Terror on Talus</em>, and then <em>Project Lightbringer</em>.</p><p><a class="btn" href="lightbringer.html">Read the stories →</a></p><p class="muted">Mission 1: The Universe Medallion.</p>')}
{sec("Inspiration Node, ThotBot &amp; UrantiaBot", '<p>Choose Love, ThotBot, the UrantiaBot and guided meditations now live on their own page.</p><p><a class="btn" href="inspiration.html">Visit the Inspiration page →</a></p>')}
{sec("Videos", '<div class="grid">'+yt("Q3j1k2lna8A","I Crit You Not! on Lettuce Talk Games")+yt("BAYIJh4qq9Y","Gift for Gamers")+'</div>')}
{sec("The original shop", products)}
{sec("Support Prism Cortex", '<p>Donations of $2–100 kept the lights on and the dice rolling. Thank you! <a href="contact.html">Get in touch</a> to support the work.</p>')}
</div></section>
''', head='<meta name="robots" content="noindex">')

# ---------------- POS NODE ----------------
POS_HEAD = '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,500;12..96,700;12..96,800&family=Manrope:wght@400;500;700&display=swap"><link rel="stylesheet" href="pos.css">'
page("pos.html","POS Node | Prism Cortex Solutions",
"Point-of-sale systems for St. Louis small businesses: register, inventory, customers, booking and online store. Setup from $399, then $39 a month.",
open(__file__.rsplit("/",1)[0]+"/pos_body.html").read(), head=POS_HEAD)

# ---------------- VIDEO NODE ----------------
VIDS=[("RUon07ukD30","Learn to play I Crit You Not!","Lettuce Talk Games deep-dive tutorial"),("03IveFrhfCw","I Crit You Not! Lucklympics Edition",""),
("Q3j1k2lna8A","I Crit You Not! on Lettuce Talk Games",""),("bhRmHTEea-A","D-20 On The Money trailer",""),("BAYIJh4qq9Y","Gift for Gamers",""),
("zofZiOmZw18","Choose Love","Music video"),("hfhg6tk0M0g","Cosmic Meditation","10 minutes · more on the <a href=inspiration.html>Inspiration page</a>")]
vrows="".join(f'<div class="card"><h3>{t}</h3>{"<p>"+d+"</p>" if d else ""}{yt(v,t)}</div>' for v,t,d in VIDS)
page("videos.html","Video Node | Prism Cortex Solutions",
"Tutorials, trailers, music videos and meditations from Prism Cortex.",
f"""
<section class="hero"><div class="wrap">
<span class="eyebrow">Video Node</span>
<h1>Watch the <span class="grad">brain at work</span></h1>
<p class="lead">Learn-to-play tutorials, trailers, music videos and meditations.</p>
</div></section>
<section class="alt"><div class="wrap feature">
<div><video controls playsinline preload="metadata" poster="media/choose-love-poster.jpg" style="width:100%;max-width:400px;border-radius:var(--r);display:block;margin:0 auto" src="media/choose-love.mp4"></video></div>
<div><span class="eyebrow">New</span><h2>Choose Love, with lyrics</h2><p class="muted">The captioned version of our anthem.</p></div>
</div></section>
<section><div class="wrap"><div class="grid">{vrows}</div></div></section>
""")

# ---------------- INSPIRATION ----------------
page("inspiration.html","Inspiration | Prism Cortex Solutions",
"Choose Love, ThotBot, the UrantiaBot and guided meditations from Prism Cortex.",
f"""
<section class="hero"><div class="wrap">
<span class="eyebrow">Inspiration</span>
<h1>Make your new mantra: <span class="grad">Choose Love</span></h1>
<p class="lead">We believe in equity for all. Our purpose here is to cherish, love and experience this wonderful universe. Choose Love and you&rsquo;ll never lose.</p>
<p class="muted">All my writings, games, and designs are based in love. Thank you for your support on my creative expedition.</p>
</div></section>

<section class="alt"><div class="wrap feature">
<div>
<span class="tag">AI spiritual guide</span>
<h2>ThotBot &amp; the UrantiaBot</h2>
<p><strong>Get inspired by the part of the Creator that is inside all of us.</strong></p>
<p class="muted">I programmed ThotBot as an AI spiritual guide that creates inspirational quotes, meditations and ideas. I have practiced meditation, energy work and spiritual studies for most of my life, and I use those skills to shape the bot and tune what it says to my vision. The UrantiaBot, also called the Thought Adjuster, draws on the teachings of The Urantia Book.</p>
<div class="btns"><a class="btn primary" href="https://thoughtadjuster.vercel.app/">Talk to the Thought Adjuster</a><a class="btn" href="https://youtube.com/playlist?list=PL_RniOZRasa_hU9W5lZPMeiGmUiUVXjVZ">ThotBot videos</a></div>
</div>
<div><img src="img/choose-love.jpg" alt="Choose Love: a rainbow brain flowing into a rainbow heart" style="border-radius:var(--r)"></div>
</div></section>

<section><div class="wrap">
<span class="eyebrow">ThotBot speaks</span>
<h2>Short thoughts for a better day</h2>
<p class="muted">Under a minute each. ThotBot on the things that matter.</p>
<div class="grid shorts"><div class="card"><h3>On Creating</h3>{vid("thotbot-creating","ThotBot On Creating",True)}</div><div class="card"><h3>On Responsibility</h3>{vid("thotbot-responsibility","ThotBot On Responsibility",True)}</div><div class="card"><h3>On Joy</h3>{vid("thotbot-joy","ThotBot On Joy",True)}</div><div class="card"><h3>On Patience</h3>{vid("thotbot-patience","ThotBot On Patience",True)}</div><div class="card"><h3>On Integrity</h3>{vid("thotbot-integrity","ThotBot On Integrity",True)}</div><div class="card"><h3>On Being Generous</h3>{vid("thotbot-generous","ThotBot On Being Generous",True)}</div><div class="card"><h3>On Ethics</h3>{vid("thotbot-ethics","ThotBot On Ethics",True)}</div><div class="card"><h3>On Gratitude</h3>{vid("thotbot-gratitude","ThotBot On Gratitude",True)}</div></div>
</div></section>

<section class="alt"><div class="wrap">
<h2>Guided meditations</h2>
<div class="grid">
 <div class="card"><h3>Cosmic Meditation</h3><p>ThotBot and I created this 10-minute guided meditation to help connect to our true selves. Enjoy, and spread the love.</p>{vid("cosmic-meditation","Cosmic Meditation, 10 minutes")}</div>
 <div class="card"><h3>Choose Love</h3><p>Our anthem, with the lyrics on screen.</p><video controls playsinline preload="metadata" poster="media/choose-love-poster.jpg" style="width:100%;max-width:320px;border-radius:12px;display:block;margin:0 auto" src="media/choose-love.mp4"></video></div>
</div>
<p class="muted" style="margin-top:20px">More uplifting clips on <a href="https://www.youtube.com/n8ofbase">YouTube</a>.</p>
</div></section>
""")

# ---------------- BEHIND THE BRAIN (about N8) ----------------
page("behind-the-brain.html","Behind the Brain | Prism Cortex Solutions",
"Meet N8, the musician, game designer and builder behind Prism Cortex Solutions: Choose Love, board game songs, meditation and the inspiration behind it all.",
f"""
<section class="hero"><div class="wrap">
<span class="eyebrow">Behind the Brain</span>
<h1>Music first. <span class="grad">Love always.</span></h1>
<p class="lead">Hi, I&rsquo;m N8 (Nate Sloan). I write songs, design board games and build software in St. Louis, and all of it comes from the same place: a love of music, play and the people I get to share them with.</p>
</div></section>
<section class="banner"><div class="banner-photo"><img src="img/n8-banner.jpg" alt="N8 grinning with his N8 guitar, waving, in front of glowing Cortex nodes"></div></section>

<section><div class="wrap feature">
<div>
<span class="eyebrow">The music</span>
<h2>A guitar with my name on it</h2>
<p>Music is where the brain lights up first. I write and record my own songs, from our anthem <strong>Choose Love</strong> to <em>My New Favorite Color</em> (with POSTCARD), <em>Savior Dreams</em>, <em>The Mourning of Glory</em>, <em>Snow</em> and <em>N8&rsquo;s Blue Christmas</em>.</p>
<p>Then there are the board game songs, which combine my two favorite things, music and gaming. If a game makes me smile, it&rsquo;s probably getting a song.</p>
<div class="btns"><a class="btn primary" href="music.html">Listen on the Music Node</a><a class="btn" href="https://www.youtube.com/n8ofbase">YouTube</a></div>
</div>
<div><video controls playsinline preload="metadata" poster="media/choose-love-poster.jpg" style="width:100%;max-width:360px;border-radius:var(--r);display:block;margin:0 auto" src="media/choose-love.mp4"></video></div>
</div></section>

<section class="alt"><div class="wrap feature">
<div><img src="img/choose-love.jpg" alt="Choose Love: a rainbow brain flowing into a rainbow heart" style="border-radius:var(--r)"></div>
<div>
<span class="eyebrow">The inspiration</span>
<h2>Choose Love, and you&rsquo;ll never lose</h2>
<p>I&rsquo;ve practiced meditation, energy work and spiritual study for most of my life, and The Urantia Book shapes a lot of how I see the universe. That&rsquo;s where ThotBot and the Thought Adjuster came from, and it&rsquo;s why the Project Lightbringer stories are about love and light.</p>
<p class="muted">All my writings, games and designs are based in love. Thank you for joining me on this creative expedition.</p>
<div class="btns"><a class="btn" href="inspiration.html">Meditations &amp; ThotBot</a><a class="btn" href="lightbringer.html">Read Project Lightbringer</a></div>
</div>
</div></section>

<section><div class="wrap">
<span class="eyebrow">What I do now</span>
<h2>One brain, many nodes</h2>
<p class="lead">Prism Cortex Solutions is where it all plugs in. I design and release board games with my friends Adam Collins and Tim Forbis at <a href="https://beardedboardgames.com">Bearded Board Games</a>, make the online game <a href="{ICYN_PLAY}">I Crit You Not!</a>, and build websites and point-of-sale systems for small businesses.</p>
<p class="quote">&ldquo;Combining my 2 favorite things, music and gaming.&rdquo;</p>
<div class="btns"><a class="btn primary" href="contact.html">Say hi</a><a class="btn" href="games.html">Game Node</a></div>
</div></section>
""")

# ---------------- LIGHTBRINGER STORIES ----------------
import html as _h
def _story(fn):
    t=open(__file__.rsplit("/",1)[0]+"/stories/"+fn,encoding="utf-8").read().strip()
    return "".join(f"<p>{_h.escape(x.strip())}</p>" for x in t.split("\n") if x.strip())
page("lightbringer.html","Project Lightbringer | Prism Cortex Solutions",
"Project Lightbringer: the Prism Cortex story universe. Read the prologue, Terror on Talus, and Project Lightbringer.",
f"""
<section class="hero"><div class="wrap">
<span class="eyebrow">Stories</span>
<h1>Project <span class="grad">Lightbringer</span></h1>
<p class="lead">A story of love, light and the Universe Medallion, set on the planet Talus.</p>
<div class="btns"><a class="btn" href="#talus">Prologue: Terror on Talus</a><a class="btn" href="#lightbringer">Project Lightbringer</a><a class="btn" href="behind-the-brain.html">Back to Behind the Brain</a></div>
</div></section>
<section class="alt" id="talus"><div class="wrap story"><h2>Prologue: Terror on Talus</h2>{_story("s__stories__project-lightbringer-prologue-terror-on-talus.txt")}</div></section>
<section id="lightbringer"><div class="wrap story"><h2>Project Lightbringer</h2>{_story("s__stories__project-lightbringer.txt")}</div></section>
""")

page("404.html","Page not found | Prism Cortex Solutions","That page moved or never existed.",
"""<section class="hero"><div class="wrap"><span class="eyebrow">404</span><h1>That node <span class="grad">isn&rsquo;t connected</span></h1>
<p class="lead">The page you wanted moved when Prism Cortex became Prism Cortex Solutions. Try the home page, or meet N8 in Behind the Brain.</p>
<div class="btns"><a class="btn primary" href="/">Go home</a><a class="btn" href="/behind-the-brain.html">Behind the Brain</a></div></div></section>""")

# ---------------- CONTACT ----------------
page("contact.html","Contact | Prism Cortex Solutions",
"Start a technology or game project with Prism Cortex Solutions, or join the Prismatic Fanatic email list.",
'''
<section class="hero"><div class="wrap">
<span class="eyebrow">Contact</span>
<h1>Let's build <span class="grad">something bright</span></h1>
<p class="lead">Tell us about your app, website, point-of-sale or game idea. Or just say hi at <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
</div></section>
<section class="alt"><div class="wrap" style="max-width:640px">
<form class="card" action="mailto:{EMAIL}" method="post" enctype="text/plain">
<label>Name<br><input name="name" required style="width:100%;padding:10px;border-radius:10px;border:1px solid var(--line);background:var(--bg);color:var(--ink)"></label><br>
<label>Email<br><input type="email" name="email" required style="width:100%;padding:10px;border-radius:10px;border:1px solid var(--line);background:var(--bg);color:var(--ink)"></label><br>
<label>What can we help with?<br><textarea name="message" rows="5" style="width:100%;padding:10px;border-radius:10px;border:1px solid var(--line);background:var(--bg);color:var(--ink)"></textarea></label><br>
<label><input type="checkbox" name="list"> Make me a Prismatic Fanatic (email updates)</label><br><br>
<button class="btn primary" type="submit">Send</button>
</form>
</div></section>
''')
print("ok", sorted(p.name for p in OUT.iterdir()))

# 404 is served at any missing path, so make its relative links resolve from the site root
_f=OUT/"404.html"; _f.write_text(_f.read_text(encoding="utf-8").replace('<meta charset="utf-8">','<meta charset="utf-8"><base href="/">',1),encoding="utf-8")
