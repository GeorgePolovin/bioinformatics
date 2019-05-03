import time

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

t0=time.time()
with open('rosalind_gc.txt', 'r') as f:
    sequences = f.read()
    #print(fasta2dict(sequences))
    fh=open('rosalind_gc_output.txt','w+')
    fh.write(sort_by_GC(fasta2dict(sequences)))
    fh.close()

t1=time.time()
print(t1-t0)
