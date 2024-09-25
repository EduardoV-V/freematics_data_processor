import csv
import time
from pid_list import pid_list
from openpyxl import load_workbook

with open("1.CSV", 'r') as arquivo:
    dataset = arquivo.readlines()

def print_all_data(dataset):
    new_csv = []

    header = ["timestamp?", "PID", "Data"]
    new_csv.append(header)

    for pid, description in pid_list.items():
        for lin in dataset:
            campos = lin.strip().split(",")
            if len(campos) > 1:
                current_pid = campos[1].strip()
                if current_pid == pid:
                    new_csv.append(campos)

    ts = time.time()
    name = f"PIDs_{ts}.csv"
    
    with open(name, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerows(new_csv)
    return name

#print('\n PIDs disponíveis: ')
#for pid, desc in pid_list.items():
    #print(pid, ": ", desc)

print_all_data(dataset)