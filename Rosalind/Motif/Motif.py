
def FindMotif(s,t):
    output=[]
    if t not in s:
        print('match not found')
    while t in s:
        index=s.index(t)+1
        if output==[]:
            output.append(index)
        else:
            output.append(output[-1]+index)
        s=s[index:]
    return ' '.join(str(item) for item in output)


with open('rosalind_subs.txt','r') as file:
    seq, tar = file.read().splitlines()
    fh = open('rosalind_subs_output.txt','w+')

    fh.write(FindMotif(seq,tar))

    fh.close()

    print(FindMotif(seq,tar))
    
'''
s1,s2 = open('rosalind_subs.txt').read().split('\r\n')

for i in range(len(s1)):
    if s1[i:].startswith(s2):
        print(i+1)
'''
