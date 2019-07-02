'''
def mortal_fibonacci(n,k,m):
    fibseq=[0,1]
    if n==0:
        return fibseq[-2]
    elif n==1:
        return fibseq[-1]
    else:
        for i in range(1,n):
            if m>=i:
                Fib=fibseq[-1]+k*fibseq[-2]
            else:
                Fib=fibseq[-1]+k*fibseq[-2]-fibseq[-(m+1)]
            fibseq.append(Fib)
    return fibseq
'''

def mortal_fibonacci(n,k,m):
    youngfibseq=[0,1]
    maturefibseq=[0,0]
    fibseq=[0]
    if n==0:
        return youngfibseq[-2]
    elif m==0:
        for i in range(1,n+1):
            fibseq.append(0)
    else:
        for i in range(2,n+1):
            if m>i:
                maturefibseq.append(youngfibseq[-1]+maturefibseq[-1])
            else:
                maturefibseq.append(youngfibseq[-1]+maturefibseq[-1]-youngfibseq[(i-m)])
            youngfibseq.append(k*maturefibseq[-2])
        fibseq= fibseq+[sum(x) for x in zip(youngfibseq[1:],maturefibseq[1:])]
    return 'youngfibseq='+str(youngfibseq), 'maturefibseq='+str(maturefibseq), 'fibseq='+str(fibseq)
    #return fibseq[-1]

'''
def mortal_fibonacci(n,m):
    if n>m+1:
        return fibonacci(n,1)-2*fibonacci(n-m,1)
    else:
        return fibonacci(n,1)
'''

print(mortal_fibonacci(13,1,4))


with open('Fibonacci/rosalind_fibd.txt', 'r') as file:
    values=list(map(int,file.read().split()))

    fh=open('Fibonacci/rosalind_fibd_output.txt','w+')

    fh.write(str(mortal_fibonacci(values[0],1,values[1])))

    fh.close()
'''
#!/usr/bin/env python
def fib(n,k=1):
  ages = [1] + [0]*(k-1)
  for i in xrange(n-1):
    ages = [sum(ages[1:])] + ages[:-1]
  return sum(ages)
  '''
