
import snowflake.connector as sf
import streamlit as st
import pandas as pd
import os
import numpy as np
import pydeck as pdk
from PIL import Image
from tempfile import NamedTemporaryFile
from footer import generate_footer_html
from navbar import generate_header_html
from streamlit.components.v1 import components
import json
from logo_utils import add_logo


conn_param = {
    "user":'AliTahir',
    "password":'TestSnowFlake123-',
    "account":'YLQGJGX-GF89364',
    "warehouse":'COMPUTE_WH',
  
}


connection = sf.connect(
    user='AliTahir',
    password='TestSnowFlake123-',
    account='YLQGJGX-GF89364',
    warehouse='COMPUTE_WH',
  
)

st.set_page_config(
    page_title="User App",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

cursor = connection.cursor()
cursor.execute("USE WAREHOUSE COMPUTE_WH;")
cursor.execute("CREATE OR REPLACE DATABASE SNOWFLAKE_DEMO_APP_DATA;")
cursor.execute("USE DATABASE SNOWFLAKE_DEMO_APP_DATA;")

cursor.execute("CREATE OR REPLACE SCHEMA APP_SCHEMA;")

cursor.execute("USE SCHEMA APP_SCHEMA;")


# connection.cursor().execute("USE DATABASE COVID19_EPIDEMIOLOGICAL_DATA;")

# connection.cursor().execute(
#     "INSERT INTO USERS_DATA(name, f_name,contact_no) "
#     "VALUES(%s, %s,%s)", (
#         'hadi',
#         'abdul',
#         92389273809
#     ))

add_logo()

# header_html = generate_header_html()
# st.markdown(header_html, unsafe_allow_html=True)


st.write("")

# Create the map using pydeck

st.pydeck_chart(pdk.Deck(
    map_style="mapbox://styles/mapbox/light-v9",
   
    initial_view_state=pdk.ViewState(
        latitude=37.7749,
        longitude=-122.4194,
        zoom=10,
        pitch=50,
        height=650,
         width=700
    )
), use_container_width=True)

footer_html = generate_footer_html()
st.markdown(footer_html, unsafe_allow_html=True)
# footer = """<style>
# a:link , a:visited{
# color: blue;
# background-color: transparent;
# text-decoration: underline;
# text- align: center;
# }

# a:hover,  a:active {
# color: red;
# background-color: transparent;
# text-decoration: underline;
# }

# .footer {
# position: fixed;
# left: 0;
# bottom: 0;
# width: 100%;
# background-color: #74a7c3;
# color: white;
# text-align: center;
# }
# </style>
# <div class="footer">
# <p>Powered by <a style="color:white" href="https://www.snowflake.com/en/" target="_blank">Snowflake</a></p>
# </div>
# """
# st.markdown(footer, unsafe_allow_html=True)



# connection.close()
