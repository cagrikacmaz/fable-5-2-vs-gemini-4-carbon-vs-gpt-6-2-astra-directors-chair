import re,json,sys
RND=sys.argv[1] if len(sys.argv)>1 else '1'
def num(s):
    m=re.search(r'\d[\d,]*',s or ''); return int(m.group(0).replace(',','')) if m else None
def fable():
    t=open('t-a/ORDERS-%s.md'%RND,encoding='utf-8').read()
    out={'video':[],'sound':[],'music':[]}
    for m in re.finditer(r'^### (\d+)\. (Video|Sound effect|Voiceover|Music attempt): `(.+?)`\n(.*?)(?=^### |^## |\Z)',t,re.S|re.M):
        n,kind,label,body=m.groups(); f={}
        for line in body.strip().split('\n'):
            mm=re.match(r'- ([^:]+?):\s*(.*)$',line)
            if mm: f[mm.group(1).strip().lower()]=mm.group(2).strip()
        if kind=='Video':
            out['video'].append(dict(order=int(n),label=label,model=f['model'],duration=num(f['duration']),outputs=num(f['outputs']),cost=num(f['cost']),resolution=f.get('resolution'),prompt=f['prompt']))
        elif kind=='Sound effect':
            out['sound'].append(dict(order=int(n),label=label,type='sfx',seconds=num(f['length setting']),cost=num(f['cost']),prompt=f['prompt']))
        elif kind=='Voiceover':
            vk=[k for k in f if k.startswith('voice')][0]
            out['sound'].append(dict(order=int(n),label=label,type='vo',voice=f[vk],cost=num(f['cost']),script=f['script']))
        else:
            out['music'].append(dict(order=int(n),label=label,description=f['description']))
    return out
def carbon():
    t=open('t-b/ORDERS-%s.md'%RND,encoding='utf-8').read()
    out={'video':[],'sound':[],'music':[]}
    for m in re.finditer(r'^### Order (\d+) — (.*?)\n(.*?)(?=^### |^## |^---|\Z)',t,re.S|re.M):
        n,head,body=m.groups(); f={}
        for line in body.strip().split('\n'):
            mm=re.match(r'- \*\*([^:]+?):\*\*\s*(.*)$',line)
            if mm: f[mm.group(1).strip().lower()]=mm.group(2).strip().strip('`')
        lab=re.search(r'`([^`]+)`',head); label=lab.group(1) if lab else head
        if 'model' in f:
            out['video'].append(dict(order=int(n),label=label,model=f['model'],duration=num(f['duration']),outputs=num(f['number of outputs']),cost=num(f['cost']),resolution=f.get('resolution'),prompt=f['prompt']))
        elif f.get('type','').lower().startswith('voice'):
            out['sound'].append(dict(order=int(n),label=label,type='vo',voice=f['voice description'],cost=num(f['cost']),script=f['script']))
        elif f.get('type','').lower().startswith('sound'):
            ls=f.get('length setting','')
            out['sound'].append(dict(order=int(n),label=label,type='sfx',seconds=(None if 'auto' in ls.lower() else num(ls)),cost=num(f['cost']),prompt=f['prompt']))
        else:
            out['music'].append(dict(order=int(n),label=head,description=f.get('description')))
    return out
def astra():
    t=open('t-c/ORDERS-%s.md'%RND,encoding='utf-8').read()
    out={'video':[],'sound':[],'music':[]}
    common=re.search(r'^> (.*)$',t,re.M).group(1).strip()
    vm=re.search(r'\*\*Baker voice\*\* — (.*)$',t,re.M); voice=vm.group(1).strip() if vm else None
    for line in t.split('\n'):
        if not re.match(r'^\| \d\d · ',line): continue
        c=[x.strip() for x in line.strip().strip('|').split('|')]
        n=int(c[0][:2]); label=c[0].split('·')[1].strip()
        if len(c)==8:
            out['video'].append(dict(order=n,label=label,model=c[1],duration=num(c[3]),outputs=num(c[4]),cost=num(c[7]),resolution=c[2],prompt=common+' '+c[6]))
        elif len(c)==5:
            if c[1]=='Voiceover': out['sound'].append(dict(order=n,label=label,type='vo',voice=voice,cost=num(c[4]),script=c[3].strip('`')))
            else: out['sound'].append(dict(order=n,label=label,type='sfx',seconds=(None if c[2].lower().startswith('auto') else num(c[2])),cost=num(c[4]),prompt=c[3]))
        elif len(c)==3:
            out['music'].append(dict(order=n,label=label,description=c[2]))
    return out
allo={'t-a':fable(),'t-b':carbon(),'t-c':astra()}
json.dump(allo,open('_desk/orders/orders-%s.json'%RND,'w',encoding='utf-8'),ensure_ascii=False,indent=1)
gt=dict(v=0,s=0,m=0,clips=0)
for d,o in allo.items():
    v=sum(x['cost'] for x in o['video']); clips=sum(x['outputs'] for x in o['video']); s=sum(x['cost'] for x in o['sound'])
    sfx=[x for x in o['sound'] if x['type']=='sfx']; vo=[x for x in o['sound'] if x['type']=='vo']
    print(d,'video orders',len(o['video']),'clips',clips,'credits',v,'| sfx',len(sfx),'vo',len(vo),'credits',s,'| music',len(o['music']))
    # checks
    for x in o['video']:
        per={'Veo 3.1 Quality':100,'Veo 3.1 Fast':10,'Veo 3.1 Lite':5}.get(x['model'])
        exp=per*x['outputs'] if per else 3*x['duration']*x['outputs']
        if exp!=x['cost']: print('  VIDEO COST MISMATCH',x['order'],x['model'],x['cost'],exp)
    for x in vo:
        if len(x['script'])!=x['cost']: print('  VO MISMATCH',x['order'],len(x['script']),x['cost'])
    for x in sfx:
        exp=100 if x['seconds'] is None else 11*x['seconds']
        if exp!=x['cost']: print('  SFX MISMATCH',x['order'],x['seconds'],x['cost'])
    gt['v']+=v;gt['s']+=s;gt['m']+=len(o['music']);gt['clips']+=clips
print('TOTAL',gt)
from collections import Counter
c=Counter()
for d,o in allo.items():
    for x in o['video']: c[(x['model'],x['duration'],x['resolution'])]+=x['outputs']
for k,v in sorted(c.items()): print(k,v)
