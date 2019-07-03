'''
Given: A collection of k (k≤100) DNA strings of length at most 1 kbp each in FASTA format.

Return: A longest common substring of the collection. (If multiple solutions exist, you may return any single solution.)

Sample Dataset
>Rosalind_1
GATTACA
>Rosalind_2
TAGACCA
>Rosalind_3
ATACA
Sample Output
AC
'''
def fasta_to_dict(fasta_file):
    seq_dict={}
    id=''
    multiple_line_seq=''
    with open(fasta_file, 'r') as file:
        for line in file:
            if '>' in line:
                if id=='':
                    id=line.strip('>\n')
                else:
                    seq_dict[id]=multiple_line_seq
                    multiple_line_seq=''
                    id=line.strip('>\n')
            else:
                multiple_line_seq+=line.strip('>\n')
            seq_dict[id]=multiple_line_seq
    return seq_dict

def longest_shared_motif(dict):
    motifs=[]
    shortest_seq_id=min(dict, key=lambda k: len(dict[k]))
    shortest_seq=dict[shortest_seq_id]
    for start in range(0,len(shortest_seq)):
        for end in range(0,len(shortest_seq)):
            ifcommon=True
            for id in dict:
                if dict[shortest_seq_id][start:end] in dict[id]:
                    continue
                else:
                    ifcommon=False
                    break
            if ifcommon==True:
                motifs.append(dict[shortest_seq_id][start:end])
    return max(motifs, key=len)


seq_dict=fasta_to_dict('shared_motif/shared_motif.txt')
print(longest_shared_motif(seq_dict))


##########USER SOLUTIONS##########
def substr_in_all(arr, part):
  for dna in arr:
    if dna.find(part)==-1:
      return False
  return True

def common_substr(arr, l):
  first = arr[0]
  for i in range(len(first)-l+1):
    part = first[i:i+l]
    if substr_in_all(arr, part):
      return part
  return ""

def longest_common_substr(arr):
  l = 0; r = len(arr[0])

  while l+1<r:
    mid = (l+r) / 2
    if common_substr(arr, mid)!="":
      l=mid
    else:
      r=mid

  return common_substr(arr, l)

'''
Faster (<0.1s) solution using Binary search on the length of the longest common substring. Time complexity: O(log(len)∗len∗len∗k).

The task could be solved in O(log(len)∗len∗k) with addition of hashing for parallel check of all the substrings of the fixed lenght to the current solution (see Rabin-Karp algorithm).
'''
