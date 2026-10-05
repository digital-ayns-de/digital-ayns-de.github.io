import html, os, pathlib, textwrap
BASE = "https://digital-ayns-de.github.io"
CONTACT = "info@digital-ayns.xyz"
STRIPE = {
  "sichtwerk": "https://buy.stripe.com/4gM7sMeXZ9Ev2729Zdbwk06",
  "sichtwerk_de": "https://buy.stripe.com/7sY6oIcPRg2TbHC8V9bwk05",
  "klarbetrieb": "https://buy.stripe.com/7sY9AUg23eYP6ni6N1bwk00",
  "klarangebot": "https://buy.stripe.com/4gM5kE17917ZfXS7R5bwk01",
}
CSS = """
:root{--paper:#F6F3EE;--ink:#1A1A1A;--accent:#2F5D50;--line:#C8C2B6;--muted:#5a5650}
*{box-sizing:border-box}html{font-size:17px}body{margin:0;background:var(--paper);color:var(--ink);font-family:ui-sans-serif,system-ui,-apple-system,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;line-height:1.6}
a{color:var(--accent)}.wrap{max-width:820px;margin:0 auto;padding:0 20px}
header{border-bottom:1px solid var(--line);padding:14px 0}header .wrap{display:flex;justify-content:space-between;align-items:center;gap:12px;flex-wrap:wrap}
.brand{font-weight:700;text-decoration:none;color:var(--ink);letter-spacing:.02em}nav a{margin-left:14px;text-decoration:none;color:var(--muted);font-size:.92rem}
h1{font-size:2.1rem;line-height:1.2;margin:42px 0 10px}h2{font-size:1.35rem;margin:38px 0 10px}h3{margin:22px 0 4px;font-size:1.05rem}
.lead{font-size:1.15rem;color:var(--muted)}.meta{font-size:.95rem;color:var(--muted)}
.btn{display:inline-block;background:var(--accent);color:#fff;padding:12px 22px;border-radius:6px;text-decoration:none;font-weight:600;margin:14px 10px 6px 0}
.btn.alt{background:transparent;color:var(--accent);border:1px solid var(--accent)}
.cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:16px;margin:24px 0}
.card{border:1px solid var(--line);border-radius:8px;padding:18px;background:#fbfaf7}.card h3{margin-top:0}
.price{font-weight:700}.tag{display:inline-block;font-size:.78rem;border:1px solid var(--line);border-radius:20px;padding:1px 9px;margin-right:4px;color:var(--muted)}
pre{background:#fff;border:1px solid var(--line);border-radius:6px;padding:14px;overflow-x:auto;font-size:.82rem;line-height:1.45;white-space:pre-wrap}
ul{padding-left:22px}footer{border-top:1px solid var(--line);margin-top:56px;padding:20px 0;font-size:.88rem;color:var(--muted)}
.faq dt{font-weight:600;margin-top:14px}.faq dd{margin:4px 0 0 0}
"""
def page(path, title, desc, body, canon):
    out = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)}</title><meta name="description" content="{html.escape(desc)}">
