#!/usr/bin/env python
# coding: utf-8

# In[5]:


import sys
import glob, os
os.chdir('.')
for file in glob.glob("*.gold_conll"):
    with open(cur_dir,'r',encoding='utf-8') as conll:
    conll=list(conll)
    cpt=0
    heyho=[]
    for e in conll:
        if e!='\n' and e[0]!='#':
            cpt+=1
            b=e.split()
            heyho.append(b)
    different=[]
    for e in heyho:
        if e[-1]!='-':
            hm=str(e[-1]).replace('(','').replace(')','').strip()
            different.append(hm)
    op=conll[-3].split()
    print(int(op[1])+1,'\t',cpt,'\t',len(set(different)))