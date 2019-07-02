
from operator import ne

with open("rosalind_hamm.txt", 'r') as file:
    #print (sum(map(ne, *file.read().split())))
    print(*file.read().split())

'''
s1 = 'GAGCCTACTAACGGGAT'
s2 = 'CATCGTAATGACGGCCT'
print [ a!=b for (a, b) in zip(s1, s2)].count(True)
'''
