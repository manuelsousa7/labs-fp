def primos(n):
    n_raiz=int(n**(1/2))
    i=2
    a=0
    while i <= n_raiz:
        if(n%i==0):
            return False
        i+=1
    return True
        
"""
def crivo(n):
    np1 = n + 1
    s = list(range(np1)) 
    s[1] = 0
    sqrtn = int(round(n**0.5))
    for i in range(2, sqrtn + 1): 
        if s[i]:
            s[i*i: np1: i] = [0] * len(range(i*i, np1, i))
    return filtro(None, s)
"""
