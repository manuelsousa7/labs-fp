inteiro = eval(input('Escreva um inteiro\n? '))
num = 0
pos = 1
while inteiro != 0:
    dig = inteiro % 10
    print(inteiro % 10)
    if dig % 2 != 0:
        num = num + dig * pos
        pos = pos * 10
    inteiro = inteiro // 10
print(num)