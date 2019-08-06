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
        for end in range(start+4,len(seq)+1):
            if seq[start:end]==DNAreverse_complement(seq[start:end]):
                length=len(seq[start:end])
                if length<=12:
                    result_tuples.append((start+1,length))
    return result_tuples

def print_results(tuple_list):
    result_string=''
    for pair in tuple_list:
        result_string+=str(pair[0])+' '+str(pair[1])+'\n'
    return result_string

def loc_restric(rosalind_file):
    with open(rosalind_file, 'r') as rfile:
        sequence=''.join(rfile.read().splitlines()[1:])
    with open(rosalind_file+'_result.txt','w+') as wfile:
        wfile.write(print_results(palindrome_pos_len(sequence)))

loc_restric('restriction_sites/rosalind_revp.txt')


##########################USER_SOLUTIONS############################
def Problem09(): #Protein Translation
    file = open("./rosalind9.txt", "r")
    dna = file.read()
    for i in range(len(dna)):
        for j in range(4, 9):
            if i + j < len(dna) and dna[i:i + j] == reverse_complement(dna[i:i + j]):
                print i + 1, j
