'''
Problem

A DNA string is a reverse palindrome if it is equal to its reverse complement. For instance, GCATGC is a reverse palindrome because its reverse complement is GCATGC. See Figure 2.

Given: A DNA string of length at most 1 kbp in FASTA format.

Return: The position and length of every reverse palindrome in the string having length between 4 and 12. You may return these pairs in any order.

Sample Dataset
>Rosalind_24
TCAATGCATGCGGGTCTATATGCAT

Sample Output
4 6
5 4
6 6
7 4
17 4
18 4
20 6
21 4
'''

#function to take DNA sequence string and return the reverse complement
def DNAreverse_complement(seq):
    complement=str.maketrans('ATGCN','TACGN')
    return seq.translate(complement)[::-1]

def palindrome_pos_len(seq):
    result_tuples=[]
    for start in range(len(seq)):
        for end in range(start+4,len(seq)):
            if seq[start:end]==DNAreverse_complement(seq[start:end]):
                if len(seq[start:end])<=12:
                    result_tuples.append((start+1,end))
    return result_tuples

test='TCAATGCATGCGGGTCTATATGCAT'
print(palindrome_pos_len(test))
print(palindrome_pos_len(DNAreverse_complement(test)))
