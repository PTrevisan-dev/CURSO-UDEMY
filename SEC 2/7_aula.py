movie = 'top gun'
movieDescription = '''
 Top Gun Maverick é im filme de aviação e aventura 
muito consagrado na industria '''

print(movie.upper())
print(movie.lower())
print(movie.capitalize()) # deixa apenas a primeira letra em maiusculo 
print(movie.title()) # deixa como um titulo mesmo e primeira e segunda letra em maiusculo 
print(movie.center(9, '-')) # retorna a str centralizada com caractere de preenchimento 
print(movie.find('u')) # retorna o indice do caractere que vc procura 
print(movie.replace('top', 'Top')) # troca as palavras 
print(movieDescription.split(','))   
print(movie.split(','))

