import os, html, json
exec(open('logos.py').read())
a=json.load(open('aspects.json'))
alone_svg={"upcloud","nginx","valkey","splunk","cpanel","plesk","php","aws","kinsta","vmware"}
kinds={}
def has(k,n): return os.path.exists(f'{k}/{n}.svg') and os.path.getsize(f'{k}/{n}.svg')>0
def cell(n):
    disp=html.escape(L[n][0])
    if has('wm',n) and a.get('wm-'+n,0)>=2.3:
        kinds[n]='wordmark'; return f'<div class="c"><img class="wm" src="wm/{n}.svg"></div>'
    if n in alone_svg and has('svg',n):
        kinds[n]='wordmark'; return f'<div class="c"><img class="wm" src="svg/{n}.svg"></div>'
    kinds[n]='named'
    if has('svg',n): return f'<div class="c"><img class="g" src="svg/{n}.svg"><span>{disp}</span></div>'
    return f'<div class="c"><span>{disp}</span></div>'
css='''body{margin:0;font-family:Inter}.c{width:1100px;height:150px;display:flex;align-items:center;gap:20px;padding-left:20px;box-sizing:border-box}
.wm{height:84px;width:auto;max-width:560px;object-fit:contain}.g{height:72px;width:auto;max-width:110px;object-fit:contain}
span{font-size:56px;font-weight:500;color:#2E1B34;white-space:nowrap}'''
names=list(L)
for v,f in (("color",""),("dim","filter:grayscale(1);opacity:.22"),("half","opacity:.5")):
    open(f'wall-{v}.html','w').write(f'<!doctype html><style>{css} .c{{{f}}}</style>'+"".join(cell(n) for n in names))
open('names2.txt','w').write("\n".join(names))

json.dump(kinds,open('kinds.json','w'))
