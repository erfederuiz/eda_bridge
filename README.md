# Proyecto EDA - Bootcamp Datascience Full Time Nov. 2021

Este proyecto proporciona una aplicación Streamlit para visualizar  datos de desplazamientos por trabajo dentro de la Comunidad de Madrid.
Se han creado dos vistas en Streamlit que separan los datos en dos secciones:

<ol>
<li>Desplazamientos entre municipios de la Comunidad de Madrid</li>
<li>Desplazamientos entre distritos de Madrid Capital</li>
</ol>

Esta separación de la lógica, se ha implementado usando la aplicación <em><a href="https://github.com/alanjones2/mustrapp">Mustrapp</a> - (Multi-app Streamlit Application)</em>

https://towardsdatascience.com/how-to-build-a-gallery-of-streamlit-apps-as-a-single-web-app-466682190629

Esta aplicación se implementa en un archivo Python, que busca en una carpeta determinada <em>stlib</em> las aplicaciones que se mostrarán en forma de galería:

<ul>
<li>commd_app.py</li>
<li>inmd_app.py</li>
</ul>
  
Estas aplicaciones contendrán la lógica Streamlit para formatear la presentación.
La lógica de preparación de datos internos se ha implementado en dos módulos: 

<ul>
<li>commd_code.py</li>
<li>inmd_code.py</li>
</ul>

Los datos se ubicarán en el directorio <em>data</em>, separados según las necesidades de las aplicaciones.
Esta es la arquitectura física de la aplicación desarrollada.


```
/src
 |
 |-- index.py
 |
 |-- commd_code.py
 |
 |-- inmd_code.py
 |
 |-- /data
 |     |
 |     |-- incommd_df.csv
 |     |
 |     |-- inmd_df.csv
 |      
 |-- /stlib
       |
       |-- __init__.py
       |
       |-- commd_app.py
       |
       |-- inmd_app.py
```
       
|Aplicación               |Archivo datos  |Archivo lógica|Archivo Streamlit|
|:------------------------|:--------------|:-------------|:----------------|
|Datos Comunidad de Madrid|incommd_df.csv |commd_code.py |commd_app.py     |
|Datos Madrid capital     |inmd_df.csv    |inmd_code.py  |inmd_app.py      |

## Ejecución
Descargar el código 

Instalar los módulos Python mediante el archivo Requirements.txt

Ejecutar en el directorio src:
```
stremlit run index.py
```
