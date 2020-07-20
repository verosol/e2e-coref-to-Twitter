'''
Transforms the output of e2e back into conll format.
Returns a conll file of all documents predicted by e2e. 
'''

import os
import json
import codecs
import sys

# Merged gold conll-file
gold_conll = sys.argv[1]

# Folder with e2e predictions for each document (in json)
json_files = sys.argv[2]

# e2e-predicted conll-file
e2e_conll = sys.argv[3]



def main():

    def get_clusters(filename):

        with codecs.open(json_files+filename+".json", "r", "utf-8") as f:
            cluster_dict = json.load(f)
    
        coref_dict = dict()
        chain_id = 0 

        for chain in cluster_dict["predicted_clusters"]:
            chain_id += 1
            for mention in chain:
                if mention[0] == mention[1]:
                    if mention[0] in coref_dict:
                        coref_dict[mention[0]] += ("|("+str(chain_id)+")")
                    else:
                        coref_dict[mention[0]] = "("+str(chain_id)+")"
                else:
                    if mention[1] < mention[0]:
                        print("!!! span in wrong order !!!")
                        print(mention)
                    if mention[0] in coref_dict:
                        coref_dict[mention[0]] += ("|("+str(chain_id))
                    else:
                        coref_dict[mention[0]] = "("+str(chain_id)
                    if mention[1] in coref_dict:
                        coref_dict[mention[1]] += ("|"+str(chain_id)+")")
                    else:
                        coref_dict[mention[1]] = str(chain_id)+")"
        
        return coref_dict

    conll = codecs.open(gold_conll, "r", "utf-8")
    new_conll = codecs.open(e2e_conll, "w", "utf-8")
    
    for line in conll:
        if line != "\n":
            if line.split()[0] == "#begin":
                print(line)
                directory = line.split()[2].replace("(","").replace(")","").strip(";").split("/")
                part = line.split()[-1]
                filename = directory[0]+"_"+directory[1]+"_"+directory[2]+"_"+directory[3].split("_")[1]+"_"+part
                coref_dict = get_clusters(filename)
                new_conll.write(line)
                line_count = 0
            elif line.split()[0] == "#end":
                new_conll.write(line)
            else:
                if line_count in coref_dict:
                    new_line = ""
                    for entry in line.split()[0:-1]:
                        new_line += entry+"\t"
                    new_line += coref_dict[line_count]
                    new_conll.write(new_line+"\n")
                    line_count += 1
                else:
                    new_line = ""
                    for entry in line.split()[0:-1]:
                        new_line += entry+"\t"
                    new_line += "-"
                    new_conll.write(new_line+"\n")
                    line_count += 1
        else:
            new_conll.write(line)        
                
    conll.close()
    new_conll.close()
        
if __name__ == "__main__":
    main()
              

