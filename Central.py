#Libraries
import pandas as pd
import streamlit as st


#Modules
import DataAquisition
import DfManipulation
import Central
import Config


st.set_page_config(
page_title="PyHMS Central",
page_icon="🧊",
layout="wide",
initial_sidebar_state="collapsed"

)
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
            
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 




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



#Main loop
def main():


    st.title("Status UCDs PYHMS")
    
    st.table(data=Get_table_UCDS())
    st.button('Atualizar status')
    





if __name__ == "__main__":
    PAGES = {
    "Central": Central,
    "Config": Config
    }
    st.sidebar.title('Navegação')
    selection = st.sidebar.radio("Ir para:", list(PAGES.keys()))
    page = PAGES[selection]
    page.main()
