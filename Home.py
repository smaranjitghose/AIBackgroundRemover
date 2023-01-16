import streamlit as st
from utils import hide_footer, lottie_local

def main():
    """
    Main Function
    """
    st.set_page_config(
        page_title="AI Background Remover",
        page_icon="./assets/favicon.ico",
        layout= "centered",
        initial_sidebar_state="expanded",
        menu_items={
        'Get Help': 'https://github.com/smaranjitghose/AIBackgroundRemover',
        'Report a bug': "https://github.com/smaranjitghose/AIBackgroundRemover/issues",
        'About': "## A minimalistic application to remove image backgrounds built using Python"
        } )
    
    st.title("AI Background Remover")
    hide_footer()



if __name__ == "__main__":
    main()