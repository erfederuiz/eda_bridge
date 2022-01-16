import os
import sys

script_dir = os.path.dirname(__file__)
mymodule_dir = os.path.join(script_dir, '..')
sys.path.append(mymodule_dir)

import commd_code
description = "Comunidad de Madrid"

# Your app goes in the function run()
def run():
        
    import streamlit as st


    st.title("Datos Comunidad de Madrid")
    st.header("Desplazamientos entre municipios de Madrid")

    st.plotly_chart(commd_code.fig01_mas20k_salidas(commd_code.incommd_nomd_salidas_mas20k_df))
    st.plotly_chart(commd_code.fig02_menos20k_salidas(commd_code.incommd_nomd_salidas_menos20k_df))
    st.plotly_chart(commd_code.fig03_mas20k_entradas(commd_code.incommd_nomd_entradas_mas20k_df))
    st.plotly_chart(commd_code.fig04_menos20k_entradas(commd_code.incommd_nomd_entradas_menos20k_df))

    (col1, col2) = st.columns(2)
    with col1:
        st.write("Distribución de desplazamientos")
        st.write("desde " + 'Madrid')
        st.plotly_chart(commd_code.fig06_distribucion_sankey_salidas_municipio(commd_code.group_incommd_conmd_df, 'Madrid', ""))
    with col2:
        st.write("Distribución de desplazamientos")
        st.write("hacia " + 'Madrid')
        st.plotly_chart(commd_code.fig07_distribucion_sankey_entradas_municipio(commd_code.group_incommd_conmd_df, 'Madrid', ""))

    municipio_filtrar = st.selectbox("Filtrar un municipio:", commd_code.lista_municipios(commd_code.salidas_incommd_nomd_df))

    (col3, col4) = st.columns(2)
    with col3:
        st.write("Distribución de desplazamientos")
        st.write("desde " + municipio_filtrar)
        st.plotly_chart(commd_code.fig06_distribucion_sankey_salidas_municipio(commd_code.group_incommd_df, municipio_filtrar, ""))
    with col4:
        st.write("Distribución de desplazamientos")
        st.write("hacia " + municipio_filtrar)
        st.plotly_chart(commd_code.fig07_distribucion_sankey_entradas_municipio(commd_code.group_incommd_df, municipio_filtrar, ""))

    (col5, col6) = st.columns(2)
    with col5:
        st.write("Distribución de desplazamientos")
        st.write("desde " + municipio_filtrar + ' (incluyendo Madrid)' )
        st.plotly_chart(commd_code.fig06_distribucion_sankey_salidas_municipio(commd_code.group_incommd_conmd_df, municipio_filtrar, ""))
    with col6:
        st.write("Distribución de desplazamientos")
        st.write("desde " + municipio_filtrar + ' (sin incluir Madrid)')
        st.plotly_chart(commd_code.fig06_distribucion_sankey_salidas_municipio(commd_code.group_incommd_df, municipio_filtrar, ""))
# end of app

# This code allows you to run the app standalone
# as well as part of a library of apps
if __name__ == "__main__":
    run()