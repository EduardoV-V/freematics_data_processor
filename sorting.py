import csv as csv
import time
from pid_list import pid_list
with open("1.CSV", 'r') as arquivo:
    dataset = arquivo.readlines()
    
def print_data(dataset,opt):
    data=[]
    new_csv=[]
    
    for lin in dataset:
        campos=lin.strip().split(",")
        if len(campos) > 1 and campos[1].strip().lower()==opt.lower():
            data.append(lin.strip())
            new_csv.append(campos)
            
    ts=time.time()
    with open(f"PID_{opt.upper()}_{ts}.csv", 'w', newline='') as file:
        writer=csv.writer(file)
        writer.writerows(new_csv)
    
    for lin in data:
        print(lin)
    
    data, lin, new_csv=None, [], []

print('\n PIDs disponíveis: ')
for pid, desc in pid_list.items():
    print(pid, ": ", desc)

opt=input('\n Digite o PID para ver os dados: ')
print_data(dataset,opt)