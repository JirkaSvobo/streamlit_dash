import streamlit as st

st.title('Moje prvni apka')


page = st.sidebar.radio('select page',['Test','Thomson'])

if page == 'Test':
    st.write('toto je prvni apka')

if page == 'Thomson':
    st.write('Thomson sampling')