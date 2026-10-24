#!/usr/bin/env python3
"""Warley Works: local Chromium QA of an actual GitHub branch checkout."""
from pathlib import Path
import json
from playwright.sync_api import sync_playwright

root = Path(__file__).resolve().parents[1]
out = root / "qa-artifacts"
out.mkdir(exist_ok=True)
results = []
with sync_playwright() as pw:
    browser = pw.chromium.launch(headless=True)
    for width, height in [(1440,900),(1024,768),(768,1024),(375,812),(320,720)]:
        page = browser.new_page(viewport={"width":width,"height":height},reduced_motion="reduce")
        errors, failures, writes = [], [], []
        page.on("pageerror",lambda e:errors.append(str(e)))
        page.on("requestfailed",lambda r:failures.append(r.url))
        page.on("request",lambda r:writes.append(r.url) if r.method not in ("GET","HEAD") else None)
        page.goto((root/"index.html").as_uri(),wait_until="load",timeout=30000)
        page.screenshot(path=str(out/f"canonical-{width}.png"),full_page=True,animations="disabled")
        checks=page.evaluate("""() => ({
          noOverflow:document.documentElement.scrollWidth<=innerWidth+1,
          heroAndServices:!!document.querySelector('h1')&&!!document.querySelector('#services'),
          logoLoaded:[...document.images].some(i=>i.getAttribute('src')==='assets/logo-horizontal.svg'&&i.naturalWidth>0),
          labels:[...document.querySelectorAll('input,select,textarea')].every(i=>i.labels&&i.labels.length>0),
          anchors:[...document.querySelectorAll('a[href^="#"]')].every(a=>a.hash.length<2||!!document.getElementById(a.hash.slice(1)))
        })""")
        menu=None
        if width<=860:
            button=page.locator(".nav-toggle")
            button.click()
            opened=button.get_attribute("aria-expanded")=="true" and page.locator("#main-nav").is_visible()
            page.keyboard.press("Escape")
            menu=opened and button.get_attribute("aria-expanded")=="false"
        form=None
        if width in (1440,375):
            f=page.locator("#estimate-form")
            f.locator('button[type="submit"]').click()
            invalid="Please complete" in page.locator("#form-message").inner_text()
            for name,value in [("name","QA Example"),("email","example@example.invalid"),("phone","3125550100"),("zip","60628"),("details","Fictional demo inquiry")]:
                f.locator('[name="'+name+'"]').fill(value)
            f.locator('[name="service"]').select_option(label="Interior painting")
            f.locator('button[type="submit"]').click()
            valid="No information was sent or stored" in page.locator("#form-message").inner_text()
            form=invalid and valid
        results.append({"width":width,"checks":checks,"menu":menu,"form":form,"errors":errors,"failed_resources":failures,"write_requests":writes})
        page.close()
    browser.close()
(out/"results.json").write_text(json.dumps(results,indent=2),encoding="utf-8")
fail=[r for r in results if not all(r["checks"].values()) or r["errors"] or r["write_requests"] or r["menu"] is False or r["form"] is False]
for r in results: print(r["width"],r["checks"],"menu",r["menu"],"form",r["form"],"failed resources",len(r["failed_resources"]))
if fail: raise SystemExit(f"{len(fail)} viewport(s) failed; see qa-artifacts/results.json")
print("PASS: local browser checks. Manual Founder screenshot fidelity review remains required.")
