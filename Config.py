#Libraries
import streamlit as st
import pandas as pd
#Read Config


#Load config
def Load_config():
    return pd.read_json('config.json', orient='index').sort_index()
 

#Write a File

def Write_config(DF):
    DF.to_json('teste_config_json.json',orient='index',indent=4)



def check_same(UCD, DF):
    checked = False
    for i in DF.index:
        if i == UCD:
            checked = True
        else:
            checked = False
    return checked


def Add_config(UCD,Adress,Software,Type,DF_config):
    dict_ucd = {'':[UCD],'Adress':[Adress],'Type':[Type],'Software':[Software]}
    return pd.concat([DF_config,pd.DataFrame.from_dict(data=dict_ucd).set_index('')])

def remove_config(UCD, df_config):
    if check_same(UCD, df_config) == True:
        return df_config.drop('UCD')
    elif check_same(UCD, df_config) == False:
        return st.error(f'{UCD} Não encontrada')

def alter_config(UCD,Adress,Software,Type,DF_config):
    dfx = remove_config(UCD, DF_config)
    return Add_config(UCD,Adress,Software,Type,dfx)



#Main loop
def main():
    st.set_page_config(
        page_title="PyHMS Central - Config Page",
        page_icon="📡",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    st.title("Pagina de Configuração")

    st.table(data=Load_config())

    st.markdown('_______________________________')

    c1,c2,c3,c4 = st.beta_columns(4)

    with c1:
        st.text_input('Nome Unidade')

    with c2:
        st.text_input('Endereço:Porta')
    
    with c3:
        st.radio('Software', ('PyHMS','Dadas'))

    with c4:
        st.radio('Tipo de Unidade', ('HMS','EPTA'))

   
    st.markdown('_______________________________')

    c1,c2,c3,cx,cx,cx,cx = st.beta_columns(7)
    with c1:
        st.button('Inserir Unidade')

    with c2:
        if st.button('Alterar Unidade'):
            st.error('UCD Nao encontrada')

    with c3:
        st.button('Deletar Unidade')






if __name__ == "__main__":
    main() 
