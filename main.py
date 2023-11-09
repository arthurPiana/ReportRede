import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

df = pd.read_excel('relatorio_zaaz.xlsx')

st.title('Relatorio geral por tipo de cabo')

st.write(open("intro.txt", 'r', encoding='utf-8').read())

fig = px.bar(df, x="nivel", y="comprimento", color='tipo',barmode="group", text_auto='.2s')
st.plotly_chart(fig, use_container_width=True)


st.header('Dados angariados pela ferramenta')
st.dataframe(df)
