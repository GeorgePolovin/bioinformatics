'''
Given: At most 15 UniProt Protein Database access IDs.

Return: For each protein possessing the N-glycosylation motif, output its given access ID followed by a list of locations in the protein string where the motif can be found.
N-glycosylation motif is written as N{P}[ST]{P}

Sample Dataset
A2Z669
B5ZC00
P07204_TRBM_HUMAN
P20840_SAG1_YEAST
Sample Output
B5ZC00
85 118 142 306 395
P07204_TRBM_HUMAN
47 115 116 382 409
P20840_SAG1_YEAST
79 109 135 248 306 348 364 402 485 501 614

'''
import urllib.request #native python3 lib for pulling data from url

uniprot_db='http://www.uniprot.org/uniprot/'
folder_dir='protein_motif/'

#Take a list of uniprot access IDs and add fasta protein sequence to dictionary with structure of id:sequence
def uniprot_to_dict(id_list):
    dict={}
    for id in id_list:
        fasta_list_split=urllib.request.urlopen(uniprot_db+id+'.fasta').read().decode('utf-8').split('\n')
        fasta=''.join([fasta_list_split[i] for i in range(1,len(fasta_list_split))])
        dict[id]=fasta
    return dict

#Take a rosalind input file and parse uniprot access IDs into a list
def id_list(file):
    with open(folder_dir+file,'r') as file:
        list=[item for item in file.read().split('\n') if item!='']
    return list

def find_Nglycosylation_motif(prot_dict):
    for id in prot_dict:



#-----------------RUN_SCRIPT------------------
id_list=id_list('protein_motif.txt')
seq_dict=uniprot_to_dict(id_list)
print(seq_dict)

'''
def FindMotif(s,t):
    output=[]
    if t not in s:
        print('match not found')
    while t in s:
        index=s.index(t)+1
        if output==[]:
            output.append(index)
        else:
            output.append(output[-1]+index)
        s=s[index:]
    return ' '.join(str(item) for item in output)
'''
