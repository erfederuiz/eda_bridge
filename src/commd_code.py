import pandas as pd
import numpy as np
import plotly.express as pex
import chart_studio
import chart_studio.plotly as py
from plotly.graph_objects import *
import plotly.graph_objects as go
import re

import datetime
chart_studio.tools.set_credentials_file(username='erfederuiz', api_key='VHWs2LzZApSHGte53mDv')

def lista_municipios(df):
    return sorted(df['origin_town_name'].unique().tolist())


def filter_municipios_convarios(row):
    origin_town_name = row['origin_town_name']
    destination_town_name = row['destination_town_name']
    if origin_town_name.count(',') > 1 or destination_town_name.count(',') > 1:
        return False
    elif origin_town_name.count(',') == 1 or destination_town_name.count(',') == 1:
        pattern = re.compile(r', (El|Los|Las)')
        origin_matches = pattern.search(origin_town_name)
        destination_matches = pattern.search(destination_town_name)
        if origin_matches and destination_matches:
            return True
        else:
            return False
    else:
        return True

def fig01_mas20k_salidas(df):
    fig = pex.bar(df.sort_values(by='Salidas', ascending=True), x='Salidas', y='Municipio',
                  title='Salidas por municipio (>20.000)', height=800)
    return fig

def fig02_menos20k_salidas(df):
    fig = pex.bar(df.sort_values(by='Salidas', ascending=True), x='Salidas',
                  y='Municipio', title='Salidas por municipio (<20.000)', height=800)
    return fig

def fig03_mas20k_entradas(df):
    fig = pex.bar(df.sort_values(by='Entradas', ascending=True), x='Entradas',
                  y='Municipio', title='Entradas por municipio (>20.000)', height=800)
    return fig

def fig04_menos20k_entradas(df):
    fig = pex.bar(df.sort_values(by='Entradas', ascending=True), x='Entradas',
                  y='Municipio', title='Entradas por municipio (<20.000)', height=800)
    return fig


def fig06_distribucion_sankey_salidas_municipio(df, municipio_filtrar, mensaje_title):
    sankey_df = df[(df['origin_town_name'] == municipio_filtrar) & (df['destination_town_name'] != municipio_filtrar)].sort_values(by='Desplazamientos', ascending=False).head(20)
    values_list = sankey_df['Desplazamientos'].unique().tolist()
    labels_list = sankey_df['destination_town_name'].unique().tolist()
    labels_list.insert(0, municipio_filtrar)

    trace1 = {
        "link": {
            "color": ['antiquewhite',
                      'aqua',
                      'aquamarine',
                      'azure',
                      'beige',
                      'bisque',
                      'black',
                      'blanchedalmond',
                      'aliceblue',
                      'blueviolet',
                      'brown',
                      'burlywood',
                      'cadetblue',
                      'chartreuse',
                      'chocolate',
                      'coral',
                      'cornflowerblue',
                      'cornsilk',
                      'crimson',
                      'cyan'],
            "value": values_list,
            "source": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            "target": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        },
        "node": {
            "pad": 30,
            "line": {
                "color": "black",
                "width": 0
            },
            "color": ['blue', 'antiquewhite', 'aqua', 'aquamarine', 'azure',
                    'beige', 'bisque', 'black', 'blanchedalmond', 'aliceblue',
                    'blueviolet', 'brown', 'burlywood', 'cadetblue',
                    'chartreuse', 'chocolate', 'coral', 'cornflowerblue',
                    'cornsilk', 'crimson', 'cyan'],
            "label": labels_list,
            "thickness": 30
        },
        "type": "sankey",
        "domain": {
            "x": [0, 1],
            "y": [0, 1]
        },
        "orientation": "h",
        "valueformat": ".0f"
    }
    data = Data([trace1])
    layout = {
        "font": {"size": 15},
        "title": mensaje_title,
        "height": 772
    }
    fig = Figure(data=data, layout=layout)
    return fig

