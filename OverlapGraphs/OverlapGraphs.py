



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

with open('OverlapGraphs/overlap_graph.txt','r') as file:
    seq_dict=fasta2dict(file.read())
    pairs_list=overlap_pairs(seq_dict,3)
    pairs_format=''
    for pair in pairs_list:
        pairs_format+=pair[0]+ ' '+pair[1]+'\n'
    fh=open('OverlapGraphs/overlap_graph_results.txt','w+')
    fh.write(pairs_format)
    fh.close()



############################USER SOLUTIONS###################################
#!/usr/bin/env python

import sys
import re
import collections

with open(sys.argv[1], 'rU') as f:
  data = f.read().replace("\n","")

pattern = re.compile(r'>(?P<label>Rosalind_\d{4})\s*(?P<bases>[ACGT\s]+)')

dnastrings = collections.OrderedDict(pattern.findall(data))

for s1 in dnastrings.keys():
  for s2 in dnastrings.keys():
    if s1 != s2:
      if dnastrings[s1][-3:] == dnastrings[s2][:3]:
        print s1, s2
