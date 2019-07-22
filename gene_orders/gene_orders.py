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

test=[1,2,3,4]
print(permutation(test))
#for x in permute(test,):
    #print(x)
