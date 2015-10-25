def bissexto(ano):
    if(ano % 4 == 0 and (ano % 400 == 0 or ano % 100 != 0)):
        return True
    return False
    

def dias_mes(ano):
    if(len(ano)=='fev'):
        return ValueError("Nao tem 3 caracteres")
    return 
    
mes=str(input("Mes: "))
print(dias_mes(mes))