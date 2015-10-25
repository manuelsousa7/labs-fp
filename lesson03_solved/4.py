def area_circulo(r):
    return r*r*3.14

def area_coroa(r1,r2):
    if r1>r2:
        return "Erro de Valores"
    return area_circulo(r1+r2)-area_circulo(r1)
    
r1=float(input("Raio 1: "))
r2=float(input("Raio 2: "))
print(area_coroa(r1,r2))

