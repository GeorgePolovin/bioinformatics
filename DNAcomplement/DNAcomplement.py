
def reversecomplement(s):
	nucl_replace={'A':'T','T':'A','C':'G','G':'C'}
	revcom=''
	for nucl in s.strip('\n')[::-1]:
		revcom = revcom + nucl_replace[nucl]
	return revcom

with open('rosalind_revc.txt') as file:
	DNAsequence = file.read()
	fh=open('rosalind_revc_output.txt', 'w+')
	
	fh.write(reversecomplement(DNAsequence))
	
	fh.close()

#Look faster
#from string import maketrans
#s = 'AAAACCCGGT'
#print(s[::-1].translate(maketrans('ACGT', 'TGCA')))
#s = 'AAAACCCGGT'
#print(s[::-1].translate(str.maketrans('ACGT', 'TGCA')))

#loop for mulitple characters replacement, in successive order
#def replace_all(str, dict):
	#for i, j in dict.iteritems():
		#str = str.replace(i,j)
	#return str
	
#$ cat rosalind2.txt | tr 'ACGT' 'TGCA' | rev