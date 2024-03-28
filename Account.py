import streamlit as st

#header
import streamlit as st
from navbar import generate_header_html
header_html = generate_header_html()
st.markdown(header_html, unsafe_allow_html=True)




st.write("")  # Empty line

st.write("")  # Empty line
st.write("")  # Empty line
st.write("")  # Empty line


st.write("Account Settings")





# footer
import streamlit as st
from footer import generate_footer_html
footer_html = generate_footer_html()
st.markdown(footer_html, unsafe_allow_html=True)