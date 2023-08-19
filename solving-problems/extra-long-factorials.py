def extraLongFactorials(n):
    print(f"{fatorial(n)}")
    
def fatorial(n):
    if n == 1:
        return 1
    
    return n * fatorial(n-1) 