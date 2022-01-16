import os
import sys

script_dir = os.path.dirname(__file__)
mymodule_dir = os.path.join(script_dir, '..')
sys.path.append(mymodule_dir)

import inmd_code
description = "Madrid Capital"

# Your app goes in the function run()
def run():
        
    import streamlit as st


    st.title("Datos Madrid capital")
    st.header("Desplazamientos entre distritos de Madrid")
    (col1, col2) = st.columns(2)
    with col1:
        st.plotly_chart(inmd_code.fig01_salidas_distrito(inmd_code.inmd_df))
    with col2:
        st.plotly_chart(inmd_code.fig02_entradas_distrito(inmd_code.inmd_df))

    (col3, col4) = st.columns(2)
    with col3:
        st.plotly_chart(inmd_code.fig03_comparativa_es_distrito(inmd_code.compare_inmd_df))
    with col4:
        st.plotly_chart(inmd_code.fig04_tipos_salidas_distrito(inmd_code.distritos_df))

    distrito_filtrar = st.selectbox("Filtrar un distrito:",inmd_code.lista_distritos(inmd_code.group_inmd_df))
    (col5, col6 ) = st.columns(2)
    with col5:
        st.write("Porcentaje desplazamientos internos/externos en " + distrito_filtrar)
        st.plotly_chart(inmd_code.fig05_tipos_salidas_distrito_percent(inmd_code.group_inmd_df, distrito_filtrar))
    with col6:
        st.write("   ")

    (col7, col8) = st.columns(2)
    with col7:
        st.plotly_chart(inmd_code.fig06_distribucion_sankey_salidas_distrito(inmd_code.group_inmd_df, distrito_filtrar))
    with col8:
        st.plotly_chart(inmd_code.fig07_distribucion_sankey_entradas_distrito(inmd_code.group_inmd_df, distrito_filtrar))

# end of app

# This code allows you to run the app standalone
# as well as part of a library of apps
if __name__ == "__main__":
    run()