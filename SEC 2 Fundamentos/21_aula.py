# usando parametros ARGS e KWARGS
'''
 *args - utilizando ele quando nao temso certezas de quantos arguments queremos ter numa funcao.
 - os argumentos sao passados como uma tupla
 *Kwargs - alem dos valores podemos passar tambem as respectivas chaves para cada argumento.
 - Os argumentos sao passados como um dicionario 
'''
# 1 - soma de numeros (o * no parametro faz com que receba um valor dinamico) ----- isso e um args
def sum(*num):
    sum_total = 0 
    for n in num:
        sum_total += n
    print(f'Soma e: {sum_total}')

sum(7)
sum(7,8)
sum(7,9,8)

# 2 - apresentacao de cursos 

def presentation(**data):
    for key, value in data.items():
        print(f'{key} - {value}')
print('Lista de cursos:')
presentation(name='Python', category='Bcakend', level='Iniciante')
presentation(name='Visao computacional com Python', category='IA', level='Avancado')
presentation(name='Dashboards com Dash', category='Bcakend', level='Intermediario')