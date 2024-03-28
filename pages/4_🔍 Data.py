
import snowflake.connector as sf
import streamlit as st
import pandas as pd
import os
from PIL import Image
from tempfile import NamedTemporaryFile
from snowflake.snowpark import FileOperation, Session

from footer import generate_footer_html
from navbar import generate_header_html
from logo_utils import add_logo


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


cursor = connection.cursor()
cursor.execute("USE WAREHOUSE COMPUTE_WH;")
cursor.execute("CREATE DATABASE SNOWFLAKE_DEMO_APP_DATA IF NOT EXISTS;")
cursor.execute("USE DATABASE SNOWFLAKE_DEMO_APP_DATA;")

cursor.execute("CREATE SCHEMA APP_SCHEMA IF NOT EXISTS;")

cursor.execute("USE SCHEMA APP_SCHEMA;")


# header_html = generate_header_html()
# st.markdown(header_html, unsafe_allow_html=True)

add_logo()


create_stage_sql = f"CREATE OR REPLACE STAGE IOT_data_stage"
cursor.execute(create_stage_sql)

create_stage_sql = f"CREATE OR REPLACE STAGE EO_data_stage"
cursor.execute(create_stage_sql)

st.write("# Data Uploading")

uploaded_file = st.file_uploader("Choose CSV File To Upload")
if uploaded_file is not None:
    file_name = os.path.splitext(uploaded_file.name)[0]

    df = pd.read_csv(uploaded_file)
    headers = list(df.columns)
    

    st.write(df)


    uploaded_file_contents = uploaded_file.read()

    # Create a temporary file in memory and write the uploaded file's contents to it
    with NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(uploaded_file_contents)
        temp_file_path = temp_file.name

    # Upload data from CSV to the stage
    put_statement = f"PUT file://{temp_file_path} @IOT_data_stage"
    cursor.execute(put_statement)


    # Generate CREATE TABLE statement dynamically
    create_table_sql = f"CREATE OR REPLACE TABLE {file_name} ({', '.join([f'{header} STRING' for header in headers])})"
    cursor.execute(create_table_sql)


    # Copy data from the stage into the table
    copy_into_statement = f"COPY INTO {file_name} FROM @IOT_data_stage"
    cursor.execute(copy_into_statement)

    

    # Load data from CSV into Snowflake
    # put_statement = f"PUT file:///home/gisplus/Downloads/US_MSR_10M/{uploaded_file.name} @%{file_name}"
    # cursor.execute(put_statement)

    # copy_into_statement = f"COPY INTO {file_name}"
    # cursor.execute(copy_into_statement)



    os.remove(temp_file_path)

    connection.cursor().close()


eo_uploaded_file = st.file_uploader("Upload TIFF file", type=["tif", "tiff"])
if eo_uploaded_file is not None:
        

        session = Session.builder.configs(conn_param).create()
        session.sql("use database SNOWFLAKE_DEMO_APP_DATA").collect()

        FileOperation(session).put_stream(input_stream=eo_uploaded_file,stage_location='SNOWFLAKE_DEMO_APP_DATA.APP_SCHEMA.EO_data_stage/' + eo_uploaded_file.name)
        

        st.image(eo_uploaded_file)


footer_html = generate_footer_html()
st.markdown(footer_html, unsafe_allow_html=True)
