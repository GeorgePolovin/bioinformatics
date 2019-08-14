'''
Problem
A subsequence of a permutation is a collection of elements of the permutation in the order that they appear. For example, (5, 3, 4) is a subsequence of (5, 1, 3, 4, 2).

A subsequence is increasing if the elements of the subsequence increase, and decreasing if the elements decrease. For example, given the permutation (8, 2, 1, 6, 5, 7, 4, 3, 9), an increasing subsequence is (2, 6, 7, 9), and a decreasing subsequence is (8, 6, 5, 4, 3). You may verify that these two subsequences are as long as possible.

Given: A positive integer n≤10000 followed by a permutation π of length n.

Return: A longest increasing subsequence of π, followed by a longest decreasing subsequence of π.

Sample Dataset
5
5 1 4 2 3
Sample Output
1 2 3
5 4 2
'''

def inc_dec_subseq(subseq):
    inc=[]
    dec=[]
    for index, cur_num in enumerate(subseq):
        cur_inc=[cur_num]
        cur_dec=[cur_num]
        for num in subseq[index+1:]:
            if num>cur_num:
                cur_inc.append(cur_num)
            if num<cur_num:
                cur_dec.append(cur_num)
            else:
                continue
        print(cur_inc)
        #inc.append(cur_inc)
        #dec.append(cur_dec)
    #return inc, dec

test=[5,1,4,2,3]
print(inc_dec_subseq(test))