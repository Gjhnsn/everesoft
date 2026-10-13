#!/usr/bin/env python3
"""Generates the static EvereSoft site (shared header/footer). Run: python3 build.py"""
EMAIL = "everesofttech@gmail.com"
NAV = [("index.html", "Home"), ("tabtape.html", "TabTape"), ("contact.html", "Contact")]

def page(fname, title, desc, body):
    nav = "".join(f'<li><a href="{h}"{" aria-current=\"page\"" if h == fname else ""}>{t}</a></li>' for h, t in NAV)
    html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="icon" href="assets/img/everesoft-mark.svg" type="image/svg+xml">
<link rel="icon" href="assets/img/favicon-32.png" sizes="32x32" type="image/png">
<link rel="apple-touch-icon" href="assets/img/apple-touch-icon.png">
<link rel="stylesheet" href="assets/style.css">
</head>
<body>
<header class="site-header"><div class="wrap">
<a class="brand" href="index.html"><img src="assets/img/everesoft-mark.svg" alt="" width="32" height="32">EvereSoft</a>
<nav aria-label="Main"><ul>{nav}</ul></nav>
</div></header>
<main>
{body}
</main>
<footer class="site-footer"><div class="wrap">
<div>© 2026 EvereSoft · Madera, California, USA · <a href="mailto:{EMAIL}">{EMAIL}</a></div>
<nav aria-label="Legal"><ul><li><a href="privacy.html">Privacy</a></li><li><a href="terms.html">Terms</a></li><li><a href="refunds.html">Refunds</a></li><li><a href="contact.html">Contact</a></li></ul></nav>
</div></footer>
</body>
</html>
"""
    open(fname, "w").write(html)

# ---------- Home ----------
page("index.html", "EvereSoft — Privacy-first browser tools",
     "EvereSoft builds privacy-first browser extensions. Software that runs on your device, without tracking.",
f"""<div class="hero"><div class="wrap">
<h1>Privacy-first browser tools.</h1>
<p>EvereSoft makes small, focused browser extensions that do their work on your device. No tracking, no accounts unless you need one, and nothing uploaded that doesn't have to be.</p>
<div class="btns"><a class="btn" href="tabtape.html">See TabTape</a><a class="btn alt" href="contact.html">Contact us</a></div>
</div></div>
<section><div class="wrap">
<h2>Products</h2>
<div class="grid">
<article class="card"><div class="top"><img src="assets/img/tabtape-128.png" alt="TabTape icon" width="56" height="56"><div><h3>TabTape <span class="badge soon">Coming soon</span></h3><div class="muted small">Chrome extension</div></div></div>
<p>Record any tab's audio in one click and transcribe it privately on your device. Export MP3 or WebM. Free plan, with an optional Pro subscription.</p>
<a href="tabtape.html">Learn more and see pricing →</a></article>
<article class="card"><div class="top"><img src="assets/img/everesoft-mark.svg" alt="" width="56" height="56"><div><h3>Reject Cookies <span class="badge soon">Coming soon</span></h3><div class="muted small">Chrome extension · Free</div></div></div>
<p>Automatically clicks "reject" on cookie consent banners, and never accepts. Runs entirely in your browser, built on open-source consent rules.</p>
<span class="muted small">Free. Launching after TabTape.</span></article>
</div></div></section>
<section><div class="wrap">
<h2>How we build software</h2>
<div class="values">
<div><h3>On-device first</h3><p class="muted">Processing happens in your browser whenever possible.</p></div>
<div><h3>No tracking</h3><p class="muted">No analytics or ad trackers in our products or on this site.</p></div>
<div><h3>Honest pricing</h3><p class="muted">Useful free plans. Paid upgrades are optional and you can cancel anytime.</p></div>
</div></div></section>
""")

# ---------- TabTape ----------
shots = [("1-record", "Record a tab's audio in one click, and keep hearing it"),
         ("2-library", "All your recordings in one library, with timestamped transcripts"),
         ("3-search", "Pro: search inside all your transcripts"),
         ("4-export", "Pro: trim, then export SRT, VTT or DOCX"),
         ("5-private", "Transcribed on your device, nothing uploaded")]
figs = "".join(f'<figure><a href="assets/img/{s}.webp"><img src="assets/img/{s}-640.webp" srcset="assets/img/{s}-640.webp 640w, assets/img/{s}.webp 1280w" sizes="(max-width: 700px) 100vw, 520px" width="640" height="400" loading="lazy" alt="{c}"></a><figcaption>{c}</figcaption></figure>' for s, c in shots)
page("tabtape.html", "TabTape — Record tab audio & transcribe privately | EvereSoft",
     "TabTape by EvereSoft: record any tab's audio and transcribe it on your device. Free plan; Pro $4/month or $29/year.",
f"""<div class="hero"><div class="wrap">
<div class="top" style="display:flex;gap:16px;align-items:center;margin-bottom:12px"><img src="assets/img/tabtape-128.png" alt="TabTape icon" width="72" height="72"><span class="badge">Chrome extension by EvereSoft</span></div>
<h1>TabTape: record tab audio and transcribe it privately</h1>
<p>TabTape records the audio of any browser tab in one click and turns it into text on your computer. Use it for online lectures, webinars, podcasts, interviews and meetings that run in the browser.</p>
<div class="btns"><a class="btn" aria-disabled="true" role="link" title="Not published yet">Chrome Web Store: coming soon</a><a class="btn alt" href="#pricing">Pricing</a></div>
</div></div>
<section><div class="wrap"><div class="grid">
<div class="card"><h3>Record</h3><ul><li>One click records the current tab's audio. You keep hearing the tab while it records.</li><li>Optionally mix in your microphone.</li><li>Crash-safe: audio is saved to your device every second.</li><li>Keyboard shortcut: Alt+Shift+R.</li></ul></div>
<div class="card"><h3>Organize and export</h3><ul><li>A clean library: play, rename, delete.</li><li>Export to WebM or MP3.</li><li>Click any transcript line to jump to that moment.</li></ul></div>
<div class="card"><h3>Private transcripts</h3><ul><li>Speech-to-text runs on your device using the open-source Whisper speech model.</li><li>Your audio and transcripts are never uploaded. No account needed.</li><li>The speech model (about 40–120 MB) downloads once, then works offline.</li></ul></div>
</div></div></section>
<section id="pricing" style="background:var(--bg2)"><div class="wrap">
<h2>Pricing</h2>
<div class="grid">
<div class="card"><h3>Free</h3><div class="price">$0</div>
<ul><li>Unlimited recording</li><li>Microphone mix</li><li>Library and playback</li><li>WebM and MP3 export</li><li>Transcripts of the first 10 minutes of each recording</li><li>TXT transcript export</li></ul></div>
<div class="card"><h3>Pro <span class="badge pro">Optional</span></h3><div class="price">$4 <small>USD / month</small></div><div class="muted">or $29 USD / year</div>
<ul><li>Everything in Free</li><li>Transcripts of any length</li><li>Subtitle export (SRT, VTT)</li><li>Word (DOCX) export</li><li>Search inside all your transcripts</li><li>Trimming</li></ul></div>
</div>
<p class="small muted" style="margin-top:16px">Payments are processed by <a href="https://extensionpay.com" rel="noopener">ExtensionPay</a> using <a href="https://stripe.com" rel="noopener">Stripe</a>. Prices are in US dollars. Subscriptions renew automatically until you cancel, and you can cancel anytime. See our <a href="terms.html">Terms</a> and <a href="refunds.html">Refund &amp; Cancellation Policy</a>.</p>
</div></section>
<section><div class="wrap"><h2>Screenshots</h2><div class="shots">{figs}</div></div></section>
<section><div class="wrap prose"><h2>Good to know</h2><ul>
<li>Chrome doesn't let extensions record its own pages (chrome:// pages and the Chrome Web Store).</li>
<li>Some streaming sites use copy-protected (DRM) audio, which can't be recorded. TabTape tells you when that happens and doesn't try to get around it.</li>
<li>Transcription accuracy depends on audio quality. Please review important transcripts.</li>
<li>Only record content you have the right to record, and follow your local laws on recording conversations.</li></ul>
<p>Read the <a href="privacy.html">TabTape privacy policy</a>.</p></div></section>
""")

# ---------- Contact ----------
page("contact.html", "Contact — EvereSoft", "Contact EvereSoft, Madera, California, USA.",
f"""<div class="hero"><div class="wrap"><h1>Contact EvereSoft</h1><p>Questions, support, billing or refund requests: email us and we'll usually reply within 2 business days.</p></div></div>
<section><div class="wrap"><div class="grid">
<div class="card"><h3>Email</h3><p><a href="mailto:{EMAIL}">{EMAIL}</a></p><p class="muted small">For subscription and refund requests, please include the email address you used at checkout.</p></div>
<div class="card"><h3>Business</h3><p>EvereSoft<br>Madera, California, USA</p></div>
</div></div></section>
""")

# ---------- Privacy ----------
page("privacy.html", "Privacy Policy — EvereSoft", "Privacy policy for the EvereSoft website and the TabTape extension.",
f"""<section><div class="wrap prose">
<h1>Privacy Policy</h1>
<p class="muted">Last updated: October 13, 2026</p>
<p>This page explains how EvereSoft ("we") handles information on this website and in the TabTape browser extension.</p>
<h2>This website</h2>
<p class="note">This website uses no cookies, analytics, tracking pixels or third-party scripts. We don't collect personal information when you browse it. If you email us, we use your message and email address only to reply and to provide support.</p>
<p>Our hosting provider may keep standard server logs (such as IP address and pages requested) for security and operations.</p>
<h2>TabTape</h2>
<p><strong>Short version: your recordings and transcripts stay on your computer. We don't collect, upload or sell them.</strong></p>
<h3>What is stored, and where</h3>
<ul><li><strong>Audio recordings</strong> you make, with their names, dates, durations and <strong>transcripts</strong>, are stored only in your browser (IndexedDB inside the extension). They are never sent to us or to any third party. Deleting a recording or uninstalling the extension removes them.</li>
<li><strong>Settings</strong> (microphone preference, chosen speech model) are stored in the extension's local storage.</li></ul>
<h3>Microphone</h3>
<p>The microphone is used only if you turn on "Also record my microphone", and only while you are recording. Microphone audio is mixed into the local recording and is not sent anywhere.</p>
<h3>Transcription</h3>
<p>Speech-to-text runs entirely on your device (Whisper model via transformers.js and ONNX Runtime). The first time you transcribe, the extension downloads the model files (about 40–200 MB) from huggingface.co. That download is a normal file request and contains no audio, text or personal data. Hugging Face may log standard request data (such as IP address) under its own privacy policy. After that, the model is cached and transcription works offline.</p>
<h3>Payments (Pro only)</h3>
<p>Purchases are processed by ExtensionPay (extensionpay.com) and Stripe. They handle your email address and payment details under their own privacy policies. The extension only asks ExtensionPay whether your license is active. We never see your full card details or your recordings.</p>
<h3>Analytics</h3><p>None. No tracking, no telemetry.</p>
<h3>Your responsibility</h3><p>Only record content you have the right to record, and follow the law where you live about recording conversations (some places require everyone's consent). TabTape does not get around copy protection (DRM).</p>
<h2>Children</h2><p>Our products are not directed at children under 13.</p>
<h2>Your choices and requests</h2><p>For questions or a privacy request (for example under the California Consumer Privacy Act), email <a href="mailto:{EMAIL}">{EMAIL}</a>. We don't sell or share personal information.</p>
<h2>Changes</h2><p>If we change this policy, we'll post the update here with a new date.</p>
<h2>Contact</h2><p>EvereSoft, Madera, California, USA · <a href="mailto:{EMAIL}">{EMAIL}</a></p>
</div></section>
""")

# ---------- Terms ----------
page("terms.html", "Terms of Service — EvereSoft", "Terms of Service for EvereSoft software and subscriptions.",
f"""<section><div class="wrap prose">
<h1>Terms of Service</h1>
<p class="muted">Last updated: October 13, 2026</p>
<p>These terms apply when you use software from EvereSoft, based in Madera, California, USA ("EvereSoft", "we", "us"). That includes TabTape, Reject Cookies, and any paid plans ("Pro"). By installing or using our software, you agree to these terms.</p>
<h2>1. License</h2><p>We grant you a personal, non-exclusive, non-transferable license to use our software for lawful purposes. You may not resell it, reverse engineer it beyond what the law allows, or remove notices. Open-source components are covered by their own licenses, which are included with the software.</p>
<h2>2. Free and paid plans</h2><p>Some features are free. Pro features need a paid subscription. Current prices are on each product page and are in US dollars. Taxes may apply depending on where you live.</p>
<h2>3. Billing and renewal</h2><p>Subscriptions are billed in advance, monthly or yearly, through our payment providers ExtensionPay and Stripe. They <strong>renew automatically</strong> at the then-current price until you cancel. If we change a price, we'll give you notice before it applies to your next renewal.</p>
<h2>4. Cancellation</h2><p>You can cancel anytime from the extension's payment/account page (provided by ExtensionPay), or by emailing <a href="mailto:{EMAIL}">{EMAIL}</a>. When you cancel, the next renewal is stopped and Pro stays active until the end of the period you've already paid for. See the <a href="refunds.html">Refund &amp; Cancellation Policy</a>.</p>
<h2>5. Acceptable use</h2><p>You are responsible for how you use the software. In particular, only record or process content you have the right to, and follow laws on recording consent, copyright and privacy. Don't use our software to get around copy protection (DRM) or to break the law.</p>
<h2>6. Your content</h2><p>Recordings, transcripts and settings you create stay on your device and belong to you. We don't get any rights to them.</p>
<h2>7. Updates and availability</h2><p>We may update, change or discontinue features. If we discontinue a paid product, we'll give reasonable notice and a prorated refund for any prepaid, unused time.</p>
<h2>8. Disclaimer</h2><p>The software is provided "as is" and "as available". To the fullest extent the law allows, we disclaim warranties of merchantability, fitness for a particular purpose and non-infringement. Transcriptions may contain errors, and you should review important output. Keep your own backups of important recordings.</p>
<h2>9. Limitation of liability</h2><p>To the fullest extent the law allows, EvereSoft is not liable for indirect, incidental, special or consequential damages, or for lost data or profits. Our total liability for any claim is limited to the amount you paid us in the 12 months before the claim.</p>
<h2>10. Termination</h2><p>You may stop using the software at any time. We may suspend a license that is used in serious violation of these terms.</p>
<h2>11. Governing law</h2><p>These terms are governed by the laws of the State of California, USA, without regard to its conflict-of-law rules. Disputes will be handled in the state or federal courts located in Madera County, California, unless the law where you live requires otherwise.</p>
<h2>12. Changes</h2><p>We may update these terms and will post the new version here with a new date. Continuing to use the software after a change means you accept the updated terms.</p>
<h2>13. Contact</h2><p>EvereSoft, Madera, California, USA · <a href="mailto:{EMAIL}">{EMAIL}</a></p>
</div></section>
""")

# ---------- Refunds ----------
page("refunds.html", "Refund & Cancellation Policy — EvereSoft", "Refund and cancellation policy for EvereSoft subscriptions.",
f"""<section><div class="wrap prose">
<h1>Refund &amp; Cancellation Policy</h1>
<p class="muted">Last updated: October 13, 2026</p>
<h2>Cancel anytime</h2><p>You can cancel a Pro subscription at any time:</p>
<ul><li>open the extension's Settings → Pro → manage subscription (handled by ExtensionPay and Stripe), or</li><li>email <a href="mailto:{EMAIL}">{EMAIL}</a> with the email address you used at checkout.</li></ul>
<p>Cancelling stops future renewals. Pro stays active until the end of the billing period you've already paid for. We don't charge cancellation fees.</p>
<h2>Refunds</h2>
<ul><li><strong>14-day refund window:</strong> if you're not happy, email us within 14 days of a charge (the first purchase or a renewal) and we'll refund that charge in full.</li>
<li>After 14 days, payments are generally non-refundable. We'll still look at problems we caused, such as duplicate charges or a feature that doesn't work as described, case by case.</li>
<li>Refunds go back to the original payment method through Stripe. They usually appear within 5–10 business days, depending on your bank.</li>
<li>When a charge is refunded, Pro access for that period may end.</li></ul>
<h2>How to request a refund</h2><p>Email <a href="mailto:{EMAIL}">{EMAIL}</a> with your checkout email address, the date of the charge and (optionally) the reason. We usually reply within 2 business days.</p>
<h2>Free plan</h2><p>The free plan costs nothing and needs no cancellation. Just uninstall the extension.</p>
<h2>Contact</h2><p>EvereSoft, Madera, California, USA · <a href="mailto:{EMAIL}">{EMAIL}</a></p>
</div></section>
""")

# ---------- 404 ----------
page("404.html", "Page not found — EvereSoft", "Page not found.",
"""<div class="hero"><div class="wrap"><h1>Page not found</h1><p>That page doesn't exist. <a href="index.html">Go to the EvereSoft home page</a>.</p></div></div>""")
print("built")