def fig07_distribucion_sankey_entradas_municipio(df, municipio_filtrar, mensaje_title):
    sankey_df = df[(df['origin_town_name'] != municipio_filtrar) & (df['destination_town_name'] == municipio_filtrar)].sort_values(by='Desplazamientos',ascending=False).head(20)
    values_list = sankey_df['Desplazamientos'].unique().tolist()
    labels_list = sankey_df['origin_town_name'].unique().tolist()
    labels_list.append( municipio_filtrar)

    trace1 = {
        "link": {
            "color": ['antiquewhite',
                      'aqua',
                      'aquamarine',
                      'azure',
                      'beige',
                      'bisque',
                      'black',
                      'blanchedalmond',
                      'aliceblue',
                      'blueviolet',
                      'brown',
                      'burlywood',
                      'cadetblue',
                      'chartreuse',
                      'chocolate',
                      'coral',
                      'cornflowerblue',
                      'cornsilk',
                      'crimson',
                      'cyan'],
            "value": values_list,
            "source": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
            "target": [20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20]

        },
        "node": {
            "pad": 30,
            "line": {
                "color": "black",
                "width": 0
            },
            "color": ['antiquewhite', 'aqua', 'aquamarine', 'azure',
                    'beige', 'bisque', 'black', 'blanchedalmond', 'aliceblue',
                    'blueviolet', 'brown', 'burlywood', 'cadetblue',
                    'chartreuse', 'chocolate', 'coral', 'cornflowerblue',
                    'cornsilk', 'crimson', 'cyan', 'red'],
            "label": labels_list,
            "thickness": 30
        },
        "type": "sankey",
        "domain": {
            "x": [0, 1],
            "y": [0, 1]
        },
        "orientation": "h",
        "valueformat": ".0f"
    }
    data = Data([trace1])
    layout = {
        "font": {"size": 15},
        "title": mensaje_title,
        "height": 772
    }
    fig = Figure(data=data, layout=layout)
    return fig


csv_incommd_df = "./data/incommd_df.csv"
csv_incommd_df = pd.read_csv(csv_incommd_df)

#Eliminar los desplazamientos de mas de un municipio
incommd_df = csv_incommd_df[csv_incommd_df.apply(lambda row: filter_municipios_convarios(row), axis=1)]

municipios_origin = incommd_df['origin_town_name'].unique().tolist()
municipios_destination = incommd_df['destination_town_name'].unique().tolist()

# Estudiar solo los desplazamientos de salida de municipios != Madrid
salidas_incommd_nomd_df = incommd_df[(incommd_df['origin_town_name'] != 'Madrid')]
incommd_nomd_salidas_df = salidas_incommd_nomd_df['origin_town_name'].value_counts().sort_index().rename_axis('Municipio').reset_index(name='Salidas')

incommd_nomd_salidas_mas20k_df = incommd_nomd_salidas_df[(incommd_nomd_salidas_df['Salidas'] > 20000)]
incommd_nomd_salidas_mas20k_df.sort_values(by=['Salidas'], inplace=True, ascending=False)
incommd_nomd_salidas_menos20k_df = incommd_nomd_salidas_df[(incommd_nomd_salidas_df['Salidas'] <= 20000)]
incommd_nomd_salidas_menos20k_df.sort_values(by=['Salidas'], inplace=True, ascending=False)


entradas_incommd_nomd_df = incommd_df[(incommd_df['destination_town_name'] != 'Madrid')]
incommd_nomd_entradas_df = entradas_incommd_nomd_df['destination_town_name'].value_counts().sort_index().rename_axis('Municipio').reset_index(name='Entradas')

incommd_nomd_entradas_mas20k_df = incommd_nomd_entradas_df[(incommd_nomd_entradas_df['Entradas'] > 20000)]
incommd_nomd_entradas_mas20k_df.sort_values(by=['Entradas'], inplace=True, ascending=False)
incommd_nomd_entradas_menos20k_df = incommd_nomd_entradas_df[(incommd_nomd_entradas_df['Entradas'] <= 20000)]
incommd_nomd_entradas_menos20k_df.sort_values(by=['Entradas'], inplace=True, ascending=False)

#Dataframes desglose Sankey
group_incommd_df = incommd_df
group_incommd_df = group_incommd_df[(group_incommd_df['origin_town_name'] != 'Madrid') & (group_incommd_df['destination_town_name'] != 'Madrid')].groupby(['origin_town_name', 'destination_town_name'], as_index=False).size()
group_incommd_df.rename(columns={'size':'Desplazamientos'}, inplace=True)

group_incommd_conmd_df = incommd_df
group_incommd_conmd_df = group_incommd_conmd_df.groupby(['origin_town_name', 'destination_town_name'], as_index=False).size()
group_incommd_conmd_df.rename(columns={'size':'Desplazamientos'}, inplace=True)