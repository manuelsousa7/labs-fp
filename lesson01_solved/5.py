x=str(input("Escreva um numero: "))
t=0
s=""
print("Resultado: ")
while t<len(x):
    if(int(x[t])!=2 and int(x[t])!=4 and int(x[t])!=6 and int(x[t])!=8 and int(x[t])!=0):
        s+=x[t]
    t+=1
print(s)
    
    
