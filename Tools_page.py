#Libraries
import streamlit as st
import os
import base64
import ftpref


#Download Function

def get_binary_file_downloader_html(bin_file, file_label='File'):
    with open(bin_file, 'rb') as f:
        data = f.read()
    bin_str = base64.b64encode(data).decode()
    href = f'<a href="data:application/octet-stream;base64,{bin_str}" download="{os.path.basename(bin_file)}">Download {file_label}</a>'
    return href



def main():


    st.title("Softwares OCN")

    c1 , c2 = st.beta_columns(2)

    with c1:
        #PyHMS
        
        with st.beta_expander(label='PyHMS'):
            st.text('Padrão PyHMS')
            st.markdown(ftpref.pyhms, unsafe_allow_html=True)
        #Dadas
        with st.beta_expander(label='Dadas'):
            st.text('Instalação padrão do Dadas')
            st.markdown(ftpref.dadas, unsafe_allow_html=True)
    with c2:
        #PyHMS sem HMS
        with st.beta_expander(label='PyHMS - Somente com EPTA'):
            st.text('PyHMS sem a vizualização do HMS, somente EPTA')
            st.markdown(ftpref.pyhsm_epta, unsafe_allow_html=True)

        #Dadas Client
        with st.beta_expander(label='Dadas Client'):
            st.text('Dadas Client Padrão')
            st.markdown(ftpref.dadas_client, unsafe_allow_html=True)

    st.title("Download de Ferramentas")

    c1 , c2 = st.beta_columns(2)

    with c1:
        #Descompactador de GZ em Lote
        with st.beta_expander(label='Descompactador'):
            st.text('Descompactador de Arquivos gz em lote')
            st.markdown(get_binary_file_downloader_html('Tools\Descompactador\MyPrgComp.zip', 'Descompactador'), unsafe_allow_html=True)
        #Putty
        with st.beta_expander(label='Putty'):
            st.text('Leitor de portas serias e IP')
            st.markdown(get_binary_file_downloader_html('Tools\Putty\putty.exe', 'Putty'), unsafe_allow_html=True)
  
    with c2:
        #Sublime portable
        with st.beta_expander(label='Sublime'):
            st.text('Editor de textos')
            st.markdown(ftpref.sublime, unsafe_allow_html=True)
       #Gemeos
        with st.beta_expander(label='Gemeos'):
            st.text('Move arquivos')
            st.markdown(ftpref.gemeos, unsafe_allow_html=True)


    
if __name__ == "__main__":
    main() 