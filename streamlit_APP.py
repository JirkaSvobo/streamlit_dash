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
query_morning = """SELECT
                start_station_latitude as lat,
                start_station_longitude as lon
            FROM edinburgh_bikes
            WHERE hour(started_at) BETWEEN 6 AND 9
            LIMIT 100000
        """

query_afternoon = """SELECT
                start_station_latitude as lat,
                start_station_longitude as lon
            FROM edinburgh_bikes
            WHERE hour(started_at) BETWEEN 15 AND 19
            LIMIT 100000
        """

df_bikes_morning = pd.read_sql(sql=query_morning, con=engine)
df_bikes_afternoon = pd.read_sql(sql=query_afternoon, con=engine)

# #####################################
# vizualizace
# #####################################
st.title('Moje prvni apka')


page = st.sidebar.radio('Select page',['Mapa','Thomson'])

if page == 'Mapa':
    st.header('Mapa pouzivani sdilenych kol v Edinburgu')
    st.write('Pocatecni stanice rano 6 az 9')
    st.map(df_bikes_morning)
    st.write('Pocatecni stanice odpoledne 15 az 19')
    st.map(df_bikes_afternoon)


if page == 'Thomson':
    st.write('Thomson sampling')
