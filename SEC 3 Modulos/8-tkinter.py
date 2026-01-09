import tkinter as tk

# 1 criando a nossa janela 
window = tk.Tk()
window.geometry('300x150')
window.title('gerenciador de fases')

# 2 adicionar um frame 
frame = tk.Frame(window)
frame.pack(padx=10, pady=10, fill='x', expand=True)

# 3 adicionar um label 
label = tk.Label(frame, text='DILDO')
label.pack(fill='x', expand=True)

# 4 adicionar o input text 
frase_lab = tk.Label(frame, text='Frase')
frase_lab.pack(fill='X', expand=True)

frase_inp = tk.Entry(frame)
frase_inp.pack(fill='X', expand=True)

# 5 funcao para elternar o texto do label 
def click():
    label.config(text=frase_inp.get())

# 6 adicionar um botao 
button = tk.Button(frame, text="enviar")
button.pack()

# GIT IDIOTA BRECANDO DNV


print('Eu git lixo')

window.mainloop()