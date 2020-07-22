#!/usr/bin/env python
# coding: utf-8

number=0
import glob, os
#write the path to the docs 
genre='/wb/eng/00/'
#write the full path to the genre output folder, where the file must appear
path='./test2/data/english/annotations'+genre
#write the full path to the genre input folder, where files msut be found
parent_dir = './test/data/english/annotations'+genre
for conll in glob.glob(os.path.join(parent_dir, '*.9v_gold_conll')):
    print(conll)
    with open(conll,'r') as one:   
        one=list(one)
        new=[]
        verbs='VBP|VBG|VBD|MD|VB|VB|VBZ|VBN'.split('|')
        for e in one:
            if e[0]=='#':
                new.append(e)
            elif e=='\n':
                new.append(e)
            else:
                e=e.split()
                new.append(e)
        u=[m for m in new if m!='\n' and '#' not in m[0]]
        final=[]
        final0=[]
        final1=[]
        temp_0=[]
        temp_1=[]
        only_one=[]
        for e in new:
            if isinstance(e,list):
                if e[4] in verbs:
                    if e[-1]!='-':
                         #print('-------')
                        #  #print(e,'verb itself')
                        annotation=e[-1].replace(')','').replace('(','').split('|')
                        anno=e[-1].split('|')
                         #print(annotation)
                        if isinstance(annotation,list) and len(annotation)!=1:
                            if '(' in anno[0] and ')' in anno[0]:
                                #print(anno[0],'anno0')
                                annotation=str(anno[0].replace(')','').replace('(',''))
                                i=[f for f in u if f[-1]=='('+annotation or f[-1]==annotation+')' or f[-1]=='('+annotation+')' and '|' not in f[-1]]
                                temp=[g for g in u if '|' in g[-1]]
                                for j in temp:
                                    h=j[-1].split('|')
                                    if h[0]=='('+annotation or h[0]==annotation+')' or  h[0]=='('+annotation+')':
                                        temp_0.append(j)
                                        #print('| here')
                                        #print(j)
                                    elif h[1]=='('+annotation or h[1]==annotation+')' or  h[1]=='('+annotation+')':
                                        temp_1.append(j)
                                        #print('| here')
                                        #print(j)
                                if len(i)+len(temp_0)+len(temp_1)==2:
                                    #print('yes')
                                    for k in i:
                                        #print(k)
                                        final.append(k)
                                    for k in temp_0:
                                        #print('comes to temp_0')
                                        final0.append(k)
                                    for k in temp_1:
                                        #print('comes to temp_1')
                                        final1.append(k)
                                else:
                                    final0.append(e)
                                temp_1=[]
                                temp_0=[]
                                
                            elif '(' in anno[1] and ')' in anno[1]:
                                #print(anno[0],'anno1')
                                annotation=str(anno[1].replace(')','').replace('(',''))
                                i=[f for f in u if f[-1]=='('+annotation or f[-1]==annotation+')' or f[-1]=='('+annotation+')' and '|' not in f[-1]]
                                temp=[g for g in u if '|' in g[-1]]
                                for j in temp:
                                    h=j[-1].split('|')
                                    if h[0]=='('+annotation or h[0]==annotation+')' or  h[0]=='('+annotation+')':
                                        temp_0.append(j)
                                        #print('| here')
                                        #print(j)
                                    elif h[1]=='('+annotation or h[1]==annotation+')' or  h[1]=='('+annotation+')':
                                        temp_1.append(j)
                                        #print('| here')
                                        #print(j)
                                if len(i)+len(temp_0)+len(temp_1)==2:
                                    #print('yes')
                                    for k in i:
                                        #print(k)
                                        final.append(k)
                                    for k in temp_0:
                                        #print('comes to temp_0')
                                        final0.append(k)
                                    for k in temp_1:
                                        #print('comes to temp_1')
                                        final1.append(k)
                                else:
                                    final1.append(e)
                                temp_1=[]
                                temp_0=[]
                            else:
                                #print('it goes nowhere')
                                pass
                                
                            #an1=annotation[0]
                            #an2=annotation[1]
                            #i1=[f[-1] for f in u if '('+a1+'\n' in f[-1] or f[-1]==a1+')\n' or '('+a1+')' in f[-1]]
                            #i2=i=[f[-1] for f in u if '('+a2+'\n' in f[-1] or f[-1]==a2+')\n' or '('+a2+')' in f[-1]]
                            #print('WARNING')
                        else:
                            annotation=str(annotation[0])
                            i=[f for f in u if f[-1]=='('+annotation or f[-1]==annotation+')' or f[-1]=='('+annotation+')' and '|' not in f[-1]]
                            temp=[g for g in u if '|' in g[-1]]
                            for j in temp:
                                h=j[-1].split('|')
                                if h[0]=='('+annotation or h[0]==annotation+')' or  h[0]=='('+annotation+')':
                                    temp_0.append(j)
                                    #print('| here')
                                    #print(j)
                                elif h[1]=='('+annotation or h[1]==annotation+')' or  h[1]=='('+annotation+')':
                                    temp_1.append(j)
                                    #print('| here')
                                    #print(j)
                            if len(i)+len(temp_0)+len(temp_1)==2:
                                #print('yes')
                                for k in i:
                                    #print(k)
                                    final.append(k)
                                for k in temp_0:
                                    #print('comes to temp_0')
                                    final0.append(k)
                                for k in temp_1:
                                    #print('comes to temp_1')
                                    final1.append(k)
                            else:
                                if '(' in e[-1] and ')' in e[-1]:
                                    final.append(e)
                                else:
                                    #print('goes nowhere')
                                    pass
                                
                            temp_1=[]
                            temp_0=[]
        #print(final)
        last=[]
        tog=0
        for e in new:
            if e in final:
                if ')' in e[-1]:
                    tog+=1
                #print(e)
                e[-1]='-'
                #print(e)
                last.append(e)
                
            elif e in final0:
                #print(e)
                comp=e[-1].split('|')
                e[-1]=comp[1]
                #print(e)
                if ')' in e[-1]:
                    tog+=1
                last.append(e)
            elif e in final1:
                #print(e)
                comp=e[-1].split('|')
                e[-1]=comp[0]
                #print(e)
                if ')' in e[-1]:
                    tog+=1
                last.append(e)
            else:
                last.append(e)

        #------------------------------------
        print(tog,'mentions')
        print('STATS')
         #ugg=len(final)+len(final0)+len(final1)
        number+=tog
        print(tog)
        end=[]
        name=last[1][0].split('/')[-1]
        #print('name',name)
        for e in last:
            if isinstance(e,list):
                e='   '.join(e)+'\n'
                end.append(e)
            else:
                end.append(e)
        #print(end[:100])
        with open(path+name+'.9v_gold_conll','w',encoding='utf-8') as out:
            for e in end:
                out.write(e)
print(number)
        


