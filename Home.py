
#Libraries
import streamlit as st

#modules
import Central
import Config
import Tools_page
import Home


st.set_page_config(
page_title="SOP Tools",
page_icon="🧊",
layout="wide",
initial_sidebar_state="expanded"

)
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
            
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

def main():

    st.title("SOP Tools")

    st.text('Utilize o menu lateral para navegar entre as páginas')

    st.markdown("### Links úteis do Sistema Oceanop:")


    st.markdown('[OCN Tools](http://ocntools.petrobras.biz/)')
    st.markdown('[Portal Oceanop](http://portaloceanop.petrobras.biz/default.asp)')


    st.markdown('[CIEM 2.0](http://ciem2.petrobras.biz/)')    
    st.markdown('[Click](https://click.petrobras.com.br/)')

    










        

if __name__ == "__main__":
    PAGES = {
    "Home":Home,
    'Central': Central,
    "Config": Config,
    "Tools": Tools_page
        }
    st.sidebar.title('Navegação')
    selection = st.sidebar.radio("Ir para:", list(PAGES.keys()))
    page = PAGES[selection]
    page.main()
    #main() 

