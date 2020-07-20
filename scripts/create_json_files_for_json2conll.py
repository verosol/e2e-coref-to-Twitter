#!/usr/bin/env python
# coding: utf-8

# In[3]:


#gets json predicted file issued from the prediction mode of the e2e-coref
with open ('output.json','r',encoding='utf-8') as inp:
    inp=list(inp)
    for e in inp:
        part=e.split('doc_key')[1].replace('"','').replace(':','').split(',')[0].split('_')[2].replace('}','')
        print(part)
        hm=e.split('doc_key')[1].replace('"','').replace(':','').split(',')[0].replace('/','_')[:-1]
        print(hm)
        hm=hm.split('_')
        final=hm[0]+'_'+hm[1]+'_'+hm[2]+'_'+hm[4]
        print(final)
        if len(part)==1:
            print(part)
            #needs full path to the output folder
            with open('./test/'+final.split()[0]+'_000'+'.json','w') as out:
                out.write(e)
        else:
            with open('./test/'+final.split()[0]+'_000'+'.json','w') as out:
                out.write(e)
        
        
        
        
    
        
        


# In[ ]:





# In[ ]:




