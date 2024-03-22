
import snowflake.connector as sf
import streamlit as st
import pandas as pd
import os
from PIL import Image
from tempfile import NamedTemporaryFile


conn_param = {
    "user":'atahir',
    "password":'AliSnowFlake1$',
    "account":'YVTQFWQ-WU63006',
    "warehouse":'COMPUTE_WH',
    "database":'SNOWFLAKE_DATA_APP',
    "schema":'app',
}

connection = sf.connect(
    user='atahir',
    password='AliSnowFlake1$',
    account='YVTQFWQ-WU63006',
    warehouse='COMPUTE_WH',
    database='SNOWFLAKE_DATA_APP',
    schema='app',
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
cursor.execute("USE DATABASE SNOWFLAKE_APP_DATA;")
cursor.execute("USE SCHEMA APP;")


# connection.cursor().execute("USE DATABASE COVID19_EPIDEMIOLOGICAL_DATA;")

# connection.cursor().execute(
#     "INSERT INTO USERS_DATA(name, f_name,contact_no) "
#     "VALUES(%s, %s,%s)", (
#         'hadi',
#         'abdul',
#         92389273809
#     ))



with st.sidebar:
    st.image("./unnamed.png", width=300)

    nav_items = {
        "Partners": "/Partners",
        "shared": "/shared",
        "operations": "/operations",
        "Account": "/Account",
        "Message": "/Message",
        "profile": "/profile",
    }

# Generate HTML links for navbar items
    nav_links = ''.join(f'<a href="{url}">{label}</a>' for label, url in nav_items.items())

    navbar_template = f"""
        <style>
            .navbar {{
                background-color:#74A7C3;
                display: flex;
                align-items: center;
                width: 60%; 
                height:10%;
                margin: 0;
                position: fixed; 
                top: 39px; 
            
            }}

            .navbar a {{
                color: #fffff;
                text-align: center;
                text-decoration: none;
                font-size: 17px;
                padding: 14px 20px;
            
            }}

            .navbar a:hover {{
                background-color: #ddd;
                color: black;
            }}
        </style>
        <div class="navbar">
            {nav_links}
        </div>
    """
 

st.markdown(navbar_template, unsafe_allow_html=True)


footer = """<style>
a:link , a:visited{
color: blue;
background-color: transparent;
text-decoration: underline;
text- align: center;
}

a:hover,  a:active {
color: red;
background-color: transparent;
text-decoration: underline;
}

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: #74a7c3;
color: white;
text-align: center;
}
</style>
<div class="footer">
<p>Powered by <a style="color:white" href="https://www.snowflake.com/en/" target="_blank">Snowflake</a></p>
</div>
"""
st.markdown(footer, unsafe_allow_html=True)

# connection.close()
