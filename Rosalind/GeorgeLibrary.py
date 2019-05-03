def GCcontent(seq):
    return 100*(seq.count('G') + seq.count('C'))/len(seq)

def fasta2dict(file):
    pairs={}
    cur_ID=''
    cur_seq=[]
    for item in file.split('\n'):
        if item.startswith('>') and cur_ID=='':
            cur_ID=item.lstrip('>')
        elif item.startswith('>') and cur_ID!='':
            pairs[cur_ID]=''.join(cur_seq)
            cur_ID=item.lstrip('>')
            cur_seq=[]      
        else:
            cur_seq.append(item)
        pairs[cur_ID]=''.join(cur_seq)
    return pairs

def sort_by_GC(dic):
    maxGC=0
    maxkey=''
    for key, sequence in dic.items():
        if GCcontent(sequence)>maxGC:
            maxGC=GCcontent(sequence)
            maxkey=key
        else:
            continue
    return str(maxkey) + '\n' + str(maxGC)

def reversecomplement(s):
	nucl_replace={'A':'T','T':'A','C':'G','G':'C'}
	revcom=''
	for nucl in s.strip('\n')[::-1]:
		revcom = revcom + nucl_replace[nucl]
	return revcom

def count(seq):
      return seq.count("A"), seq.count("G"), seq.count("C"), seq.count("T")

def txn(str):
    return str.replace('T','U')

def GCcontent(seq):
    return 100*(seq.count('G') + seq.count('C'))/len(seq)

def fasta2dict(file):
    pairs={}
    cur_ID=''
    cur_seq=[]
    for item in file.split('\n'):
        if item.startswith('>') and cur_ID=='':
            cur_ID=item.lstrip('>')
        elif item.startswith('>') and cur_ID!='':
            pairs[cur_ID]=''.join(cur_seq)
            cur_ID=item.lstrip('>')
            cur_seq=[]      
        else:
            cur_seq.append(item)
        pairs[cur_ID]=''.join(cur_seq)
    return pairs

def sort_by_GC(dic):
    maxGC=0
    maxkey=''
    for key, sequence in dic.items():
        if GCcontent(sequence)>maxGC:
            maxGC=GCcontent(sequence)
            maxkey=key
        else:
            continue
    return str(maxkey) + '\n' + str(maxGC)     
