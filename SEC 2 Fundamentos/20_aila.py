# funcao recursiva

'''
Fatorial de um numero:
1 -> 1 * 1 
2 -> 2 * 1 
3 -> 3 * 2 * 1

'''

def factorial(num):
    if num == 1:
        return 1
    else:
        return (num * factorial(num - 1))
number = int(input('Digite o numero para o fatorial:\n'))
print(f'O fatorial de {number} e {factorial(number)}')

'''
Vamos explicar mais ou menos como aconteceu 
nos demos o parametro num ou oque tenha la dentro caso esse num \ numero seja 1 vai ser 1 
mas quando nos colocamos o num fora de def podemos substituir o parametro no caso do num ele virou numero a conta vai trocar por numero tbm 
ao inves de num 
'''

# 2 - soma total de um numero 
def total_sum(num):
    if num == 1:
        return 1
    else:
        return (num + total_sum(num - 1))

num = int(input('Digite o numero da soma:\n'))
print(f'A soma total de {num} e {total_sum(num)}')

'''
Dessa vez foi a mesma coisa mas usei o num para assim ficar mais claro quando eu for ver 
ao inves de number como no factorial usei o num 
'''

