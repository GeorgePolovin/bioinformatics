
'''
Given: A protein string of length at most 1000 aa.

Return: The total number of different RNA strings from which the protein could have been translated, modulo 1,000,000. (Don't neglect the importance of the stop codon in protein translation.)

Sample Dataset
MA
Sample Output
12
'''

codonperaminoacid={'F':2,'L':6,'S':6,'Y':2,'Stop':3,'C':2,'W':1,'P':4,'H':2,'Q':2,'R':6,'I':3,'M':1,'T':4,'N':2,'K':2,'V':4,'A':4,'D':2,'E':2,'G':4}

def num_unique_rna_seq(prot_seq):
    count=3 #3 stop codons for any RNA sequence
    for aa in prot_seq:
        count=(count*codonperaminoacid[aa])%1000000
    return count

def import_seq(filename):
    with open(filename, 'r') as file:
        seq=file.read().strip('\n')
    return seq

def output_result(result,result_filename):
    with open(result_filename, 'w+') as file:
        file.write(str(result))

#===========SCRIPT=====================
aa_seq=import_seq('infer_mrna/infer_mrna.txt')
output_result(num_unique_rna_seq(aa_seq),'infer_mrna/infer_mrna_result.txt')

#=======USER_SOLUTION=======
bases = ['U', 'C', 'A', 'G']
codons = [a+b+c for a in bases for b in bases for c in bases]
amino_acids = 'FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
codon_table = dict(zip(codons, amino_acids))

datafile = open('rosalind_mrna.txt','r')
prot = datafile.read()

number = 1
for aa in prot:
        number *= amino_acids.count(aa)

print number * amino_acids.count('*')%1000000
