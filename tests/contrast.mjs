// WW-WEB-v1.2. No external packages or network requests.
// Run: node tests/contrast.mjs
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
const css=readFileSync(new URL('../styles.css',import.meta.url),'utf8');
const rgb=s=>s.slice(1).match(/../g).map(h=>parseInt(h,16)/255).map(n=>n<=.04045?n/12.92:((n+.055)/1.055)**2.4);
const luminance=s=>rgb(s).reduce((a,b,i)=>a+b*[.2126,.7152,.0722][i],0);
const ratio=(a,b)=>{let [l,h]=[luminance(a),luminance(b)].sort((x,y)=>x-y);return (h+.05)/(l+.05);};
const checks=[['Small gold labels on ivory','#8f601f','#faf9f7'],['Small gold labels on white','#8f601f','#ffffff'],['Gold on navy','#d4a15e','#061c29'],['Navy text on gold','#0f2a3a','#d4a15e']];
assert.match(css,/--gold-text:#8f601f/);
assert.match(css,/\.eyebrow:not\(\.eyebrow-gold\)/);
for(const [label,fg,bg] of checks){const actual=ratio(fg,bg);assert.ok(actual>=4.5,`${label}: ${actual.toFixed(2)} failed WCAG normal-text contrast`);console.log(`PASS ${label}: ${actual.toFixed(2)}:1`);}
