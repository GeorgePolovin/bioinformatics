'''
Problem
A permutation of length n is an ordering of the positive integers {1,2,…,n}. For example, π=(5,3,2,1,4) is a permutation of length 5.

Given: A positive integer n≤7.

Return: The total number of permutations of length n, followed by a list of all such permutations (in any order).
Sample Dataset
3
Sample Output
6
1 2 3
1 3 2
2 1 3
2 3 1
3 1 2
3 2 1
'''
#Probability mass function f(k,n,p)=Pr(X=k)=(n,k)p**k(1-p)**(n-k), where (n,k)= n!/k!(n-k)!
# n is trails, k is successes, p is probability of success
#Cumulative distribution function F(k,n,p)=Pr(X<=k)=|k|:SUMMATION:i=0 (n,i)p**i(1-p)**(n-i), where (n,i)=n!/i!(n-i)!
# n is trails, k is successes, p is probability of success; can be reformulated for Pr(X>=k)
#Permutation P(n,k)=n!/(n-k)!
#Combination C(n,k)=n!/k!*(n-k)! AKA binomial coeffiient

def factorial(num):
    if num==0:
        return 1
    else:
        return num*factorial(num-1)

def gene_orders(gene_num):
    pass

def shift_list(perm_list):
    perm_list.append(perm_list.pop(0))
    return perm_list

def permutation(gene_num_list):
    #gene_num_list.index(max(gene_num_list))
    perm_list=[]
    for index,element in enumerate(gene_num_list):
        llist=gene_num_list[:index]
        rlist=gene_num_list[index:]
        for x in range(0,len(rlist)):
            rlist.append(rlist.pop(0))
            perm_list.append(llist+rlist)
    return perm_list

def permute(xs, low=0):
    if low + 1 >= len(xs):
        yield xs
    else:
        for p in permute(xs, low + 1):
            yield p
        for i in range(low + 1, len(xs)):
            xs[low], xs[i] = xs[i], xs[low]
            for p in permute(xs, low + 1):
                yield p
            xs[low], xs[i] = xs[i], xs[low]

def per(num_list):
    if not num_list:
        return [[]]
    else:
        list_of_permutes=[]
        for permute in per(num_list[:-1]):
            list_of_permutes+= [permute[:i] + num_list[-1:] + permute[i:]
                                    for i in range(0,len(permute)+1)]
        return list_of_permutes

with open('gene_orders/rosalind_perm.txt','r') as rfile:
    n=int(rfile.readlines()[0])
    result=per(list(range(1,n+1)))
    with open('gene_orders/rosalind_perm_result.txt','w+') as wfile:
        result_string=str(len(result))+'\n'
        for item in result:
            result_string+=str(item).strip('[]').replace(',',' ') +'\n'
        wfile.write(result_string)


#test=[1,2,3,4]
#print(permutation(test))
#for x in permute(test,):
    #print(x)
#print(per(test))





#########USER_SOLUTION########
'''
n=7

def permutations(l):
    return [ (m[:i] + [l[0]] + m[i:]) for m in permutations(l[1:]) for i in xrange(len(m)+1) ] if len(l)>1 else [l]

p = permutations(range(1,n+1))

print len(p)
for l in p:
    print ' '.join(map(str,l))
'''
