import re 

text = 'Udemy - uma plataforma com muitos cursos'

# 1 indicie inicial e final de palavras 
# O r siginifica uma raw string (string bruta)

match = re.search(r'muitos cursos', text)
print(f'Indice inicial: {match.start()}')
print(f'Indice final: {match.end()}')

# 2 buscando o indicie que possui o ponto 
site = 'https://udemy.com'
match = re.search(r'\.', site)
print(match)

# 3 buscnado uma lista de caracteres dentro de uma frase 
pattern = '[a-m]'
result = re.findall(pattern, text)
print(result)

# 4 verificnaod o inicio de uma string 
rule = r'^A'
phrase = ['A casa esta suja', 'O dia esrta lindo', 'vamos passear']
for f in phrase:
    if re.match(rule, f):
        print(f'Correspondente: {f}')
    else:
        print(f'Nao Correspondente: {f}')
'''
desse jeito nos podemos fazer sem precisar de modulo e muito mais simples usando qual letra como parametro 

for f in phrases:
    if f and f[0].isupper():
        print(f'Correspondente: {f}')
    else:
        print(f'Nao Correspondente: {f}')
'''

# 5 verificar o final de uma string 
rule_end = r'!$'
phrase2 = 'o dia esta lindo!'
match = re.search(rule_end, phrase2)
if match:
    print('sim, corresponde')
else:
    print('Nao corresponde')