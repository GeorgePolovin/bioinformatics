



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

def overlap_pairs(seqs,overlap_len):
    overlaps=[]
    for id1 in seqs:
        for id2 in seqs:
            if id1==id2:
                continue
            else:
                if seqs[id1][-(overlap_len):]==seqs[id2][:(overlap_len)]:
                    overlaps.append((id1,id2))
                else:
                    continue
    return overlaps
                    




string='''>Rosalind_0498
AAATAAA
>Rosalind_2391
AAATTTT
>Rosalind_2323
TTTTCCC
>Rosalind_0442
AAATCCC
>Rosalind_5013
GGGTGGG
'''

DNAseq=fasta2dict(string)
print(overlap_pairs(DNAseq,3))
