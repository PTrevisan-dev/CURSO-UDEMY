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