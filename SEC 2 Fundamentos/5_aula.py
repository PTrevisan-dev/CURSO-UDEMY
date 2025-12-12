#ul=tilizaçãp de str

movieName = 'Top Gun'
movieName2 = 'top gun'
print(movieName == movieName2) # python é case snsitive que significa que ele  pegga a diferanca de maiusc e minusc


# usar a str multi linha é da mesma maneira que comentamos multi linha 
movieDescription = '''
 Top Gun Maverick é im filme de aviação e aventura 
muito consagrado na industria '''

#ctrl + x apaga a linha !!!!!!!!!!!!!!!!!!!!!!!!!
print(movieName)
# 1- multiplicação de str
line = '='
print(line*60)
print(movieDescription)

# 2- procurar palavra dentra do texto 
print('top' in movieName)
print('Top' in movieName)
print('aviação' in movieDescription)
