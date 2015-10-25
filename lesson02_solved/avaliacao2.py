saldo=float(input("Indique o seu salario: "))
juros=float(input("Indique a taxa de juro anual: "))
meses=int(input("Indique o numero de meses: "))

taxa=juros/100
ano= meses // 12

while ano !=0:
  saldo += saldo*taxa
  ano-=1

print ("Juro Composto ", saldo)
