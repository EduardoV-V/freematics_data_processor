from pid_list import pid_list

with open("1.CSV", 'r') as arquivo:
    dataset = arquivo.readlines()
    
def print_data(dataset,opt):
    data=[]
    
    for lin in dataset:
        campos=lin.strip().split(",")
        if len(campos) > 1 and campos[1].strip().lower()==opt.lower():
            data.append(lin.strip())
            
    for lin in data:
        print(lin)
    
    data, lin=None, []

print('\n PIDs disponíveis: ')
for pid, desc in pid_list.items():
    print(pid, ": ", desc)

opt=input('\n Digite o PID para ver os dados: ')
print_data(dataset,opt)