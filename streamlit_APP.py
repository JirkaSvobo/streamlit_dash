import streamlit as st
from sqlalchemy import create_engine
import pandas as pd
import pymysql

import plotly.graph_objects as go
import plotly.express as px


# #####################################
# data
# #####################################

engine = create_engine("mysql+pymysql://data-student:u9AB6hWGsNkNcRDm@data.engeto.com:3306/data_academy_04_2022")
query = '''SELECT
            start_station_latitude as lat
            start_station_longitude as lon
        FROM edinburgh_bikes
        LIMIT 20000
    '''

df_bikes = pd.read_sql(sql=query, con=engine)

# #####################################
# vizualizace
# #####################################
st.title('Moje prvni apka')


page = st.sidebar.radio('Select page',['Mapa','Thomson'])

if page == 'Mapa':
    st.write('Mapa pouzivani sdilenych kol v Edinburgu')
    st.map(df_bikes)


if page == 'Thomson':
    st.write('Thomson sampling')