<link rel="canonical" href="{canon}"><meta property="og:type" content="website"><meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(desc)}"><meta property="og:url" content="{canon}"><meta property="og:image" content="{BASE}/og.png">
<meta name="twitter:card" content="summary_large_image"><link rel="icon" href="/favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="/style.css">
</head><body>
<header><div class="wrap"><a class="brand" href="/">DIGITAL AYNS · Packs</a><nav><a href="/sichtwerk/">Sichtwerk</a><a href="/klarangebot/">Klarangebot</a><a href="/klarbetrieb/">Klarbetrieb</a></nav></div></header>
<main class="wrap">{body}</main>
<footer><div class="wrap">Prompt &amp; workflow packs by Info DIGITAL AYNS · DIGITAL AYNS LLC · <a href="/imprint/">Imprint &amp; privacy</a> · Contact: {CONTACT}<br>Payments via Stripe. Files are delivered by email after payment (usually within 2 hours, CET daytime).</div></footer>
</body></html>
"""
    p = pathlib.Path(path); p.parent.mkdir(parents=True, exist_ok=True); p.write_text(out)

def esc(s): return html.escape(s)

# ---------- HOME ----------
home = f"""
<h1>Copy-paste operating packs for solo experts and solo founders.</h1>
<p class="lead">Structured prompt &amp; workflow packs that force ChatGPT, Claude or any current model into a real system — with fixed output formats, placeholders and checklists. One-time price. No subscription, no course, no community.</p>
<div class="cards">
<div class="card"><h3>Sichtwerk</h3><p>LinkedIn visibility pack for solo experts: positioning, profile, hooks &amp; posts, proof.</p><p><span class="price">€24 one-time</span> · <span class="tag">English</span><span class="tag">24 prompts</span></p><a href="/sichtwerk/">Details →</a></div>
<div class="card"><h3>Klarangebot</h3><p>Proposal pack: discovery, scope &amp; pricing, proposal copy, negotiation and follow-ups.</p><p><span class="price">€19 one-time</span> · <span class="tag">German</span><span class="tag">24 prompts</span></p><a href="/klarangebot/">Details →</a></div>
<div class="card"><h3>Klarbetrieb</h3><p>Week OS for solo founders: weekly rhythm, content, offers, outreach, decisions.</p><p><span class="price">€29 one-time</span> · <span class="tag">German</span><span class="tag">38 prompts</span></p><a href="/klarbetrieb/">Details →</a></div>
</div>
<h2>Which one first?</h2>
<p><strong>Sichtwerk</strong> = be seen. <strong>Klarangebot</strong> = close. <strong>Klarbetrieb</strong> = keep the business running. None is a prerequisite for another.</p>
<h2>How the packs work</h2>
<ul><li>Copy a prompt, replace the <code>[placeholders]</code> (2–5 minutes).</li><li>Paste into your model. Keep the output format — that is the point.</li><li>Cut hard, tick the checklist, ship.</li></ul>
<p>Every pack: Markdown files + PDF, delivered as a ZIP. Use for yourself and your own company. No resale or white-label.</p>
"""
page("index.html", "DIGITAL AYNS Packs — prompt & workflow packs for solo experts", "Copy-paste prompt and workflow packs for solo experts and solo founders: Sichtwerk (LinkedIn visibility), Klarangebot (proposals), Klarbetrieb (week OS). One-time price.", home, BASE + "/")

# ---------- SICHTWERK ----------
sw_sample = """You are a hook editor for LinkedIn (English, solo experts).
Position: [… ]
ICP: [… ]
Raw material (bullets from real work):
[…]

Produce 12 hooks (1–2 lines each, max. 180 characters for line 1).
Mix:
- 3 observation ("Most [ICP]…")
- 3 outcome/number
- 2 mistake/confession
- 2 unpopular opinion
- 2 question to ICP

Rules: no "5 tips that will change your life…", no "You won't believe…", no lies.
Mark Top-5 to expand.

