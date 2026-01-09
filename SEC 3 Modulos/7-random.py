import random as rd

# 1 selecionar valor aleatorio de uma lista 
list1 = [7, 4, 5, 3, 8, 9, 10, 1, 2]
print(rd.choice(list1))

# 2 gerar valores aleatorios em um intervalo de valores 
r1 = rd.randint(7, 777)
print(r1)

# 3 selecionar um caractere aleatorio de uma string 
name = 'curso python'
r2 = rd.choice(name)
print(r2)

# 4 selecionar mais de um valor aleatorio 
# random.sample(sequencia, tamanho)
print(rd.sample(list1, 2))
print(rd.sample(list1, 7))
s = 'ola'
print(rd.sample(s, 2))

# 5 programa de sorteio 

done = False
while not done:
    print('O que voce deseja fazer ?')
    print('1. Adivinhar o numero')
    print('2.Sair')

    choice = input('>')
    if choice == '1':
        print('=================Adivinhe um numero de 1 a 10=================')
        number = int('Digite um numeor de 1 a 10:\n')
        result = rd.randint(1, 10)
        if number == result:
            print('Prabens vc e um heroi !!!!!!')
        else:
            print(f'Tente novamente o numero sorteado foi {result}')   
    elif choice == '2':
        done = True
    else:
        print('Opcao invalida ------------------ Escolha 1 ou 2')
    
