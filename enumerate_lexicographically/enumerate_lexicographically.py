'''
Problem
Assume that an alphabet A has a predetermined order; that is, we write the alphabet as a permutation A=(a1,a2,…,ak), where a1<a2<⋯<ak. For instance, the English alphabet is organized as (A,B,…,Z).

Given two strings s and t having the same length n, we say that s precedes t in the lexicographic order (and write s<Lext) if the first symbol s[j] that doesn't match t[j] satisfies sj<tj in A.

Given: A collection of at most 10 symbols defining an ordered alphabet, and a positive integer n (n≤10).

Return: All strings of length n that can be formed from the alphabet, ordered lexicographically (use the standard order of symbols in the English alphabet).

Sample Dataset
A C G T
2
Sample Output
AA
AC
AG
AT
CA
CC
CG
CT
GA
GC
GG
GT
TA
TC
TG
TT
'''

def enumerate_lexico(alphabet,length):
    kmer_list=['']
    for word in kmer_list:
        for letter in alphabet:
            kmer_list.append(word+letter)
        if len(max(kmer_list))==length:
            break
    return [kmer for kmer in kmer_list if len(kmer)==length]

def kmers(word, max_len, alphabet):
    if len(word)==max_len:
        print(word)
    else:
        for letter in alphabet:
            kmers(word+letter,max_len,alphabet)


alpha=['A','C','G','T']
N=2
empty_word=''
kmers(empty_word,N,alpha)

'''
with open('enumerate_lexicographically/rosalind_lexf.txt','r') as rfile:
    input=rfile.read().splitlines()
alph,leng=input[0].split(),int(input[1])
with open('enumerate_lexicographically/rosalind_lexf_result.txt','w+') as wfile:
    for kmer in enumerate_lexico(alph,leng):
        wfile.write(kmer+'\n')
'''

'''Try:
function f ( length , word )    .. (1)
        if length = N  then       .. (2)
            print the word and exit
         else
               for a = 1 to A
                      f(length + 1 , word + alphabet[a])  ..(3)
'''

##########USER_SOLUTIONS############
'''
import Control.Monad

k_mers k alphabet = replicateM k alphabet
'''
'''
for p in it.product(alphabet,repeat=n):
    print ''.join(p)

'''

'''
k = 2
str = 'P R Q Z U A S N J D'
alphabet = str.split()
k_mer = alphabet

for  l in range(k-1):
    k_mer =  [i+j for i in alphabet for j in k_mer]

for i in k_mer: print i
'''
