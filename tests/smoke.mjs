// Warley Works v1.1 - dependency-free static build guardrails.
// Run: node tests/smoke.mjs (Node 20+). Does not replace actual browser QA.
import assert from 'node:assert/strict';
import fs from 'node:fs';
const read = name => fs.readFileSync(new URL('../'+name, import.meta.url),'utf8');
const html=read('index.html'),css=read('styles.css'),js=read('script.js');
const mark=read('assets/mark.svg'),logo=read('assets/logo-horizontal.svg');
const checks=[
['approved source logo in header/footer',() => assert.equal((html.match(/src="assets\/logo-horizontal\.svg"/g)||[]).length,2)],
['logo assets are SVG with vector paths',() => {assert.match(mark,/<path/);assert.match(logo,/<path/);}],
['responsive breakpoints',() => {for(const bp of [860,640,360])assert.ok(css.includes('max-width:'+bp+'px'),bp);}],
['menu accessibility',() => {assert.match(html,/aria-expanded="false"/);assert.match(js,/Escape/);}],
['demo form prevents submission',() => {assert.match(html,/id="estimate-form"/);assert.match(js,/event\.preventDefault\(\)/);assert.doesNotMatch(js,/fetch\(|sendBeacon|XMLHttpRequest|localStorage|sessionStorage/);}],
['no invented proof',() => assert.doesNotMatch(html,/Licensed & Insured|5-Star Rated|Michael R\.|excellent customer review/i)],
['prelaunch notice and genuine portfolio boundary',() => {assert.match(html,/bookings are not open yet/i);assert.match(html,/No sample images are presented as completed customer jobs/);}],
['robots prelaunch disallow',() => assert.match(read('robots.txt'),/Disallow:\s*\//)],
['no fragile external JS dependencies',() => assert.doesNotMatch(html,/<script[^>]*src="https?:/)]
];
let failed=0;
for(const [name,fn] of checks){try{fn();console.log('PASS',name)}catch(e){failed++;console.error('FAIL',name, e.message)}}
console.log(`${checks.length-failed}/${checks.length} static checks passed`);
if(failed)process.exitCode=1;
