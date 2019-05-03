

def HammingDistance(s,t):
    count=0
    for i in range(min(len(s),len(t))):
        if s[i]!=t[i]:
            count+=1
        else:
            continue
    return count

with open('rosalind_hamm.txt','r') as file:
    sequences=file.read().splitlines()
    fh=open('rosalind_hamm_output.txt','w+')
    fh.write(str(HammingDistance(sequences[0],sequences[1])))
    fh.close()

#s='GAGCCTACTAACGGGAT'
#t='CATCGTAATGACGGCCT'

#print(HammingDistance(s,t))
