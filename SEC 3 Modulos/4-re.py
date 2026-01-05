import re 

text = 'Udemy - uma plataforma com muitos cursos'

# 1 - indicie inicial e final de palavras 
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

