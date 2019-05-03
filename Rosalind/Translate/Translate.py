import re

x='''
UUU F      CUU L      AUU I      GUU V
UUC F      CUC L      AUC I      GUC V
UUA L      CUA L      AUA I      GUA V
UUG L      CUG L      AUG M      GUG V
UCU S      CCU P      ACU T      GCU A
UCC S      CCC P      ACC T      GCC A
UCA S      CCA P      ACA T      GCA A
UCG S      CCG P      ACG T      GCG A
UAU Y      CAU H      AAU N      GAU D
UAC Y      CAC H      AAC N      GAC D
UAA Stop   CAA Q      AAA K      GAA E
UAG Stop   CAG Q      AAG K      GAG E
UGU C      CGU R      AGU S      GGU G
UGC C      CGC R      AGC S      GGC G
UGA Stop   CGA R      AGA R      GGA G
UGG W      CGG R      AGG R      GGG G 
'''

#print(codondictionary.replace(':','\':\'').replace(',','\',\''))

def codontoAA(seq):
    codonlist=re.findall('..?.?',seq)
    codondictionary = {'UUU':'F','CUU':'L','AUU':'I','GUU':'V','UUC':'F','CUC':'L','AUC':'I','GUC':'V','UUA':'L','CUA':'L','AUA':'I','GUA':'V','UUG':'L','CUG':'L','AUG':'M','GUG':'V','UCU':'S','CCU':'P','ACU':'T','GCU':'A','UCC':'S','CCC':'P','ACC':'T','GCC':'A','UCA':'S','CCA':'P','ACA':'T','GCA':'A','UCG':'S','CCG':'P','ACG':'T','GCG':'A','UAU':'Y','CAU':'H','AAU':'N','GAU':'D','UAC':'Y','CAC':'H','AAC':'N','GAC':'D','UAA':'Stop','CAA':'Q','AAA':'K','GAA':'E','UAG':'Stop','CAG':'Q','AAG':'K','GAG':'E','UGU':'C','CGU':'R','AGU':'S','GGU':'G','UGC':'C','CGC':'R','AGC':'S','GGC':'G','UGA':'Stop','CGA':'R','AGA':'R','GGA':'G','UGG':'W','CGG':'R','AGG':'R','GGG':'G'}
    for n, key in enumerate(tuple(codonlist)):
        codonlist[n]=codondictionary[key]
    return ''.join(codonlist).replace('Stop','')

#print(codontoAA('AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA'))

with open('rosalind_prot.txt','r') as file:    
    RNAseq=file.read().strip('\n')
    fh=open('rosalind_prot_output.txt','w+')

    fh.write(codontoAA(RNAseq))

    fh.close()

'''
string = """UUU F      CUU L      AUU I      GUU V
UUC F      CUC L      AUC I      GUC V
UUA L      CUA L      AUA I      GUA V
UUG L      CUG L      AUG M      GUG V
UCU S      CCU P      ACU T      GCU A
UCC S      CCC P      ACC T      GCC A
UCA S      CCA P      ACA T      GCA A
UCG S      CCG P      ACG T      GCG A
UAU Y      CAU H      AAU N      GAU D
UAC Y      CAC H      AAC N      GAC D
UAA Stop   CAA Q      AAA K      GAA E
UAG Stop   CAG Q      AAG K      GAG E
UGU C      CGU R      AGU S      GGU G
UGC C      CGC R      AGC S      GGC G
UGA Stop   CGA R      AGA R      GGA G
UGG W      CGG R      AGG R      GGG G"""

coded = "AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"
decoded = ''

traL =  string.split()
traDict = dict(zip(traL[0::2], traL[1::2]))

for i in range(0, len(coded)-3, 3):
    decoded += traDict[coded[i:i+3]]

print decoded
'''
'''
codon_table = 'KNKNTTTTRSRSIIMIQHQHPPPPRRRRLLLLEDEDAAAAGGGGVVVV\0Y\0YSSSS\0CWCLFLF'
nucleo = {'A': 0, 'C': 1, 'G': 2, 'U': 3}

f = open('rosalind_prot.txt', 'r')
seq = f.read().rstrip()
f.close()

protein = []
for i in range(0, len(seq), 3):
    protein.append(codon_table[nucleo[seq[i]]*16 + nucleo[seq[i+1]]*4 + nucleo[seq[i+2]]])

print(''.join(protein[:-1]))
'''
