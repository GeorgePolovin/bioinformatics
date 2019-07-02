


with open('rosalind_rna.txt') as file:
	DNAsequence = file.read()
	RNAsequence = DNAsequence.replace('T','U')
	fh=open('rosalind_rna_output.txt', 'w+')
	
	fh.write(RNAsequence)
	
	fh.close()

#s = input()
#print(s.replace("T", "U"))
