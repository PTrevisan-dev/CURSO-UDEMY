# exercicio 1.1 formatar nome e sobrenome

from ast import IfExp
nome = input('digite seu nome:\n')
sobrenome = input('digite seu sobrenome:\n')

nome_formatado = f'{nome} {sobrenome}'

print(nome_formatado.title())

# execicio 1.2 inverter um texto (::-1)

text = 'Natal e legal'

print(text[::-1])

# outra maneira 

palavras = text.split()
text_invert = ' '.join(palavras[::-1]) # precisa dar espaço no '' para ele separa quando for junter no join 
print(text_invert)

# palavras invertidas que são a mesma coisa 

texto1 = 'arara'
texto2 = 'python'

palavra_invertida1 = (texto1[::-1])
palavra_invertida2 = (texto2[::-1])

if texto1 == palavra_invertida1:
    print('abuela')
else:
    print('nt')

if palavra_invertida2 == texto2: 
    print('abuela')
else:
    print('nt')