#Bibliotecas
import pandas as pd
import streamlit as st


#Modulos
import DataAquisition
import DfManipulation



#
def main():
    st.set_page_config(
        page_title="PyHMS Central",
        page_icon="🧊",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    st.title("Status UCDs PYHMS")

    st.table(data=Get_table_UCDS())







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




#Function to get the list of Dataframes od all UCDs Status
def Status_all_ucds(df_unidades):
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
            print(f"\n Error: Type {df_unidades.iloc[i]['Type']} not found for UCD: {df_unidades.iloc[i].name}")
    return lista_df_unidade



def Get_table_UCDS():
    df_unidades = UpdateTargets()
    Status_UCDS = pd.concat(Status_all_ucds(df_unidades))
    Status_UCDS = DfManipulation.rename_columns(Status_UCDS,DfManipulation.dict_columns)
    Status_UCDS = DfManipulation.reorder_columns(Status_UCDS,DfManipulation.columns_order)
    Status_UCDS = DfManipulation.status_rename(Status_UCDS,DfManipulation.dict_status)
    Status_UCDS = DfManipulation.coloring(Status_UCDS)

    return(Status_UCDS)



if __name__ == "__main__":
    main() 
