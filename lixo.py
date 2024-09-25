import pandas as pd
from pid_list import pid_list

def pid_cat(pid):
    return pid_list.get(pid, 'PID desconhecido')

def open_data(path):
    try:
        df=pd.read_csv(path, header=None)
        df
        if df.empty:
            print('Erro na leitura: arquivo incompatível')
            return None
        
        df[['xxx', 'pid', 'val']]=df[0].str.split(',', expand=True)
        df['pid']=df['pid'].str.strip()
        df['val']=df['val'].str.strip()
            
        df['pid_cat']=df['pid'].apply(lambda pid:pid_cat(pid))
        print(df)
        return df[['pid','val','pid_cat']]
    
    except:
        print('Erro ao processar o arquivo')
        return None

def return_data(df,pid_esc):
    try:
        print(df)
        pid_desc=pid_list.get(pid_esc)
        if pid_desc is None:
            print('PID inválido')
            return None
        
        pid_data=df[df['pid']==pid_esc]
        
        if pid_data.empty:
            print('nenhum dado encontrado')
        else:
            print('Exibindo valores do PID {pid_desc}')
            print(pid_data[['value']])
    except ValueError:
        print('Insira um PID válido')
        
######################################

path="1.CSV"

df_cataloged=open_data(path)
if df_cataloged is None:
    print("df_cataloged = none")
    
print('\n PIDs disponíveis: ')
for pid, desc in pid_list.items():
    print(pid, ": ", desc)

pid_esc=input('\n Digite o PID para ver os dados: ')
return_data(df_cataloged, pid_esc)