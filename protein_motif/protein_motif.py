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
import re
import urllib.request #native python3 lib for pulling data from url


uniprot_db='http://www.uniprot.org/uniprot/'
folder_dir='protein_motif/'

#Take a rosalind input file and parse uniprot access IDs into a list
def id_list(file):
    with open(folder_dir+file,'r') as file:
        list=[item for item in file.read().split('\n') if item!='']
    return list

#Take a list of uniprot access IDs, request fasta data from website, and add fasta protein sequence to dictionary with structure of id:sequence
def uniprot_to_dict(id_list):
    dict={}
    for id in id_list:
        fasta_list_split=urllib.request.urlopen(uniprot_db+id+'.fasta').read().decode('utf-8').split('\n')
        fasta=''.join([fasta_list_split[i] for i in range(1,len(fasta_list_split))])
        dict[id]=fasta
    return dict

#iterate through each sequence to find first instances of N{P}[ST]{P}, then slice sequence after instance and repeat
#store in separate dictionary
def find_Nglycosylation_motif(prot_dict):
    loc_dict={}
    for id in prot_dict:
        index_list=[]
        hit_list=[]
        seq=prot_dict[id]
        if 'N' not in seq:
            continue
        while 'N' in seq:
            index=seq.index('N')
            if index_list==[]:
                index_list.append(index)
            else:
                index_list.append(index_list[-1]+index+1)
            try:
                if seq[index+1]!='P' and seq[index+3]!='P':
                    if seq[index+2]=='S' or seq[index+2]=='T':
                        hit_list.append(index_list[-1]+1)
            except:
                pass
            seq=seq[index+1:]
        loc_dict[id]=hit_list
    return loc_dict

#use real expressions to find each instance of N{P}[ST]{P}
def find_glyco_motif(prot_dict):
    loc_dict={}
    for id in prot_dict:
        loc_dict[id]=[match.start(0)+1 for match in re.finditer('N[^P][ST][^P]',prot_dict[id])]
    return loc_dict

#write protein motif locations to text file
def write_to_file(loc_dict):
    with open(folder_dir+'protein_motif_results.txt','w+') as file:
        for id in loc_dict:
            if loc_dict[id]!=[]:
                file.write(id+'\n'+str(index_dict[id]).strip('[]')+'\n')

#-----------------RUN_SCRIPT------------------
id_list=id_list('protein_motif.txt')
seq_dict=uniprot_to_dict(id_list)
#index_dict=find_Nglycosylation_motif(seq_dict)
index_dict=find_glyco_motif(seq_dict)
write_to_file(index_dict)
