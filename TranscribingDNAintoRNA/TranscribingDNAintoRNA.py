

def txn(s):
	RNAs=''
	for nucleotide in s:
		if nucleotide=='T':
			RNAs = RNAs + 'U'
		else:
			RNAs = RNAs + nucleotide
	return RNAs

with open('rosalind_rna.txt') as file:
	DNAsequence = file.read()
	RNAsequence = txn(DNAsequence)
	fh=open('rosalind_rna_output.txt', 'w+')
	
	fh.write(RNAsequence)
	
	fh.close()
#Best Method


#s = input()
#print(s.replace("T", "U"))
