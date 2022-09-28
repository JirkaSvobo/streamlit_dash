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


# #####################################
# vizualizace
# #####################################
st.set_page_config(layout = 'wide')
st.title('Moje prvni apka')


page = st.sidebar.radio('Select page',['Mapa','Thomson'])

if page == 'Mapa':
    st.header('Mapa pouzivani sdilenych kol v Edinburgu')

    col1, col2 = st.columns(2)

    from_hour_morning = col1.slider('rano od', min_value=5, max_value=12)
    to_hour_morning = col1.slider('rano do', min_value=5, max_value=12)
    col1.write('Pocatecni stanice rano mezi {} a {}'.format(from_hour_morning, to_hour_morning))
    query_morning = """SELECT
                        start_station_latitude as lat,
                        start_station_longitude as lon
                    FROM edinburgh_bikes
                    WHERE hour(started_at) BETWEEN {} AND {}
                    LIMIT 100000
                """.format(from_hour_morning, to_hour_morning)
    df_bikes_morning = pd.read_sql(sql=query_morning, con=engine)
    col1.map(df_bikes_morning)

    from_hour_afternoon = col2.slider('odpoledne od', min_value=5, max_value=12)
    to_hour_afternoon = col2.slider('odpoledne do', min_value=5, max_value=12)
    col2.write('Pocatecni stanice odpoledne mezi {} a {}'.format(from_hour_afternoon, to_hour_afternoon))
    query_afternoon = """SELECT
                         start_station_latitude as lat,
                         start_station_longitude as lon
                     FROM edinburgh_bikes
                     WHERE hour(started_at) BETWEEN {} AND {}
                     LIMIT 100000
                 """.format(from_hour_afternoon, to_hour_afternoon)
    df_bikes_afternoon = pd.read_sql(sql=query_afternoon, con=engine)
    col2.map(df_bikes_afternoon)


if page == 'Thomson':
    st.write('Thomson sampling')
