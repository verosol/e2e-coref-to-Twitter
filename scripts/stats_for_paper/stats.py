#!/usr/bin/env python
# coding: utf-8

import sys

with open(sys.argv[1], 'r') as input_file:
    input_file=list(input_file)
    cnt=0
    verbs='VBP|VBG|VBD|MD|VB|VB|VBZ|VBN'.split('|')
    part=-1
    cnt_ann=0
    out=[]
    cnt_mentions=0
    dif_ann=[]
    for line in input_file:
        if '#begin document' not in line:
            if line!='\n' and line!='#end document\n':
                cnt+=1
                line=line.split(sys.argv[2])
                if '-\n' not in line[-1] :
                    cnt_ann+=1
                    annotation=line[-1].replace('\n','').replace(')','').replace('(','')
                    if '|' in annotation:
                        annotation=annotation.split('|')
                        for i in annotation:
                            if i not in dif_ann:
                                dif_ann.append(i)
                    else:
                        if annotation not in dif_ann:
                            dif_ann.append(annotation)
        else:
            result=[str(part),str(cnt),str(cnt_ann),str(len(dif_ann))]
            out.append(result)
            cnt=0
            part+=1
            cnt_ann=0
            dif_ann=[]
    #tokens----------------------------
    tokens=[int(e[1]) for e in out]
    print(sum(tokens),'- tokens')
    #chains----------------------------
    chains=[int(e[3]) for e in out]
    print(sum(chains),'- chains')
    #mentions----------------------
    token_lines=[e.split('\t') for e in input_file if e!='\n' and e[0]!='#']
    mentions1=[1 for e in token_lines if ')\n' in e[-1]]
    mentions2=[1 for e in token_lines if ')|' in e[-1]]
    print(sum(mentions1)+sum(mentions2),'- mentions')
    #documents----------------------
    docs=[1 for e in input_file if '#begin' in e]
    print(sum(docs)-1, '- docs')
    #verbs statistics----------------
    new_docs=[]
    temp=[]
    for line in token_lines:
        for idx in line:
            if idx=='':
                pass
            else:
                temp.append(idx)
        new_docs.append(temp)
        temp=[]
    verb_ents=[1 for e in new_docs if e[4] in verbs and '(' in e[-1] and ')\n' in e[-1]] 
    verb_ents2=[1 for e in new_docs if ')|' in e[-1] and e[-1].count('(')>=1 and e[4] in verbs]
    print(sum(verb_ents)+sum(verb_ents2),'- verbal eniti(es)')
    print(((sum(verb_ents2)+sum(verb_ents))*100)/(sum(mentions1)+sum(mentions2)),'% - percentage of the verbs to total mentions')



