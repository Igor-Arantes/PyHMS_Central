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

lista_df_unidade =[]
for i in range(len(df_unidades)):
    if df_unidades.iloc[i]['Type'] == 'HMS':
        df = DataAquisition.get_status_hms(df_unidades.iloc[i].name,df_unidades.iloc[i]['Adress'],DataAquisition.pre_get,DataAquisition.get_hms)
        lista_df_unidade.append(df.T)
    elif df_unidades.iloc[i]['Type'] == 'EPTA':
        #print('\n'+unidade+'EPTA:')
        df = (DataAquisition.get_status_hms(df_unidades.iloc[i].name,df_unidades.iloc[i]['Adress'],DataAquisition.pre_get,DataAquisition.get_hms))
        df.loc[['ptchupvok','heavprok','heavvlok','rollptvok']] = '--'
        lista_df_unidade.append(df.T)
    else:
        print(f"\n Error: Type {df_unidades.iloc[i]['Type']} not found")

Status_UCDS = pd.concat(lista_df_unidade)
print(Status_UCDS)