Output format:
HOOKS 1–12:
TOP-5:"""
sw = f"""
<p class="meta">Sichtwerk · v0.1 · English</p>
<h1>Stop being good — and invisible.</h1>
<p class="lead">Sichtwerk is a LinkedIn visibility pack for solo experts and freelancers who sell B2B services. 24 copy-paste prompts in 4 modules + 3 checklists that turn real expertise into clear positioning and publishable posts — without influencer theatre or daily posting.</p>
<a class="btn" href="{STRIPE['sichtwerk']}">Buy Sichtwerk — €24 one-time</a><a class="btn alt" href="#sample">See a free sample prompt</a>
<p class="meta">Markdown + 17-page PDF · ZIP by email after payment · Deutsche Version: <a href="{STRIPE['sichtwerk_de']}">Sichtwerk DE (€24)</a></p>
<h2>The problem</h2>
<ul><li>Your LinkedIn profile reads like a CV, not an outcome.</li><li>Posts happen out of guilt — and die after two likes.</li><li>Hooks are generic, proof is missing.</li><li>Cases sit in your head and your Drive, not in 90-second posts.</li></ul>
<p>ChatGPT alone writes longer posts. Without positioning, cadence and proof logic, AI just produces more noise. Sichtwerk forces the model into a visibility system.</p>
<h2>What's inside</h2>
<h3>01 — Positioning</h3><p>ICP, one-sentence position, boundaries, topic clusters, anti-position.</p>
<h3>02 — LinkedIn system</h3><p>Headline, About, Featured, banner logic, a sustainable weekly cadence, comment system.</p>
<h3>03 — Hooks &amp; posts</h3><p>Hook bank, post formats, story → insight, series, recycling, CTAs without begging.</p>
<h3>04 — Proof &amp; case</h3><p>Before/after, mini-cases, testimonial requests, proof posts, objection killers.</p>
<h3>Bonus — 3 checklists</h3><p>Before the profile update · before a post · before publishing a case.</p>
<h2 id="sample">Free sample: Prompt 13 — Hook bank from raw material</h2>
<pre>{esc(sw_sample)}</pre>
<h2>Who it's for</h2>
<ul><li>Solo experts and freelancers with a B2B service: consulting, design, software, research, coaching, ops, specialists.</li><li>You already sell — but inquiries come irregularly or only via your network.</li><li>You want LinkedIn as a pipeline channel, not a hobby.</li></ul>
<p><strong>Not for:</strong> agencies with a content team, trades templates, mass-DM strategies.</p>
<h2>FAQ</h2><dl class="faq">
<dt>Do I need ChatGPT Plus?</dt><dd>No. Any current text model works; better models hold the formats better.</dd>
<dt>Do I have to post daily?</dt><dd>No. The pack builds a sustainable cadence (e.g. 3×/week).</dd>
<dt>How is it delivered?</dt><dd>After Stripe checkout you receive the ZIP (Markdown + PDF) by email, usually within 2 hours (CET daytime).</dd>
<dt>Refunds?</dt><dd>Digital files: generally none after delivery. If something is broken or missing, email {CONTACT} and it gets fixed.</dd>
<dt>Updates?</dt><dd>Buyers of v0.1 get v0.2 at no extra cost when it exists.</dd></dl>
<a class="btn" href="{STRIPE['sichtwerk']}">Buy Sichtwerk — €24 one-time</a>
"""
page("sichtwerk/index.html", "Sichtwerk — LinkedIn Visibility Pack for Solo Experts (€24)", "24 copy-paste prompts in 4 modules + 3 checklists for solo experts with B2B services: positioning, LinkedIn profile, hooks & posts, proof. €24 one-time, English.", sw, BASE + "/sichtwerk/")

# ---------- KLARBETRIEB ----------
kb_sample = """You are the operations lead of a one-person company.
I am [role, e.g. freelance strategist / solo SaaS founder].
My company sells [service in one sentence].
Current situation (raw, honest):
- Pipeline: [e.g. 3 open proposals, 1 active client, 0 waiting]
- Money: [cash / open invoices / revenue target next 4 weeks]
- Energy: [high / medium / thin] — reason: [one sentence]
- Calendar this week: [fixed appointments]
- Open fronts: [bullets, max. 8]

Task:
1. Write EXACTLY ONE weekly goal as one sentence describing an outcome in the world (not "work on").
2. Name 3 things that deliberately will NOT happen this week (non-goals).
3. Cut the calendar: which 2 blocks must be protected, which 2 tasks get dropped or moved?
4. Risk of the week in one sentence: where will the goal most likely fail?

