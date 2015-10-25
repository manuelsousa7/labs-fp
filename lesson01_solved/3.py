print("Escreva um ano para eu dizer se e bissexto")
ano=int(input("Ano -> "))
if(ano % 4 == 0 and (ano % 400 == 0 or ano % 100 != 0)):
 print("O ano ", ano , " e bissexto")
else:
  print("O ano ", ano , " nao e bissexto")