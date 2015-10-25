def bissexto(ano):
    if(ano % 4 == 0 and (ano % 400 == 0 or ano % 100 != 0)):
        return True
    return False
    
ano=int(input("Ano: "))
print(bissexto(ano))

