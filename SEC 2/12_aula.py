filmInception = {
    'title': 'inception',
    'yearrelease': 2010,
    'imdbrating': 8.8,
    'genere': ['Sci-fi', 'action', 'thriller']        
}

print(filmInception)
print(len(filmInception))
print(type(filmInception))

# 1 - recuperar o elemento do dicionario 
print(filmInception['genere'])
print(filmInception.get('imdbrating'))

# 2 - buscar apenas as chaves do dicionario 
print(filmInception.keys())

# 3 - buascar apenas valores do dicionario 
print(filmInception.values())

# 4 - buscar itens do dicionario com chave e valor 
print(filmInception.items())

# 5 - adicionar itens ao dicionario 
filmInception['director'] = 'Christopher Nolan'
print(filmInception)

# 6 - atualizar itens no dicionario 
filmInception.update({'imdbrating': 8.7})
print(filmInception)

# 7 - remover item no dicionario 
filmInception.pop('director')
print(filmInception)

