

def Fibonacci(n,k):
    F1=0
    F2=1
    if n==0:
        return F1
    elif n==1:
        return F2
    else:
        for i in range(1,n):
            Fib=F2 + k*F1
            F1=F2
            F2=Fib
        return Fib

print(Fibonacci(50,3))

with open('Fibonacci/rosalind_fib.txt', 'r') as file:
    value=list(map(int,file.read().split()))

    fh=open('Fiboancci/rosalind_fib_output.txt','w+')

    fh.write(str(Fibonacci(value[0],value[1])))

    fh.close()
