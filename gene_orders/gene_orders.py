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

def s_perm(seq):
    if not seq:
        return [[]]
    else:
        new_items = []
        for index, item in enumerate(s_perm(seq[:-1])):
            print('item:'+str(item)+'  '+str(index))
            #if index % 2:
            x=1
            if x==1:
                # step up
                new_items += [item[:i] + seq[-1:] + item[i:]
                              for i in range(len(item) + 1)]
                print('items1:'+str([item[:i] + seq[-1:] + item[i:]
                              for i in range(len(item) + 1)]))
            '''
            else:
                # step down
                new_items += [item[:i] + seq[-1:] + item[i:]
                              for i in range(len(item), -1, -1)]
                print('items2:'+str([item[:i] + seq[-1:] + item[i:]
                              for i in range(len(item), -1, -1)]))
            '''
        return new_items

#Non-recursive JT-permutations
def s_perms(seq):
    items = [[]]
    for j in seq:
        print('j:'+str(j))
        new_items = []
        for index, item in enumerate(items):
            print('item:'+str(item)+'   '+str(index))
            x=1
            #if i % 2:
            if x==1:
                # step up
                new_items += [item[:i] + [j] + item[i:]
                              for i in range(len(item) + 1)]
                print('items:'+str([item[:i] + [j] + item[i:]
                              for i in range(len(item) + 1)]))
            '''
            else:
                # step down
                new_items += [item[:i] + [j] + item[i:]
                              for i in range(len(item), -1, -1)]
            '''
        items = new_items

    return items

def JT_perm(nums):
    if nums==[]:
        return [[]]

test=[1,2,3,4]
count=0
for x in s_perms(test):
    print(x)
    count+=1
print(count)
print(factorial(len(test)))
#print(s_perm(None))
#for x in permute(test):
    #print(x)

#for i, item in enumerate([[]]):
    #print(i, item)
    #print(x for x in [item[:i] + test[-1:] + item[i:]
                  #for i in range(len(item) + 1)])



############JT-algorithm_by_https://rosettacode.org/wiki/Permutations_by_swapping#####
'''
#python recursive
def s_permutations(seq):
    def s_perm(seq):
        if not seq:
            return [[]]
        else:
            new_items = []
            for i, item in enumerate(s_perm(seq[:-1])):
                if i % 2:
                    # step up
                    new_items += [item[:i] + seq[-1:] + item[i:]
                                  for i in range(len(item) + 1)]
                else:
                    # step down
                    new_items += [item[:i] + seq[-1:] + item[i:]
                                  for i in range(len(item), -1, -1)]
            return new_items

    return [(tuple(item), -1 if i % 2 else 1)
            for i, item in enumerate(s_perm(seq))]

#interative of recursive method
def s_permutations(seq):
    items = [[]]
    for j in seq:
        new_items = []
        for i, item in enumerate(items):
            if i % 2:
                # step up
                new_items += [item[:i] + [j] + item[i:]
                              for i in range(len(item) + 1)]
            else:
                # step down
                new_items += [item[:i] + [j] + item[i:]
                              for i in range(len(item), -1, -1)]
        items = new_items

    return [(tuple(item), -1 if i % 2 else 1)
            for i, item in enumerate(items)]

#original interative
from operator import itemgetter

DEBUG = False # like the built-in __debug__

def spermutations(n):
    """permutations by swapping. Yields: perm, sign"""
    sign = 1
    p = [[i, 0 if i == 0 else -1] # [num, direction]
         for i in range(n)]

    if DEBUG: print ' #', p
    yield tuple(pp[0] for pp in p), sign

    while any(pp[1] for pp in p): # moving
        i1, (n1, d1) = max(((i, pp) for i, pp in enumerate(p) if pp[1]),
                           key=itemgetter(1))
        sign *= -1
        if d1 == -1:
            # Swap down
            i2 = i1 - 1
            p[i1], p[i2] = p[i2], p[i1]
            # If this causes the chosen element to reach the First or last
            # position within the permutation, or if the next element in the
            # same direction is larger than the chosen element:
            if i2 == 0 or p[i2 - 1][0] > n1:
                # The direction of the chosen element is set to zero
                p[i2][1] = 0
        elif d1 == 1:
            # Swap up
            i2 = i1 + 1
            p[i1], p[i2] = p[i2], p[i1]
            # If this causes the chosen element to reach the first or Last
            # position within the permutation, or if the next element in the
            # same direction is larger than the chosen element:
            if i2 == n - 1 or p[i2 + 1][0] > n1:
                # The direction of the chosen element is set to zero
                p[i2][1] = 0
        if DEBUG: print ' #', p
        yield tuple(pp[0] for pp in p), sign

        for i3, pp in enumerate(p):
            n3, d3 = pp
            if n3 > n1:
                pp[1] = 1 if i3 < i2 else -1
                if DEBUG: print ' # Set Moving'


if __name__ == '__main__':
    from itertools import permutations

    for n in (3, 4):
        print '\nPermutations and sign of %i items' % n
        sp = set()
        for i in spermutations(n):
            sp.add(i[0])
            print('Perm: %r Sign: %2i' % i)
            #if DEBUG: raw_input('?')
        # Test
        p = set(permutations(range(n)))
        assert sp == p, 'Two methods of generating permutations do not agree'
'''
