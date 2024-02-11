
cashe={}

def caching_fibonacci(n):
    
    def fibo(n):
        if n<=0 :
            return 0
        elif n == 1 :
            return 1
        else:
            return fibo (n-1) + fibo(n-2)
    if n in cashe:
        return cashe.get(n)
    else:
        cashe[n]= fibo(n)       
    return cashe.get(n)

print(caching_fibonacci(10))

print(cashe)

print(caching_fibonacci(5))

print(caching_fibonacci(14))

print(caching_fibonacci(2))

print(caching_fibonacci(10))

print(cashe)


