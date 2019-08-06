'''
Problem
After identifying the exons and introns of an RNA string, we only need to delete the introns and concatenate the exons to form a new string ready for translation.

Given: A DNA string s (of length at most 1 kbp) and a collection of substrings of s acting as introns. All strings are given in FASTA format.

Return: A protein string resulting from transcribing and translating the exons of s. (Note: Only one solution will exist for the dataset provided.)

Sample Dataset
>Rosalind_10
ATGGTCTACATAGCTGACAAACAGCACGTAGCAATCGGTCGAATCTCGAGAGGCATATGGTCACATGATCGGTCGAGCGTGTTTCAAAGTTTGCGCCTAG
>Rosalind_12
ATCGGTCGAA
>Rosalind_15
ATCGGTCGAGCGTGT
Sample Output
MVYIADKQHVASREAYGHMFKVCA
'''

#convert fasta to sequence and list of introns
def fasta2dict(file):
    subsequence={}
    cur_ID=''
    cur_seq=[]
    with open(file,'r') as rfile:
        file_list=rfile.read().split('\n')
        rna_id=file_list[0].lstrip('>')
        for item in file_list:
            if item.startswith('>') and cur_ID=='':
                cur_ID=item.lstrip('>')
            elif item.startswith('>') and cur_ID!='':
                subsequence[cur_ID]=''.join(cur_seq)
                cur_ID=item.lstrip('>')
                cur_seq=[]
            else:
                cur_seq.append(item)
            subsequence[cur_ID]=''.join(cur_seq)
        rna_seq=(rna_id,subsequence.pop(rna_id))
    return rna_seq, subsequence

#compact codon table and translate function by Gaik Tamazian from Rosalind
def translate(dna_seq):
    codon_table = 'KNKNTTTTRSRSIIMIQHQHPPPPRRRRLLLLEDEDAAAAGGGGVVVV*Y*YSSSS*CWCLFLF'
    nucleo = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    protein = ''
    for i in range(0, len(dna_seq), 3):
        protein+=codon_table[nucleo[dna_seq[i]]*16 + nucleo[dna_seq[i+1]]*4 + nucleo[dna_seq[i+2]]]
    return protein

#take input RNA sequence and introns; removes introns and translates sequence
def splice_trans_rna(rna_input):
    rna_id=rna_input[0][0]
    rna_sequence=rna_input[0][1]
    subseq_dict=rna_input[1]
    for id in subseq_dict:
        if subseq_dict[id] in rna_sequence:
            start=rna_sequence.find(subseq_dict[id])
            end=start+len(subseq_dict[id])
            rna_sequence=rna_sequence[:start]+rna_sequence[end:]
    return translate(rna_sequence).strip('*')

def splice_trans_rna2(rna_input):
    rna_id=rna_input[0][0]
    rna_sequence=rna_input[0][1]
    subseq_dict=rna_input[1]
    for id in subseq_dict:
        rna_sequence=rna_sequence.replace(subseq_dict[id],'')
    return translate(rna_sequence).strip('*')

#takes input and returns result file
def input_output(input_filename):
    rosalind_input=fasta2dict(input_filename)
    with open(input_filename.replace('.txt','')+'_result.txt','w+') as wfile:
        wfile.write(splice_trans_rna2(rosalind_input))

input_output('rna_splicing/rosalind_splc.txt')


#########USER_SOLUTIONS##########
'''
from Bio.Seq import Seq
from Bio import SeqIO

instream = SeqIO.parse("rosalind_splc.txt","fasta")
target = str(instream.next().seq)

for intron in instream:
    target = target.replace(str(intron.seq),"")

print Seq(target).translate()[:-1]
'''
