import self
import snowflake.connector as sf
import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import rasterio
from rasterio.plot import show
import os
import self
from PIL import Image
from tempfile import NamedTemporaryFile
import matplotlib.pyplot as plt
from snowflake.snowpark import FileOperation
from snowflake.snowpark import FileOperation, Session


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

def home():
    st.write("# Home Page")
    st.write("Welcome to the Home Page")


def about():
    st.write("# About Page")
    st.write("This is the About Page")


def contact():
    st.write("# Contact Page")
    st.write("This is the Contact Page")


def main():
    pages = {
        "Home": home,
        "About": about,
        "Contact": contact
    }


with st.sidebar:
    st.image("./unnamed.png", width=300)

with st.sidebar:
    selected = option_menu(
        menu_title='',
        options=["Home", "Partners", "Shared", "Data Upload", "Image Data", "CSV Data"]

    )


if selected == "Home":
    st.write("# Home Page")
    st.write("Welcome to the Home Page")
if selected == "Data Upload":
    uploaded_file = st.file_uploader("Choose CSV File To Upload")
    if uploaded_file is not None:
        file_name = os.path.splitext(uploaded_file.name)[0]

        df = pd.read_csv(uploaded_file, nrows=1)
        headers = list(df.columns)

        # Generate CREATE TABLE statement dynamically
        create_table_sql = f"CREATE OR REPLACE TABLE {file_name} ({', '.join([f'{header} STRING' for header in headers])})"
        cursor.execute(create_table_sql)

        # Load data from CSV into Snowflake
        put_statement = f"PUT file:///home/gisplus/Downloads/US_MSR_10M/{uploaded_file.name} @%{file_name}"
        cursor.execute(put_statement)

        copy_into_statement = f"COPY INTO {file_name}"
        cursor.execute(copy_into_statement)

        connection.cursor().close()

        dataframe = pd.read_csv(uploaded_file)
        st.write(dataframe)

    eo_uploaded_file = st.file_uploader("Upload TIFF file", type=["tif", "tiff"])
    if eo_uploaded_file is not None:
        stage_nm = 'demo'

        session = Session.builder.configs(conn_param).create()
        session.sql("use database SNOWFLAKE_APP_DATA").collect()
        session.sql("CREATE STAGE SNOWFLAKE_APP_DATA.APP.demo;")

        FileOperation(session).put_stream(input_stream=eo_uploaded_file,stage_location='@' + stage_nm + '/' + eo_uploaded_file.name)
        st.image(eo_uploaded_file)

if __name__ == "__main__":
    main()

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
