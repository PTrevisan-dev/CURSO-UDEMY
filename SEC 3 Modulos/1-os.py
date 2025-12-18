import os 

# 1- retornar a pasta atual
print(os.getcwd())

# 2- listar arquivos e pasta atual
print(os.listdir())

# 3- versao do SO 
os.system('ver')

# 4- configs da maquina 
os.system('sisteminfo')

# 5- limpar a tela do terminal 
os.system('cls')

# 6- desligar o computador 
os.system('shutdown /s') # desligar em um minuto ja e assim por padrao 
os.system('shutdown /s /t 0') # desligar imediato
os.system('shutdonw /a') # cancelar o desligamento

def turn_off_one_hour():
    os.system('shutdonw /s /t 3600')
def turn_off_half_hour():
    os.system('shutdonw s/ /t 1800')
def cancel_shutdonw():
    os.system('shutdown a/')

