#Libraries
from numpy.core.fromnumeric import size
import streamlit as st
import pandas as pd


#modules



UCD = pd.read_json('config.json', orient='index').sort_index().index

def create_panel(UCD):
    
    for i in range(len(UCD)):
        with st.beta_expander(UCD[i]):
            form = st.form(key=UCD[i]) 
            c1, c2 = st.beta_columns(2)
            with c1:                       
                form.file_uploader('Miros:',type=['txt'],accept_multiple_files=False)
                form.text('Arquivo atual')
                
            with c2:
                form.file_uploader('PyHMS, Sismo ou Dadas',type=['txt','in','zip','ini'],accept_multiple_files=True)
                form.text('Arquivo atual')
            form.form_submit_button('Enviar')















def main():


    st.title("Central de Backups")
    create_panel(UCD)

    #st.beta_container()
    #col1, col2 = st.beta_columns(2)
    #col1.subheader('Columnisation')
    #st.beta_expander('Expander')
    #with st.beta_expander('Expand'):
     #   st.write('Juicy deets')




if __name__ == "__main__":
    main() 