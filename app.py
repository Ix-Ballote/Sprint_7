import pandas as pd
import streamlit as st
import plotly.express as px

car_data = pd.read_csv('vehicles_us.csv')  # Leer los datos

st.header('Venta de coches')


# BOTONES

st.header('Botones')

# Histograma
hist_button = st.button('Histograma')  # Crear un botón

if hist_button:  # Al hacer clic en el botón
    # Escribir un mensaje
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # Crear un histograma
    fig = px.histogram(car_data, x="odometer")

    # Mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)


# Dispersión
disp_button = st.button('Gráfico de dispersión')  # Crear un botón

if disp_button:  # Al hacer clic en el botón
    # Escribir un mensaje
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')

    # Crear un gráfico de dispersión
    fig = px.scatter(car_data, x="odometer", y="price")

    # Mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)


# CASILLAS DE VERIFICACIÓN

st.header('Casillas de verificación')

# Crear una casilla de verificación
build_histogram = st.checkbox('Construir un histograma')

if build_histogram:  # Si la casilla de verificación está seleccionada
    # Escribir un mensaje
    st.write('Creación de un histograma para el año de fabricación de los coches')

    # Crear un histograma
    fig = px.histogram(car_data, x="model_year")

    # Mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)


# Crear una casilla de verificación
build_dispersion = st.checkbox('Construir un gráfico de dispersión')

if build_dispersion:  # Si la casilla de verificación está seleccionada
    # Escribir un mensaje
    st.write('Comparación de precios contra el año de fabricación del coche')

    # Crear un gráfico de dispersión
    fig = px.scatter(car_data, x="model_year", y="price")

    # Mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
