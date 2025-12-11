# praticando oq eu ja aprendi 

animelist1 = []


def animeList():
    
    while True:
        anime =  input(f'Digite seu anime aqui quando terminar pode digite sair \n').strip()
        if anime.lower() == 'sair':
            menu()
        if anime:
            animelist1.append(anime)

    return animelist1 

def animeFilter():
    global animelist1

    print('---------DIGITE A LETRA OU DIGITE "sair" PARA VOLTAR---------')

    while True:
        letra = input('> ').lower()

        if letra == 'sair':
            menu()     
             

    
        filtrados = [anime for anime in animelist1 if anime[0].lower() == letra]

        print(filtrados)
    return filtrados



def menu():
    while True:
        print('----------BEM VINDO AO MENU DO SEU APP DE CONTROLES DE ANIMES----------')
        print(f'Digite a baixo do menu qual pagina você quer acessar\n'
            f'1° Adicionar anime assistido\n'
            f'2° Procurar pela primeira letra do nome\n'
            f'3° Sair')
        search = input('>')
        
        if search == '1':
            animeList()
        elif search == '2':
            animeFilter()
        elif search.lower() == '3':
            print('saindo.......')
            return
            
        
menu()
