#!/usr/bin/env python3
"""WW-WEB-v1.3D — Browser QA fallback using actual checkout bytes in memory.

Run in a checked-out Warley Works feature branch:
    python3 tests/inline_browser_qa.py

This is an IN-MEMORY, source-derived rendering test. It is NOT equivalent to an
HTTP/production browser test, does not publish files, and does not send leads.
Photographs remain external and cannot be certified by these screenshots.
"""
from __future__ import annotations
import base64, hashlib, json, re
from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "qa-artifacts" / "in-memory"
OUT.mkdir(parents=True, exist_ok=True)
FILES = ["index.html", "styles.css", "script.js",
         "assets/logo-horizontal.svg", "assets/mark.svg", "assets/social-card.svg"]
source = {name: (ROOT / name).read_bytes() for name in FILES}
hashes = {name: hashlib.sha256(data).hexdigest() for name, data in source.items()}

html = source["index.html"].decode("utf-8")
css = source["styles.css"].decode("utf-8")
js = source["script.js"].decode("utf-8")

if html.count('<link rel="stylesheet" href="styles.css">') != 1:
    raise SystemExit("Unknown stylesheet reference: refusing unverified reconstruction")
if html.count('<script src="script.js" defer></script>') != 1:
    raise SystemExit("Unknown script reference: refusing unverified reconstruction")
if html.count("</body>") != 1:
    raise SystemExit("Ambiguous document boundary")

# Change only local file references because restricted browsers cannot navigate
# file:// or localhost. Preserve all original CSS rules and application JS.
html = html.replace('<link rel="stylesheet" href="styles.css">',
                    '<style id="qa-exact-styles">' + css + "</style>")
html = html.replace('<script src="script.js" defer></script>', "")
for name in FILES[3:]:
    data_uri = "data:image/svg+xml;base64," + base64.b64encode(source[name]).decode("ascii")
    html = html.replace(name, data_uri)
html = html.replace("</body>", '<script id="qa-exact-script">' + js + "</script></body>")

screens = [(1440,900),(1024,768),(768,1024),(375,812),(320,720)]
runs, failures = [], []
with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    for width,height in screens:
        page = browser.new_page(viewport={"width":width,"height":height},
                                reduced_motion="reduce", device_scale_factor=1)
        errors, requests = [], []
        page.on("pageerror", lambda err: errors.append(str(err)))
        page.on("requestfailed", lambda req: requests.append(req.url))
        page.set_content(html, wait_until="domcontentloaded", timeout=20000)
        page.screenshot(path=str(OUT / f"warley-{width}.png"), full_page=True, animations="disabled")
        checks = page.evaluate("""() => ({
          noOverflow:document.documentElement.scrollWidth <= innerWidth+1,
          logoLoaded:[...document.images].some(i=>i.getAttribute('src').startsWith('data:image/svg+xml;base64,') && i.naturalWidth>0),
          heroPresent:!!document.querySelector('h1'),
          noOrphanAnchors:[...document.querySelectorAll('a[href^="#"]')].every(a=>a.hash.length<=1||!!document.getElementById(a.hash.slice(1))),
          formLabels:[...document.querySelectorAll('input,select,textarea')].every(i=>i.labels.length>0)
        })""")
        menu=None
        if width<=860:
            btn=page.locator(".nav-toggle")
            btn.click()
            opened=btn.get_attribute("aria-expanded")=="true" and page.locator("#main-nav").is_visible()
            page.keyboard.press("Escape")
            menu=opened and btn.get_attribute("aria-expanded")=="false"
        form=None
        if width in (1440,375):
            f=page.locator("#estimate-form")
            f.locator('button[type="submit"]').click()
            invalid="Please complete" in page.locator("#form-message").inner_text()
            for name,value in [("name","Fictional QA"),("email","example@example.invalid"),
                               ("phone","3125550100"),("zip","60628"),
                               ("details","Fictional painting QA only")]:
                f.locator('[name="'+name+'"]').fill(value)
            f.locator('[name="service"]').select_option(label="Interior painting")
            f.locator('button[type="submit"]').click()
            valid="No information was sent or stored" in page.locator("#form-message").inner_text()
            form=invalid and valid
        record={"viewport":width,"checks":checks,"menu":menu,"demoForm":form,
                "scriptErrors":errors,"failedExternalRequests":requests}
        runs.append(record)
        if not all(checks.values()) or menu is False or form is False or errors:
            failures.append(record)
        page.close()
    browser.close()

report={"testClass":"in-memory rendering of exact checkout HTML/CSS/JS and SVG bytes",
        "notVerified":["HTTP deployment behavior","remote photo licensing","full accessibility",
                       "founder visual approval","business activation"],
        "sourceSHA256":hashes,"runs":runs,"failures":failures}
(OUT/"report.json").write_text(json.dumps(report,indent=2),encoding="utf-8")
print("Warley source-derived in-memory browser QA:",len(screens),"viewports;",len(failures),"failures")
for r in runs:
    print(r["viewport"],r["checks"],"menu",r["menu"],"form",r["demoForm"],
          "remote failures",len(r["failedExternalRequests"]))
if failures: raise SystemExit(1)
