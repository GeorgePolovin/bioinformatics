def ProbDominant(k,m,n):
    k=float(k)
    m=float(m)
    n=float(n)
    f=k+m+n
    s=k+m+n-1
    return ((k/f)*((k-1)/s))+((k/f)*(m/s))+((k/f)*(n/s))+((m/f)*(k/s))+((m/f)*(3/4)*((m-1)/s))+((m/f)*(1/2)*(n/s))+((n/f)*(k/s))+((n/f)*(1/2)*(m/s))

print(ProbDominant(28,17,20))


#kk km kn mk mm mn nk nm nn

#def firstLaw(k,m,n):
#    N = float(k+m+n)
#    return 1 - ( m*n + .25*m*(m-1) + n*(n-1) ) / ( N*(N-1) )

#using the complementary probability of getting no dominant alleles. The terms in the sum correspond to the choice of the mating partners: from the subpopulation with recessive alleles only, one from the mixed and one from recessive only (counted twice, but only 50% of the offspring are homozygous), both from mixed (only 25% of the offspring are homozygous).
