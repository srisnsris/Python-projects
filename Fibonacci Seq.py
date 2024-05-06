def fib(n):
    if n==1 or n==2:  #(n-1)+(n-2)
        return 1
    else:
        return(fib(n-1)+fib(n-2))
print(fib(5))


def fibonacci(n):
    a = 0
    b = 1
    for i in range(0 , n):   #2 or 3
        temp = a
        a = b
        b = temp + a
    return a
nterms = int(input("Howmany terms:"))
for c in range(0 , nterms):
    print(fibonacci(c) , end = " ")  
    
    
def fibo(n):
    
    a = 0
    b = 1
    if n ==1:    #n==1 orn==2  
        print(a)
    
    else:
        print(a)
        print(b)
    
    for i in range(2,n):
        c = a + b
        a = b
        b = c
        print(c)
fibo(5)