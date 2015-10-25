inteiro = eval(input('Escreva um inteiro\n? '))
numero = 0
posisao = 1
while inteiro != 0:
    digito = inteiro % 10
    print(inteiro % 10)
    if digito % 2 != 0:
        numero = numero + digito * posisao
        posisao = posisao * 10
    inteiro = inteiro // 10
print(numero)