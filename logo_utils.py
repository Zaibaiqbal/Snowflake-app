

import streamlit as st

def add_logo():
    """
    Add logo to the sidebar, above multipage selection
    """
    st.sidebar.image("unnamed.png", width=250, use_column_width=True)
    st.sidebar.markdown(
        "<style>img{position:fixed;top:25px;}</style>", 
        unsafe_allow_html=True
    )
