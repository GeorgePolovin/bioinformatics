'''
Problem
Either strand of a DNA double helix can serve as the coding strand for RNA transcription. Hence, a given DNA string implies six total reading frames, or ways in which the same region of DNA can be translated into amino acids: three reading frames result from reading the string itself, whereas three more result from reading its reverse complement.

An open reading frame (ORF) is one which starts from the start codon and ends by stop codon, without any other stop codons in between. Thus, a candidate protein string is derived by translating an open reading frame into amino acids until a stop codon is reached.

Given: A DNA string s of length at most 1 kbp in FASTA format.

Return: Every distinct candidate protein string that can be translated from ORFs of s. Strings can be returned in any order.

Sample Dataset
>Rosalind_99
AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG
Sample Output
MLLGSFRLIPKETLIQVAGSSPCNLS
M
MGMTPRLGLESLLE
MTPRLGLESLLE
'''

#function to take DNA sequence string and return the reverse complement
def DNAreverse_complement(dna_seq):
    return dna_seq.translate(str.maketrans('ATGCN','TACGN'))[::-1]

#compact codon table and translate function by Gaik Tamazian from Rosalind
def translate(dna_seq):
    codon_table = 'KNKNTTTTRSRSIIMIQHQHPPPPRRRRLLLLEDEDAAAAGGGGVVVV*Y*YSSSS*CWCLFLF'
    nucleo = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    protein = ''
    for i in range(0, len(dna_seq), 3):
        protein+=codon_table[nucleo[dna_seq[i]]*16 + nucleo[dna_seq[i+1]]*4 + nucleo[dna_seq[i+2]]]
    return protein






fasta='>Rosalind_99\nAGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG'
protein=translate(fasta.split('\n')[1])
print(protein)
print(protein.find('M'))
print(protein.find('*'))
print(protein[8:22])
print(DNAreverse_complement(fasta.split('\n')[1]))
