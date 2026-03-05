# Aplicación Web de Visualización de Datos de Venta de Coches

Desarrollada con **Python**, **Pandas** y **Streamlit**

***

## 📄 Descripción del Proyecto

Esta aplicación web permite explorar de forma interactiva un conjunto de datos sobre vehículos usados, facilitando el análisis visual a través de gráficos generados dinámicamente. Está pensada como una herramienta de apoyo para la comprensión de patrones en el mercado de autos en venta.

***

## 📂 Fuente de Datos

Se utiliza el archivo vehicles_us.csv, que contiene información detallada sobre vehículos a la venta. Algunas columnas relevantes del dataset incluyen:

* model: Marca del vehículo
* price: Precio en dólares (USD)
* odometer: Kilometraje registrado
* condition: Condición general del vehículo
* type, transmission, fuel, paint_color, entre otras


**¿Para qué sirve esta aplicación?**

Esta aplicación web permite a los usuarios:

* **Visualizar la distribución de los kilómetros recorridos (odómetro):** A través de un histograma interactivo, los usuarios pueden entender la frecuencia con la que aparecen diferentes rangos de kilometraje en los vehículos del conjunto de datos.
* **Analizar la relación entre el precio y el kilometraje:** Un gráfico de dispersión permite identificar posibles tendencias o correlaciones entre el precio de los coches y la cantidad de kilómetros que han recorrido.
* **Explorar la distribución de los años de fabricación:** Mediante otro histograma, los usuarios pueden visualizar la cantidad de coches disponibles para cada año de fabricación presente en los datos.
* **Comparar el precio con el año de fabricación:** Un segundo gráfico de dispersión ayuda a investigar si existe alguna relación entre el año en que se fabricó un coche y su precio de venta.

**Funcionalidades principales:**

La aplicación proporciona las siguientes funcionalidades interactivas:

* **Botones para generar gráficos específicos:** Los usuarios pueden hacer clic en botones para mostrar u ocultar histogramas del odómetro y gráficos de dispersión de precio vs. odómetro.
* **Casillas de verificación para visualizaciones adicionales:** Mediante casillas de verificación, los usuarios pueden activar o desactivar la visualización de histogramas del año de fabricación y gráficos de dispersión de precio vs. año de fabricación.
* **Gráficos interactivos:** Los gráficos generados con Plotly Express son totalmente interactivos, permitiendo a los usuarios hacer zoom, desplazar, pasar el ratón sobre los puntos para ver detalles y descargar los gráficos como imágenes.
* **Interfaz intuitiva:** La interfaz de usuario es sencilla y fácil de usar, lo que permite a cualquier persona explorar los datos sin necesidad de conocimientos técnicos avanzados en programación o análisis de datos.

En resumen, esta aplicación web es una herramienta útil para cualquier persona interesada en comprender mejor las características y los precios de los coches que se anuncian para la venta, utilizando visualizaciones interactivas y fáciles de interpretar.
