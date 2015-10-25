h=int(input("Introduza o numero de horas trabalhadas: "))
s=float(input("Introduza o salario recebido\\horas: "))
if(h<40):
    print("Salario: ",h*s)
else:
    print("Salario: ", s*2*(h-40)+s*40)
    