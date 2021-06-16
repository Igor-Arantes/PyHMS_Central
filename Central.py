#Bibliotecas
import pandas as pd


#Modulos
import DataAquisition


#Function to read and organize the targets
def UpdateTargets():
    
    #Reading config file    
    try:
        df_unidades = pd.read_json('config.json', orient='index')
        #Ordering the targets
        df_unidades = df_unidades.sort_index()
        return df_unidades

    except:
        return print('Config File could not be read')







df_unidades = UpdateTargets()

for unidade in df_unidades.index:
    if df_unidades.loc[unidade]['Type'] == 'HMS':
        print('\n'+unidade+'HMS:')
        print(DataAquisition.get_status_hms(df_unidades.loc[unidade]['Adress'],DataAquisition.pre_get,DataAquisition.get_hms))
    elif df_unidades.loc[unidade]['Type'] == 'EPTA':
        print('\n'+unidade+'EPTA:')
        print(DataAquisition.get_status_hms(df_unidades.loc[unidade]['Adress'],DataAquisition.pre_get,DataAquisition.get_epta))
    else:
        print(f"\n Error: Type {df_unidades.loc[unidade]['Type']} not found")