import pandas as pd
import plotly.express as px
import streamlit as st

st.title('Mi primera data app sobre :green[Venta de Automóviles]')
st.header("por :blue[Marco Martínez] :sunglasses:", divider=True)

car_data = pd.read_csv('vehicles_us.csv') # leer los datos
hist_button = st.button('Construir histograma') # crear un botón
        
if hist_button: # al hacer clic en el botón
# escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

scatter_button = st.button('Construir gráfico de dispersión')
#Se agrega un botón para crear el gráfico de dispersión solicitado

if scatter_button:
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    #Crea un gráfico de dispersión
    fig = px.scatter(car_data, x = 'odometer', y = 'price', title = 'Relación entre odómetro y precio')

# crear una casilla de verificación
build_bar = st.checkbox('Construir un histograma')

if build_bar: # si la casilla de verificación está seleccionada
    st.write('Construir un histograma para la columna odómetro')
    #Crear gráfica de barras
    fig_hist = px.histogram(car_data, x = 'odometer')
    st.plotly_chart(fig_hist, use_container_width=True) #Necesario el plotly_chart