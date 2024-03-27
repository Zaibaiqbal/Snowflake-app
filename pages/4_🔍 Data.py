
import snowflake.connector as sf
import streamlit as st
import pandas as pd
import os
from PIL import Image
from tempfile import NamedTemporaryFile
from snowflake.snowpark import FileOperation, Session

from footer import generate_footer_html
from navbar import generate_header_html

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
cursor.execute("USE DATABASE SNOWFLAKE_APP_DATA;")
cursor.execute("USE SCHEMA APP;")



header_html = generate_header_html()
st.markdown(header_html, unsafe_allow_html=True)


create_stage_sql = f"CREATE OR REPLACE STAGE IOT_data_stage"
cursor.execute(create_stage_sql)

st.write("# Data Uploading")

uploaded_file = st.file_uploader("Choose CSV File To Upload")
if uploaded_file is not None:
    file_name = os.path.splitext(uploaded_file.name)[0]

    df = pd.read_csv(uploaded_file, nrows=1)
    headers = list(df.columns)


    # Upload data from CSV to the stage
    put_statement = f"PUT file://{uploaded_file.file} @IOT_data_stage"
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


footer_html = generate_footer_html()
st.markdown(footer_html, unsafe_allow_html=True)
