import os
num1 = input('Digite um numero: ')
num2 = input('Digite um numero: ')

num1_float = float(num1)
num2_float = float(num2)

opcao = input('Favor selecionar um sinal: ')
history = []

if opcao == '+':
    result = num1_float + num2_float
    print (result)
    result.append(history)
elif opcao == '-':
    result = num1_float - num2_float
    print (result)
    result.append(history)

elif opcao == '*':
    result = num1_float * num2_float
    print (result)
    result.append(history)

elif opcao == '/':
    result = num1_float / num2_float
    print(result)
    result.append(history)
else:
    print('Favor informar o sinal')


fra = input('Deseja ver o historico? ')
if opcao == 's':
        os.system('cls')

        if len(history) == 0:
            print('Lista vazia')

        for i, valor in enumerate(history):
            print(str(i+1), valor, sep=' - ')