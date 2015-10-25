def arctg(x,n):
    a=0
    while n>=0:
        a+=((((-1)**n)*(x**(2*n+1)))/(2*n+1))
        n-=1
    return a
    
x=int(input("X: "))
n=int(input("N: "))
print(arctg(x,n))


