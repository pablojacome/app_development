import pandas as pd
import plotly.express as px
import streamlit as st

# Leer los datos
car_data = pd.read_csv('vehicles_us.csv')

# Título de la app
st.title("Análisis interactivo de vehículos")

# Checkbox para histograma
show_hist = st.checkbox('Mostrar histograma del odómetro')

# Checkbox para scatter plot
show_scatter = st.checkbox('Mostrar diagrama de dispersión: odómetro vs precio')

# Mostrar histograma si se selecciona
if show_hist:
    st.write('Histograma de odómetro')
    fig_hist = px.histogram(car_data, x='odometer')
    st.plotly_chart(fig_hist, use_container_width=True)

# Mostrar scatter plot si se selecciona
if show_scatter:
    st.write('Diagrama de dispersión: odómetro vs precio')
    fig_scatter = px.scatter(car_data, x='odometer', y='price', color='condition', opacity=0.5)
    st.plotly_chart(fig_scatter, use_container_width=True)
