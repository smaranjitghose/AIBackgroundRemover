import streamlit as st
from utils import hide_footer, lottie_local
from PIL import Image
from rembg import remove


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

    uploaded_img = st.file_uploader(label="Upload an image", type=["png","jpg","jpeg"],accept_multiple_files=False)

    if st.button("Generate"):
        # Load the input Image
        img = Image.open(uploaded_img)
        # Remove the Image Background
        res_img = remove(img)
        col1, col2 = st.columns([2,2],gap="large")
        with col1:
            st.markdown("### Input Image")
            st.image(img)
        with col2:
            st.markdown("### After Background Removal")
            st.image(res_img)



if __name__ == "__main__":
    main()