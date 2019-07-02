'''
import numpy as np
from numpy import array as arr

with open('rosalind6.txt') as f:
    A = [arr(list(line.strip())) for line in f]
    A = arr(A)

genes = arr(list('ACGT'))
P = arr([(A == g).sum(axis=0) for g in genes])
c = genes[P.argmax(axis=0)]
c = ''.join(c)

print c
for i, g in enumerate(genes):
    print '%s:' % g, ' '.join(map(str, P[i]))
'''
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


with open('fasta_consensus.txt','r') as file:
    seqdict=fasta2dict(file.read())

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
def cons(strings):
    from collections import Counter
    counters = map(Counter, zip(*strings))
    consensus = "".join(c.most_common(1)[0][0] for c in counters)
    profile_matrix = "\n".join(b + ": " + \
        " ".join(str(c[b]) for c in counters) for b in "ACGT")
    return consensus + "\n" + profile_matrix

matrix = list(seqdict.values())
print(cons(matrix))
'''
