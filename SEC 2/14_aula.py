# condicao 

# nome do filme
'''
name = input('digite o nome do filme:\n')
year_release = int(input('digite o ano de lançamento\n'))
rating = float(input('digite a nota do filme\n'))

# verificar se o filme e recomendado 

if rating > 8.0 and year_release >= 2015:
    print(f'O filme {name} é muito bom. Recomendo assistir')
else:
    print(f'O filme {name} ainda não atingiu nota boa, ou ano de lançamento recente')

'''

num = float(input('Digite seu numero:'))
num1 = float(input('Digite seu numero:'))
operation = input('Digite a operação a ser realizada : (+ - * /)\n')

if operation == '+':
    result = num + num1 
elif operation == '-':
    result = num - num1
elif operation == '*':
    result = num * num1
elif operation == '/':
    if num1 != 0:
        result = num / num1
    else:
        print('Erro: divisão por 0')

else:
    print('Operação invalida')
    result = 0 

print(f'O resultado da seguinte operação {num} {operation} {num1} é :\n {result:.5f}')


