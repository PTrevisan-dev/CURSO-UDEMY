#nao foi eu que fez essa bombba mas ta ai um exemplo basico de tkinter eu nao sei fazer isso ainda

import tkinter as tk
from tkinter import messagebox

# -----------------------------
# Janela principal
# -----------------------------
root = tk.Tk()
root.title("Lista de Tarefas")
root.geometry("420x500")
root.configure(bg="#1e1e2e")
root.resizable(False, False)

# -----------------------------
# Título
# -----------------------------
title = tk.Label(
    root,
    text="📝 Minhas Tarefas",
    font=("Segoe UI", 18, "bold"),
    bg="#1e1e2e",
    fg="#ffffff"
)
title.pack(pady=20)

# -----------------------------
# Frame de entrada
# -----------------------------
frame_entry = tk.Frame(root, bg="#1e1e2e")
frame_entry.pack(pady=10)

task_entry = tk.Entry(
    frame_entry,
    font=("Segoe UI", 12),
    width=25,
    bd=0
)
task_entry.pack(side=tk.LEFT, padx=10)

add_button = tk.Button(
    frame_entry,
    text="Adicionar",
    font=("Segoe UI", 10, "bold"),
    bg="#7aa2f7",
    fg="#000000",
    bd=0,
    padx=15,
    pady=5,
    cursor="hand2",
    command=lambda: add_task()
)
add_button.pack(side=tk.LEFT)

# -----------------------------
# Frame da lista
# -----------------------------
frame_list = tk.Frame(root, bg="#1e1e2e")
frame_list.pack(pady=20)

scrollbar = tk.Scrollbar(frame_list)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

task_list = tk.Listbox(
    frame_list,
    font=("Segoe UI", 12),
    width=40,
    height=12,
    yscrollcommand=scrollbar.set,
    bg="#2a2a40",
    fg="#ffffff",
    selectbackground="#7aa2f7",
    bd=0,
    highlightthickness=0
)
task_list.pack()

scrollbar.config(command=task_list.yview)

# -----------------------------
# Funções
# -----------------------------
def add_task():
    task = task_entry.get().strip()
    if task:
        task_list.insert(tk.END, f"✔ {task}")
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Aviso", "Digite uma tarefa!")

def remove_task():
    try:
        selected = task_list.curselection()
        task_list.delete(selected)
    except:
        messagebox.showwarning("Aviso", "Selecione uma tarefa!")

# -----------------------------
# Botão remover
# -----------------------------
remove_button = tk.Button(
    root,
    text="Remover tarefa selecionada",
    font=("Segoe UI", 10, "bold"),
    bg="#f7768e",
    fg="#000000",
    bd=0,
    padx=20,
    pady=8,
    cursor="hand2",
    command=remove_task
)
remove_button.pack(pady=10)

# -----------------------------
# Rodapé
# -----------------------------
footer = tk.Label(
    root,
    text="Feito com Tkinter 🐍",
    font=("Segoe UI", 9),
    bg="#1e1e2e",
    fg="#aaaaaa"
)
footer.pack(side=tk.BOTTOM, pady=10)

# -----------------------------
# Loop principal
# -----------------------------
root.mainloop()
