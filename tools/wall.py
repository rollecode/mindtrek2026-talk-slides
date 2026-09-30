import json, random, newsection as n, os, math
exec(open('logos.py').read())
sizes=json.load(open('sizes.json')); kinds=json.load(open('kinds.json'))
# The approved order was picked with the text-only Skynet; keep it.
LAYOUT=dict(sizes, skynet=[182.0, 54.0])
LEFT,RIGHT,TOP,BOTTOM=104,1812,104,904
best=None
for ROWS,AREA,HMAX,SN in ((12,3600,36,0.40),(12,3900,38,0.42),(11,4200,40,0.44)):
  def dims(nm, AREA=AREA, HMAX=HMAX, SN=SN):
      w,h=LAYOUT[nm]
      s=SN if kinds[nm]=='named' else min(HMAX/h, math.sqrt(AREA/(w*h)), 240/w)
      return round(w*s), round(h*s)
  for seed in range(300):
    names=list(L); random.Random(seed).shuffle(names); d={nm:dims(nm) for nm in names}
    target=sum(d[x][0] for x in names)/ROWS; rows=[[]]; acc=0
    for nm in names:
        if acc>=target*len(rows) and len(rows)<ROWS: rows.append([])
        rows[-1].append(nm); acc+=d[nm][0]
    if len(rows)<ROWS: continue
    gaps=[(RIGHT-LEFT-sum(d[x][0] for x in r))/(len(r)-1) for r in rows]
    if not all(any(L[x][1]!='dim' for x in r) for r in rows) or min(gaps)<30: continue
    sc=min(gaps)-0.3*(max(gaps)-min(gaps))
    if best is None or sc>best[0]: best=(sc,rows,d,SN)
sc,rows,d,_=best
for nm in d:
    w,h=sizes[nm]; s_=best[3] if kinds[nm]=='named' else d[nm][0]/LAYOUT[nm][0]; d[nm]=(round(w*s_),round(h*s_))
Hrow=max(h for (w,h) in d.values()); step=(BOTTOM-TOP-Hrow)/(len(rows)-1); A=os.path.abspath('../keyassets/logos'); D=n.q(n.DOC)
def build(slide, state):
    lines=[]
    for r,row in enumerate(rows):
        gap=(RIGHT-LEFT-sum(d[x][0] for x in row))/(len(row)-1); x=LEFT; cy=TOP+r*step+Hrow/2
        for nm in row:
            w,h=d[nm]
            lines.append(f'make new image with properties {{file:(POSIX file {n.q(A+"/"+nm+"-"+state(nm)+".png")}), position:{{{round(x)}, {round(cy-h/2)}}}, width:{w}, height:{h}}}')
            x+=w+gap
    n.osa(f'''tell application "Keynote" to tell slide {slide} of document {D}
  repeat with i from (count of images) to 1 by -1
    set fn to file name of image i
    if fn does not start with "prog" and fn does not start with "bg" then delete image i
  end repeat
'''+"\n".join(lines)+'\nend tell')
assert n.dump(8)[0]["text"]=="I want to see" and n.dump(6)[0]["text"]=="Sovereign by habit"
build(6, lambda nm: "color"); build(7, lambda nm: {"lit":"color","half":"half","dim":"dim"}[L[nm][1]])
n.osa(f'tell application "Keynote" to save document {D}'); print('placed', [len(r) for r in rows])
