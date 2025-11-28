import pandas as pd
import plotly.express as px
import streamlit as st

st.title('DASHCOVID - Um Painel de Informações sobre a COVID-19 - Ano 2020')

st.set_page_config(page_title = 'DASHCOVID', layout = 'wide')

df = pd.read_csv('WHO_time_series(1).csv')

df['Date_reported'] = pd.to_datetime(df['Date_reported'])

fig1 = px.line(df, x = 'Date_reported', y = 'Cumulative_cases', color = "Country", title = 'Casos acumulados')
fig1.update_layout(xaxis_title = 'Data', yaxis_title = 'Casos acumulados')
               
st.plotly_chart(fig1, use_container_width = True)
               
df_br_eua_ind = df.query("Country == 'Brazil' or Country == 'United States of America' or Country == 'India'")

fig2 = px.pie(df_br_eua_ind, values = 'Cumulative_cases', names = "Country", title = "Casos Covid-19: Brasil, EUA e India")
               
st.plotly_chart(fig2, use_container_width = True)
