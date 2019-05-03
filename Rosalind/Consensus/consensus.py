import string

seq1='ATCCAGCT'
seq2='GGGCAACT'
seq3='ATGGATCT'
seq4='AAGCAACC'

seqdict={'seq1':seq1, 'seq2':seq2, 'seq3':seq3, 'seq4':seq4}

#print(seq1.translate(str.maketrans('AGCT', '1234')))

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

def conscore(seqdic):
    A=[]
    T=[]
    G=[]
    C=[]
    for key in seqdic:
        if A == []:
            for base in seqdic[key]:
                if base=='A':
                    A.append(1),T.append(0),G.append(0),C.append(0)
                if base=='T':
                    A.append(0),T.append(1),G.append(0),C.append(0)
                if base=='G':
                    A.append(0),T.append(0),G.append(1),C.append(0)
                if base=='C':
                    A.append(0),T.append(0),G.append(0),C.append(1)
        else:
            for i,base in enumerate(seqdic[key]):
                if base=='A':
                    A[i]+=1
                    T[i]+=0
                    G[i]+=0
                    C[i]+=0
                if base=='T':
                    A[i]+=0
                    T[i]+=1
                    G[i]+=0
                    C[i]+=0
                if base=='G':
                    A[i]+=0
                    T[i]+=0
                    G[i]+=1
                    C[i]+=0
                if base=='C':
                    A[i]+=0
                    T[i]+=0
                    G[i]+=0
                    C[i]+=1
    conscoredict={'A':A,'C':C,'G':G,'T':T}
    return conscoredict

def conseq(conscoredict):
    conseq=[]
    scoretuples=list(zip(*conscoredict.values()))
    for tuple in scoretuples:
        conseq.append(tuple.index(max(tuple)))
    conseqlist=str(conseq).translate(str.maketrans('0123', 'ACGT'))
    return conseqlist

def formatdic(dic):
    tempstr=''
    for key in dic:
        templist=dic[key]
        tempstr+=key +': '+str(templist).strip('[]').replace(',','')+'\n'
    return tempstr
   
with open('rosalind_cons.txt','r') as file:
    seqdict=fasta2dict(file.read())
    scores=conscore(seqdict)
    fh=open('rosalind_cons_output.txt','w+')
    fh.write(conseq(scores).strip('[]').replace(', ','')+'\n')
    fh.write(formatdic(scores))
    fh.close()



sequence=conseq(scores)
print(sequence.strip('[]').replace(', ',''))
print(formatdic(scores))

