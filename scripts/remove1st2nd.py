import codecs
import sys

    
first = {'Im', 'im', 'my self', 'me', 'I', 'id', 'myself', 'mine', 'i', 'MY', 'Mine', 'ma', 'My', 'us', 'Our', 'we', 'our', 'We', 'WE', "'s"}
second = {'iur', 'u', 'Youve', 'youu', 'youre', 'You', 'Yours', 'Your', 'Ur', 'YOU', 'YOURE', 'your', 'uv', 'you', 'ya', 'yours', 'U', 'UR', 'yourself','ur', 'YOUR'}

def get_chains(conll):
    
    coref_chains = dict()
    mention_buffer = dict()
    token_dict = dict()
    speaker_dict = dict()
    
    for line in conll:
        if line.split() == []:
            sentence += 1
        elif line.split()[0] == "#begin":
            sentence = 0
        
        if (line.split() != []) and (len(line.split()) == 12):
            coref = line.split()[-1]
            doc_no = int(line.split()[1])
            token_no = int(line.split()[2])
            token = line.split()[3]
            speaker = line.split()[9]
            
            if doc_no not in token_dict:
                token_dict[doc_no] = dict()
                speaker_dict[doc_no] = dict()
            if sentence not in token_dict[doc_no]:
                token_dict[doc_no][sentence] = dict()
                speaker_dict[doc_no][sentence] = dict()
            token_dict[doc_no][sentence][token_no] = token
            speaker_dict[doc_no][sentence][token_no] = speaker
            
            
            if bool(mention_buffer) == True:
                new_mention_buffer = dict()
                for chain_id in mention_buffer:
                    new_mention_buffer[chain_id] = []
                    for mention in mention_buffer[chain_id]:
                        new_mention = [mention[0], mention[1]+" "+token] 
                        new_mention_buffer[chain_id].append(new_mention)
                mention_buffer = new_mention_buffer
                        
                
            if coref != "-":   
                for mention in coref.split("|"):
                    if doc_no not in coref_chains:
                        coref_chains[doc_no] = dict()
                    if sentence not in coref_chains[doc_no]:
                        coref_chains[doc_no][sentence] = dict()
                    if ("(" in mention) and (")" in mention):
                        chain_id = mention.strip("(").strip(")")
                        if chain_id not in coref_chains[doc_no][sentence]:
                            coref_chains[doc_no][sentence][chain_id] = [((int(token_no), int(token_no)), token)]
                        else:
                            coref_chains[doc_no][sentence][chain_id].append(((int(token_no), int(token_no)), token),)
                    elif "(" in mention:
                        chain_id = mention.strip("(")
                        if chain_id not in mention_buffer:
                            mention_buffer[chain_id] = list()
                        mention_buffer[chain_id].append([token_no, token]) 
                    elif ")" in mention:
                        chain_id = mention.strip(")")
                        start = mention_buffer[chain_id][0][0]
                        token = mention_buffer[chain_id][0][1]
                        mention_buffer[chain_id].remove(mention_buffer[chain_id][0])
                        if mention_buffer[chain_id] == []:
                            del mention_buffer[chain_id]
                        if chain_id not in coref_chains[doc_no][sentence]:
                            coref_chains[doc_no][sentence][chain_id] = [((int(start), int(token_no)), token)]
                        else:
                            coref_chains[doc_no][sentence][chain_id].append(((int(start), int(token_no)), token),)
    
    return speaker_dict, token_dict, coref_chains

def chain_sorted_dict(chain_dict):
    chain_sorted_dict = dict()
    for doc in chain_dict:
        chain_sorted_dict[doc] = dict()
        for sentence in chain_dict[doc]:
            for coref in chain_dict[doc][sentence]:
                if coref not in chain_sorted_dict[doc]:
                    chain_sorted_dict[doc][coref] = []
                for mention in chain_dict[doc][sentence][coref]:
                    chain_sorted_dict[doc][coref].append((sentence,)+mention)
    return chain_sorted_dict
    
def remove_chains(coref_chains):
    delete_chains = dict()
    chains = chain_sorted_dict(coref_chains)
    for doc in chains:
        for chain in chains[doc]:
            remove_chain = True
            for (sentence, span, token) in chains[doc][chain]:
                print(token)
                if token not in first|second:
                    print(remove_chain)
                    remove_chain = False
            if remove_chain == True:
                if doc not in delete_chains:
                    delete_chains[doc] = [chain]
                else:
                    delete_chains[doc].append(chain)
    print(delete_chains)
    return delete_chains
            
def rewrite_conll(conll_file):
    new_conll = codecs.open("1st2ndremoved_"+conll_file, 'w', 'utf-8')
    conll = codecs.open(conll_file, 'r', 'utf-8')
    new_document_no = 0
    for line in conll:
        if line.split() == []:
            new_conll.write(line)
        elif line.split()[0] == '#begin': 
            new_conll.write(line)
        elif line.split()[0] == '#end':
            new_conll.write(line)
            new_document_no += 1
        elif line.split()[-1] == '-':
            new_conll.write(line)
        else:
            if new_document_no in delete_chains:
                coref_ids = line.split()[-1].split('|')
                new_coref_ids = coref_ids
                for bracket in coref_ids:
                    coref_id = bracket.strip('(').strip(')')
                    if coref_id in delete_chains[new_document_no]:
                        new_coref_ids.remove(bracket)

                new_coref_string = ''
                
                if len(new_coref_ids) == 0:
                    new_coref_string += '-'
                elif len(new_coref_ids) == 1:
                    new_coref_string += new_coref_ids[0]
                else:
                    for i in range(len(new_coref_ids)-1):
                        new_coref_string += new_coref_ids[i]+'|'
                    new_coref_string += new_coref_ids[-1]
                
                new_line = ''
                for i in range(len(line.split())-1):
                    new_line += line.split()[i]+'\t'
                new_line += new_coref_string+'\n'
                
                new_conll.write(new_line)
                
            else:
                new_conll.write(line)
    new_conll.close()


if __name__ == "__main__":
    
    conll_file = sys.argv[1] 
    f = codecs.open(conll_file, "r", "utf-8")
    chains = get_chains(f)[2]
    delete_chains = remove_chains(chains)
    rewrite_conll(conll_file)

