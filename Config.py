#Libraries
import streamlit as st
import pandas as pd

#Load config
def Load_config():
    return pd.read_json('config.json', orient='index').sort_index()
 

#Write a File

def Write_config(DF):
    DF.to_json('config.json',orient='index',indent=4)


def load_table():
    st.title("Pagina de Configuração")

    st.table(data=Load_config())
    st.markdown('_______________________________')




def Add_config(UCD,Adress,Software,Type,DF_config):
    if UCD in DF_config.index:
        return st.error(f'{UCD} Já existe na Base de Dados')
        
    else:
        dict_ucd = {'':[UCD],'Adress':[Adress],'Type':[Type],'Software':[Software]}
        config = pd.concat([DF_config,pd.DataFrame.from_dict(data=dict_ucd).set_index('')])
        Write_config(config)
        st.experimental_rerun()
        
        

def remove_config(UCD, df_config):
    if UCD in df_config.index:
            config = df_config.drop(UCD)
            Write_config(config)
            st.experimental_rerun()
            
            
    else:
        return st.error(f'{UCD} Não encontrada')

def alter_config(UCD,Adress,Software,Type,df_config):
    if UCD in df_config.index:
        config = df_config.drop(UCD)
        Write_config(config)    
        dict_ucd = {'':[UCD],'Adress':[Adress],'Type':[Type],'Software':[Software]}
        config = pd.concat([config,pd.DataFrame.from_dict(data=dict_ucd).set_index('')])
        Write_config(config)  
        st.experimental_rerun()
    else:
        return st.error(f'{UCD} Não encontrada')
      
    
    



#Main loop
def main():

    
    load_table()

    c1,c2,c3,c4 = st.beta_columns(4)

    with c1:
        UCD = st.text_input('Nome Unidade')

    with c2:
        Adress = st.text_input('Endereço:Porta')
    
    with c3:
        Software = st.radio('Software', ('PyHMS','Dadas'))

    with c4:
        Type = st.radio('Tipo de Unidade', ('HMS','EPTA'))

   
    st.markdown('_______________________________')

    c1,c2,c3,cx,cx,cx,cx = st.beta_columns(7)
    with c1:
        if st.button('Inserir Unidade'):
            if UCD == '':
                st.error('Inserir nome da UCD')
            else:
                if Adress == '':
                    st.error('Inserir endereço e porta')
                else:                    
                    config = Load_config()
                    Add_config(UCD,Adress,Software,Type,config)
                    


    with c2:
        if st.button('Alterar Unidade'):
            if UCD == '':
                st.error('Inserir nome da UCD')
            else:
                if Adress == '':
                    st.error('Inserir endereço e porta')
                else:
                    config = Load_config()
                    alter_config(UCD,Adress,Software,Type,config)
                    
                    

    with c3:
        if st.button('Deletar Unidade'):
            if UCD == '':
                st.error('Inserir nome da UCD')
            else:
                config = Load_config()
                config = remove_config(UCD, config)
                
                








#if __name__ == "__main__":
    #main() 
