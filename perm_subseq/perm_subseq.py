'''
Problem
A subsequence of a permutation is a collection of elements of the permutation in the order that they appear. For example, (5, 3, 4) is a subsequence of (5, 1, 3, 4, 2).

A subsequence is increasing if the elements of the subsequence increase, and decreasing if the elements decrease. For example, given the permutation (8, 2, 1, 6, 5, 7, 4, 3, 9),
an increasing subsequence is (2, 6, 7, 9), and a decreasing subsequence is (8, 6, 5, 4, 3). You may verify that these two subsequences are as long as possible.

Given: A positive integer n≤10000 followed by a permutation π of length n.

Return: A longest increasing subsequence of π, followed by a longest decreasing subsequence of π.

Sample Dataset
5
5 1 4 2 3
Sample Output
1 2 3
5 4 2
'''

import sys
import math

def inc_dec_subseq(subseq):
    inc=[]
    #dec=[]
    for index, cur_num in enumerate(subseq):
        cur_inc=[cur_num]
        #cur_dec=[cur_num]
        for num in subseq[index+1:]:
            if num>cur_num:
                cur_inc.append(num)
            #if num<cur_num:
                #cur_dec.append(num)
            else:
                continue
        inc.append(cur_inc)
        #dec.append(cur_dec)
    return inc

def inc_subset(set):
    N=len(set)
    index=[0*x for x in range(N)]
    predecessor=[0*x for x in range(N+1)]
    L=0
    for i in range(N-1):
        lo=1
        hi=L
        while lo<=hi:
            mid=math.ceil((lo+hi)/2)
            if set[predecessor[mid]]<=set[i]:
                lo=mid+1
            else:
                hi=mid-1
        newL=lo
        predecessor[i]=index[newL-1]
        index[newL]=i
        if newL>L:
            L=newL
    S=[0*x for x in range(L)]
    k=index[L]
    for i in range(L-1,0,-1):
        S[i]=set[k]
        k=predecessor[k]
    return S


def subset(set,index,set_len,prev_num=-sys.maxsize-1):
    if index==set_len:
        return 0
    excl=subset(set,index+1,set_len,prev_num)
    incl=0
    if set[index]>prev_num:
        incl=1+subset(set,index+1,set_len,set[index])
    return max(incl,excl)


test=[5,1,4,11,12,13,24,2,3,6,7,8,9]
print(inc_subset(test))




#https://www.techiedelight.com/longest-increasing-subsequence-using-dynamic-programming/
