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

#trim translated protein sequence from Start(Met) to Stop(*) codon; first find all 'M' position and trim sequence to first '*' found in each case
def trim_orf(prot_seq):
    orfs_in_seq=[]
    start_pos=[index for index,aa in enumerate(prot_seq) if aa=='M']
    for start in start_pos:
        end=prot_seq[start:].find('*')
        if end!=-1:
            orfs_in_seq.append(prot_seq[start:end+start])
    return orfs_in_seq

#interate through all 3 open reading frames of forward and reverse sequence; be sure to choose endpoint as mod 3 to avoid error, and extend the list of translated open reading frame
def list_all_orfs(dna_seq):
    orfs=[]
    for seq in [dna_seq,DNAreverse_complement(dna_seq)]:
        for i in range(0,3):
            endpoint=len(seq)-len(seq[i:])%3
            cur_orf=trim_orf(translate(seq[i:endpoint]))
            orfs.extend(cur_orf)
    return list(dict.fromkeys(orfs)) #remove duplicate sequences and maintain order

#write results to txt file
def write_result(result_list, filename):
    with open(filename,'w+') as file:
        for seq in result_list:
            file.write(seq+'\n')

#read rosalind download txt input and output results in txt
def read_then_write(inputfile):
    with open(inputfile,'r') as file:
        DNA_seq=''.join(file.read().split('\n')[1:])
        results=list_all_orfs(DNA_seq)
        write_result(results,inputfile.replace('.txt','')+'_results.txt')


#read_then_write('open_reading_frame/rosalind_orf.txt')

#==============USER_SOLUTIONS==============
def revcomp(s):
    r = s.translate(str.maketrans('ACTG','TGAC'))
    return r[::-1]

dna = "AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG"

table = """
TTT F      CTT L      ATT I      GTT V
TTC F      CTC L      ATC I      GTC V
TTA L      CTA L      ATA I      GTA V
TTG L      CTG L      ATG M      GTG V
TCT S      CCT P      ACT T      GCT A
TCC S      CCC P      ACC T      GCC A
TCA S      CCA P      ACA T      GCA A
TCG S      CCG P      ACG T      GCG A
TAT Y      CAT H      AAT N      GAT D
TAC Y      CAC H      AAC N      GAC D
TAA Stop   CAA Q      AAA K      GAA E
TAG Stop   CAG Q      AAG K      GAG E
TGT C      CGT R      AGT S      GGT G
TGC C      CGC R      AGC S      GGC G
TGA Stop   CGA R      AGA R      GGA G
TGG W      CGG R      AGG R      GGG G"""
table = dict(zip(table.split()[::2],table.split()[1::2]))


stop = ["TAA","TAG","TGA"]
proteins = []
for s in [dna,revcomp(dna)]:
    for i in range(len(s)):
        if s[i:i+3] == "ATG":
            for j in range(i,len(s),3):
                if s[j:j+3] in stop:
                    c = [s[k:k+3] for k in range(i,j,3)]
                    proteins.append( ''.join(map(lambda x:table[x],c)) )
                    break
for seq in set(proteins):
    print(seq)