Output format (do not change):
WEEKLY GOAL:
NON-GOALS:
1.
2.
3.
CALENDAR:
- Protect:
- Drop/Move:
RISK:
FIRST STEP TODAY (25 minutes, concrete):"""
kb = f"""
<p class="meta">Klarbetrieb · v0.1 · pack language: German</p>
<h1>Week OS for solo founders — run your week instead of improvising it.</h1>
<p class="lead">You are the company. No ops team, no assistant. Klarbetrieb gives you the operating rhythm most solo founders improvise: 5 modules, 38 copy-paste prompts with fixed output formats, plus 3 checklists.</p>
<a class="btn" href="{STRIPE['klarbetrieb']}">Buy Klarbetrieb — €29 one-time</a><a class="btn alt" href="#sample">See a sample prompt</a>
<p class="meta">Markdown + 27-page PDF · ZIP by email after payment · <strong>The pack itself is written in German</strong> (works with any model; outputs can be in any language).</p>
<h2>What's inside</h2>
<h3>01 — Week OS</h3><p>Monday start, midweek cut, Friday close. Pipeline, capacity, one-sentence weekly goal.</p>
<h3>02 — Content</h3><p>LinkedIn, X, newsletter — prompts that turn real work (calls, deals, mistakes) into publishable pieces, incl. recycling one idea into five formats.</p>
<h3>03 — Offers</h3><p>From first call to a solid B2B proposal: scope, non-scope, pricing logic, good/better/best, follow-up.</p>
<h3>04 — Outreach</h3><p>Research-first first contact, observation + value, soft CTAs, two follow-ups, then stop. No spray lists.</p>
<h3>05 — Decisions</h3><p>Kill / keep / park, ICE, do-it-yourself-or-not, pricing, pre-mortem, a yes-filter.</p>
<h3>Bonus — 3 checklists</h3><p>Week start in 15 minutes · proposal quality before sending · outreach ethics before clicking.</p>
<h2 id="sample">Sample: Prompt 1 — Monday start (English translation)</h2>
<pre>{esc(kb_sample)}</pre>
<h2>Who it's for</h2>
<ul><li>Solo founders and freelancers with a B2B service (consulting, design, software, research, coaching, ops).</li><li>You already use ChatGPT/Claude and want to steer it, not chat with it.</li><li>Comfortable reading German prompts (or running them through a translator once).</li></ul>
<h2>FAQ</h2><dl class="faq">
<dt>Is there an English edition?</dt><dd>Not yet. The prompts are German; the sample above is a translation. If you want the EN edition, email {CONTACT} — buyers get it free when it ships.</dd>
<dt>How is it delivered?</dt><dd>ZIP (Markdown + PDF) by email after Stripe checkout, usually within 2 hours (CET daytime).</dd>
<dt>Refunds?</dt><dd>Digital files: generally none after delivery. Broken or missing files get fixed — email {CONTACT}.</dd></dl>
<a class="btn" href="{STRIPE['klarbetrieb']}">Buy Klarbetrieb — €29 one-time</a>
"""
page("klarbetrieb/index.html", "Klarbetrieb — Week OS for Solo Founders (€29)", "Operating pack for solo founders: week OS, content, offers, outreach and decisions. 38 copy-paste prompts + 3 checklists. €29 one-time. Pack language: German.", kb, BASE + "/klarbetrieb/")

# ---------- KLARANGEBOT ----------
ka = f"""
<p class="meta">Klarangebot · v0.1 · pack language: German</p>
<h1>Proposals that decide — not explain.</h1>
<p class="lead">Klarangebot is the closing pack for one person without a sales team: 24 copy-paste prompts in 4 modules + 3 checklists for discovery, scope &amp; pricing, proposal copy and negotiation.</p>
<a class="btn" href="{STRIPE['klarangebot']}">Buy Klarangebot — €19 one-time</a>
<p class="meta">Markdown + 19-page PDF · ZIP by email after payment · <strong>The pack itself is written in German.</strong></p>
<h2>The problem</h2>
<ul><li>The call went well — and the proposal is a task list again.</li><li>The price comes from gut feeling, the justification from panic.</li><li>Scope grows silently before anything is signed.</li><li>Follow-ups sound like begging, or never happen.</li></ul>
<h2>What's inside</h2>
<h3>01 — Discovery</h3><p>Qualifying questions, fit check, gap emails, decision-maker map.</p>
<h3>02 — Scope &amp; price</h3><p>Non-scope, assumptions, pricing logic without theatre, good/better/best, capacity cut.</p>
<h3>03 — Proposal copy</h3><p>One-page core, subject line, assumptions clause, sharpening pass, "done looks like this".</p>
<h3>04 — Negotiation</h3><p>Objections, discount traps, day-3/day-8 follow-ups, internal champion, a dignified no-exit.</p>
<h3>Bonus — 3 checklists</h3><p>Before the qualifying call · before sending · before the follow-up.</p>
<h2>FAQ</h2><dl class="faq">
<dt>How is it delivered?</dt><dd>ZIP (Markdown + PDF) by email after Stripe checkout, usually within 2 hours (CET daytime).</dd>
<dt>Refunds?</dt><dd>Digital files: generally none after delivery. Broken or missing files get fixed — email {CONTACT}.</dd></dl>
<a class="btn" href="{STRIPE['klarangebot']}">Buy Klarangebot — €19 one-time</a>
"""
page("klarangebot/index.html", "Klarangebot — Proposal Pack for Solo Founders (€19)", "Proposal pack for solo founders: discovery, scope & pricing, proposal copy, negotiation. 24 copy-paste prompts + 3 checklists. €19 one-time. Pack language: German.", ka, BASE + "/klarangebot/")

# ---------- IMPRINT ----------
imp = f"""
<h1>Imprint &amp; privacy</h1>
<p>These packs (Sichtwerk, Klarangebot, Klarbetrieb) are published by:</p>
<p><strong>DIGITAL AYNS LLC</strong><br>1603 Capitol Ave Suite 413G-1351<br>Cheyenne, Wyoming 82001<br>United States<br>Contact: {CONTACT}</p>
<h2>Privacy</h2>
<p>This site is a static page hosted on GitHub Pages. It sets no cookies and uses no analytics or tracking scripts. GitHub may process technical access data (e.g. IP address) to deliver the site — see GitHub's privacy statement.</p>
<p>Payments are processed by Stripe on Stripe-hosted checkout pages. We receive your name, email and payment status from Stripe solely to deliver your purchase and keep legally required records.</p>
<h2>Terms in short</h2>
<p>Digital products, one-time price, licensed for use by you and your own company. No resale or white-label. Delivery by email after payment.</p>
"""
page("imprint/index.html", "Imprint & privacy — DIGITAL AYNS Packs", "Imprint and privacy notice for DIGITAL AYNS prompt & workflow packs.", imp, BASE + "/imprint/")

pathlib.Path("style.css").write_text(CSS.strip()+"\n")
pathlib.Path(".nojekyll").write_text("")
pathlib.Path("favicon.svg").write_text('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="12" fill="#2F5D50"/><text x="32" y="44" font-family="Arial,Helvetica,sans-serif" font-size="34" font-weight="700" fill="#F6F3EE" text-anchor="middle">DA</text></svg>\n')
pathlib.Path("robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {BASE}/sitemap.xml\n")
urls = ["/", "/sichtwerk/", "/klarangebot/", "/klarbetrieb/", "/imprint/"]
pathlib.Path("sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(f"<url><loc>{BASE}{u}</loc><lastmod>2026-10-05</lastmod></url>\n" for u in urls) + "</urlset>\n")
pathlib.Path("README.md").write_text("# DIGITAL AYNS Packs\n\nStatic product site (GitHub Pages) for Sichtwerk, Klarangebot, Klarbetrieb. Generated by build.py. Publisher: DIGITAL AYNS LLC.\n")
print("ok")
