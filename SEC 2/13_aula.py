import pprint

filmdict = {
    'inception':{
         'yearrelease': 2010,
        'imdbrating': 8.8,
        'genere': ['Sci-fi', 'action', 'thriller']     
    },
    'interstellar':{
         'yearrelease': 2014,
        'imdbrating': 8.6,
        'genere': ['Sci-fi', 'Drama']   
    },
    'the dark knight':{
        'yearrelease': 2008,
        'imdbrating': 9.0,
        'genere': ['Action', 'Drama', 'Crime']
    }
}
pp = pprint.PrettyPrinter(depth=4)
pp.pprint(filmdict)

# 1 - buscar info dentro de um dicionario aninhado 
print(filmdict['interstellar']['genere'])

# 2 - adicionoar novo item 
filmdict['inception']['director'] = 'Christopher Nolan'

# 3 - excluir itens 
del filmdict['the dark knight']
pp.pprint(filmdict)