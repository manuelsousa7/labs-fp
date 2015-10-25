x=str(input("Escreva um inteiro: "))
t=len(x)-1
s=0
m=0
while t>=0:
    if(int(x[t])==0):
        s+=1
    else:
        if(s>m):
            m=s
            s=0
    t-=1
print("O numero tem ", m, " zeros seguidos")
    
    
