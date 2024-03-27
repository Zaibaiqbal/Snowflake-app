import streamlit as st



from logo_utils import add_logo
add_logo()











from footer import generate_footer_html
from navbar import generate_header_html


header_html = generate_header_html()
st.markdown(header_html, unsafe_allow_html=True)


footer_html = generate_footer_html()
st.markdown(footer_html, unsafe_allow_html=True)