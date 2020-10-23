import os
import sys

def main():

    cpt=0
    cpt_2=1
    cpt_parts=18

    if not os.path.isdir('train'):
        os.mkdir('train')
    if not os.path.isdir('test'):
        os.mkdir('test')
    parent_dir = sys.argv[1]

    for conll in os.listdir(parent_dir):
        parts=[6,7,14,29,98,138,144,35,64,81,91,92,95,96,117,137,140,150,153,172]
        with open(parent_dir+conll,"r",encoding="utf-8") as c:
            conll2=list(c)
            towrite=[]
            temp=[]
            for e in conll2:
                if '#end' not in e:
                    temp.append(e)
                else:
                    temp.append(e)
                    i=temp[0].split('; part')[-1].strip()
                    name=temp[1].split('\t')[0]
                    if len(str(cpt_parts))==2:
                        n='wb/eng/00/eng_00'+str(cpt_parts)
                    else:
                        n='wb/eng/00/eng_0'+str(cpt_parts)
                    begin='#begin document ('+n+'); part '+'000'+'\n'
                    for a in temp:
                        if '#begin' in a:
                            a=begin
                            towrite.append(a)
                        elif '#begin' not in a and '#end' not in a and a!='\n':
                            a=a.strip('\n').split('\t')
                            a[6] = '-'
                            a[7] = '-'
                            a[0]=n
                            a[1]='0'
                            a = a+['\n']
                            a='\t'.join(a)
                            towrite.append(a)
                        else:
                            towrite.append(a)
                    if int(i) in parts:
                        if len(str(cpt_parts))==2:
                            out_conll='test/eng_00'+str(cpt_parts)+'.9v_gold_conll'
                            cpt_parts+=1
                        else:
                            out_conll='test/eng_0'+str(cpt_parts)+'.9v_gold_conll'
                            cpt_parts+=1

                    else:
                        if len(str(cpt_parts))==2:
                            out_conll='train/eng_00'+str(cpt_parts)+'.9v_gold_conll'
                            cpt_parts+=1
                        else:
                            out_conll='train/eng_0'+str(cpt_parts)+'.9v_gold_conll'
                            cpt_parts+=1
                    with open(out_conll,'w',encoding='utf-8') as out:
                        for t in towrite:
                            out.write(t)
                    temp=[]
                    towrite=[]

if __name__ == '__main__':
    main()
