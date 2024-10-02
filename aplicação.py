import csv
import time
import tkinter as tk
from tkinter import filedialog, messagebox
from pid_list import pid_list

file_path = ""

def select_file():
    global file_path
    file_path = filedialog.askopenfilename(
        title="Selecione o arquivo CSV",
        filetypes=[("CSV files", "*.csv")]
    )
    if file_path:
        file_label.config(text=f"Arquivo selecionado: {file_path.split('/')[-1]}")

def process_file():
    global file_path
    if not file_path:
        messagebox.showerror("Erro", "Selecione um arquivo CSV primeiro.")
        return
    
    #abrir arquivo
    with open(file_path, 'r') as arquivo:
        dataset = arquivo.readlines()

    if choice.get() == 1:
        pid = pid_var.get().upper()
        if pid in pid_list:
            filtrar_pid(dataset, pid)
        else:
            messagebox.showerror("Erro", "PID inválido.")
    elif choice.get() == 2:
        organize_data(dataset)
    else:
        messagebox.showerror("Erro", "Selecione uma opção válida.")

def filtrar_pid(dataset, pid):
    data = []
    new_csv = []
    pid = pid.strip().upper()  # Remover espaços e converter o PID digitado para maiúsculas
    for lin in dataset:
        campos = lin.strip().split(",")
        if len(campos) > 1 and campos[1].strip().upper() == pid:  # Comparar PIDs em maiúsculas e sem espaços
            data.append(lin.strip())
            new_csv.append(campos)

    ts = time.time()
    with open(f"PID_{pid}_{ts}.csv", 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerows(new_csv)

    messagebox.showinfo(f"Arquivo PID_{pid}_{ts}.csv criado com sucesso.")

#organizar todos os PIDs
def organize_data(dataset):
    new_csv = []
    header = ["timestamp?", "PID", "Data"]
    new_csv.append(header)

    for pid, description in pid_list.items():
        for lin in dataset:
            campos = lin.strip().split(",")
            if len(campos) > 1 and campos[1].strip().lower() == pid.lower():
                new_csv.append(campos)

    ts = time.time()
    name = f"PIDs_{ts}.csv"
    with open(name, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerows(new_csv)

    messagebox.showinfo(f"Arquivo {name} criado com sucesso.")

root = tk.Tk()
root.title("Abublé")
root.geometry("400x350")

choice = tk.IntVar()

select_file_btn = tk.Button(root, text="Selecionar arquivo CSV", command=select_file)
select_file_btn.pack(pady=10)

file_label = tk.Label(root, text="Nenhum arquivo selecionado.")
file_label.pack(pady=5)

radio_pid = tk.Radiobutton(root, text="Separar por PID", variable=choice, value=1)
radio_pid.pack()

pid_var = tk.StringVar()
pid_entry = tk.Entry(root, textvariable=pid_var)
pid_entry.pack(pady=5)

radio_organize = tk.Radiobutton(root, text="Organizar Planilha", variable=choice, value=2)
radio_organize.pack()

process_btn = tk.Button(root, text="Start", command=process_file)
process_btn.pack(pady=10)

root.mainloop()