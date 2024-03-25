import streamlit as st

#header
import streamlit as st
from navbar import generate_header_html
header_html = generate_header_html()
st.markdown(header_html, unsafe_allow_html=True)







st.write("")  # Empty line

st.write("")  # Empty line
st.write("")  # Empty line


st.write("Welcome.")

st.write("Satellite Data: Photographs and data captured by satellites offering insights into land, water, air, infrastructure and environmental changes")

st.write("IoT Data: Data Streams from interconnected devices and sensors, providing near real-time insights into various aspects of the physical world")

st.write("Mobility Data: Anonymized footfall data from smartphone sensors measuring human`s movements and surrounding interaction")







# footer
import streamlit as st
from footer import generate_footer_html
footer_html = generate_footer_html()
st.markdown(footer_html, unsafe_allow_html=True)