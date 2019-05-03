import numpy as np
import collections

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

def conscores(matrix):
    scoredict={}
    for column in matrix.T:
        scoredict.update(collections.Counter(column))
    return scoredict

with open('fasta_consensus.txt','r') as file:
    seqdict=fasta2dict(file.read())

seqmatrix=np.array([list(x) for x in seqdict.values()])
print(conscores(seqmatrix))




'''
matrix = list(zip(*seqdict.values()))

#profile_matrix = map(lambda x: dict((base, x.count(base)) for base in "ACGT"), matrix)
profile_matrix=[dict((base,x.count(base)) for base in 'ACGT') for x in matrix]

consensus = [max(x,key = x.get) for x in profile_matrix]

    
print (''.join(consensus))

for base in "ACGT":
    print (base+":", end=' ')
    for x in profile_matrix:
        print (x[base], end=' ')
    print ("")
'''
