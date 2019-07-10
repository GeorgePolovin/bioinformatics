'''
Given: Two positive integers k (k≤7) and N (N≤2k). In this problem, we begin with Tom, who in the 0th generation has genotype Aa Bb.
Tom has two children in the 1st generation, each of whom has two children, and so on. Each organism always mates with an organism having genotype Aa Bb.

Return: The probability that at least N Aa Bb organisms will belong to the k-th generation of Tom's family tree (don't count the Aa Bb mates at each level).
Assume that Mendel's second law holds for the factors.

Sample Dataset
2 1
Sample Output
0.684
'''
#AaBa probability is always 1/4; need to find way to calculate 'binomial distribution'; find probs from N to total
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

def prob_mass_func(success,trials,probability):
    binomial_coefficient=factorial(trials)/(factorial(success)*factorial(trials-success))
    return binomial_coefficient*(probability**success)*((1-probability)**(trials-success))

def hetero_prob_min(gen,min_num):
    total_offspring=2**gen
    prob_hetero=0
    for prob_mass in range(min_num,total_offspring+1):
        prob_hetero=prob_hetero+prob_mass_func(prob_mass,total_offspring,1/4)
    return prob_hetero

def import_numbers(data_filename):
    with open(data_filename,'r') as file:
        data_list=file.read().split(' ')
    return data_list[0], data_list[1].strip('\n')

def write_to_txt(result_filename, data_string):
    with open(result_filename,'w+') as fh:
        fh.write(data_string)

given_data=import_numbers('independent_alleles/independent_alleles.txt')
result=hetero_prob_min(int(given_data[0]),int(given_data[1]))
write_to_txt('independent_alleles/independent_alleles_result.txt',str(result))


############################USER_SOLUTIONS#########################
from operator import mul
from math import factorial as fact

# faster and less likely to overflow than just taking factorials
# -- better solutions available at:
#       http://stackoverflow.com/questions/2096573/counting-combinations-and-permutations-efficiently
#       http://stackoverflow.com/questions/3025162/statistics-combinations-in-python
def choose(n, x):
    '''
    Returns the integer value for n choose x.
    '''
    if x in (0, n):
        return 1
    if x > n / 2:
        return reduce(mul, xrange(x + 1, n + 1)) / fact(n - x)
    else:
        return reduce(mul, xrange(n - x + 1, n + 1)) / fact(x)

def dbinom(n, p, x):
    '''
    Calculates the probability of getting x events with probability p in n trials.

    n = size of population
    p = prob of event
    x = number of events
    '''
    return choose(n, x) * p ** x * (1 - p) ** (n - x)

def pbinom(n, p, x):
    '''
    Calculates the cumulative binomial probability for X < x.

    n = size of population
    p = prob of event
    x = number of events
    '''
    return sum(dbinom(n, p, value) for value in xrange(x))
'''
with open('rosalind_lia.txt', 'r') as infile:
    (k, N) = (int(value) for value in infile.readline().split())

print 1 - pbinom(2 ** k, 0.25, N)
'''
