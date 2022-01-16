import pandas as pd
import numpy as np
import plotly.express as pex
import chart_studio
import chart_studio.plotly as py
from plotly.graph_objects import *
import plotly.graph_objects as go


import datetime
chart_studio.tools.set_credentials_file(username='erfederuiz', api_key='VHWs2LzZApSHGte53mDv')

def lista_distritos(df):
    return sorted(df['origin_district_name'].unique().tolist())

def calc_distrito_internos(row):
    distrito_filtrar = row['Distrito']
    return group_inmd_df[(group_inmd_df['origin_district_name'] == distrito_filtrar) & (group_inmd_df['destination_district_name'] == distrito_filtrar)]['desplazamientos'].sum()

def calc_distrito_externos(row):
    distrito_filtrar = row['Distrito']
    return group_inmd_df[(group_inmd_df['origin_district_name'] == distrito_filtrar) & (group_inmd_df['destination_district_name'] != distrito_filtrar )]['desplazamientos'].sum()

# Entradas y salidas por distrito
def fig01_salidas_distrito(df):
    fig = pex.bar(inmd_df['origin_district_name'].value_counts(sort=True, ascending=True), x='origin_district_name',
                  title='Salidas por distrito', labels={'index': 'Distritos', 'origin_district_name': 'Salidas'})
    return fig


def fig02_entradas_distrito(df):
    fig = pex.bar(inmd_df['destination_district_name'].value_counts(sort=True, ascending=True),
                  x='destination_district_name', title='Entradas por distrito',
                  labels={'index': 'Distritos', 'destination_district_name': 'Entradas'})
    fig.update_traces(marker_color='red')

    return fig

    #return pex.bar(df['destination_district_name'].value_counts(), x='destination_district_name',title='Entradas por distrito')

def fig03_comparativa_es_distrito(df):
    return pex.bar(df, x="distrito", color="tipo",
                    y='valor',
                    title="Comparativa entradas y salidas por distrito",
                    barmode='group',
                    height=600,
                    labels={'valor':'Desplazamientos','distrito':'Distrito', 'tipo':'Tipos de desplazamiento'}
                    )

def fig04_tipos_salidas_distrito(df):
    return pex.bar(df, x="Distrito", color="tipo",
                  y='valor',
                  title="Comparativa tipos de salida por distrito",
                  barmode='group',
                  height=600,
                  labels={'valor':'Desplazamientos','distrito':'Distrito', 'tipo':'Tipos de desplazamiento'}
                  )


def fig05_tipos_salidas_distrito_percent(df, distrito_filtrar):
    """
    https://plotly.com/python/pie-charts/
    https://pythonwife.com/pie-chart-with-plotly/
    """
    externo = \
    df[(df['origin_district_name'] == distrito_filtrar) & (df['destination_district_name'] != distrito_filtrar)][
        'desplazamientos'].sum()
    interno = \
    df[(df['origin_district_name'] == distrito_filtrar) & (df['destination_district_name'] == distrito_filtrar)][
        'desplazamientos'].sum()
    values = [interno, externo]
    names = ['Desplazamientos internos', 'Desplazamientos externos']
    go_fig = go.Figure()
    obj = go.Pie(labels=names, values=values)
    go_fig.add_trace(obj)
    go_fig.update_traces(marker=dict(colors=['blue', 'red'], line=dict(color='#000000', width=1)))

    return go_fig


def fig06_distribucion_sankey_salidas_distrito(df, distrito_filtrar):
    sankey_df = df[(df['origin_district_name'] == distrito_filtrar) & (group_inmd_df['destination_district_name'] != distrito_filtrar)]
    values_list = sankey_df['desplazamientos'].unique().tolist()
    labels_list = sankey_df['destination_district_name'].unique().tolist()
    labels_list.insert(0, distrito_filtrar)

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
        "title": "Distribución salidas a otros distritos desde " + distrito_filtrar,
        "height": 772
    }
    fig = Figure(data=data, layout=layout)
    return fig

def fig07_distribucion_sankey_entradas_distrito(df, distrito_filtrar):
    sankey_df = df[(df['destination_district_name'] == distrito_filtrar) & (group_inmd_df['origin_district_name'] != distrito_filtrar)]
    values_list = sankey_df['desplazamientos'].unique().tolist()
    labels_list = sankey_df['origin_district_name'].unique().tolist()
    labels_list.append( distrito_filtrar)

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
        "title": "Distribución de entradas desde otros distritos a " + distrito_filtrar,
        "height": 772
    }
    fig = Figure(data=data, layout=layout)
    return fig

#Dataframe principal
inmd_file = "./data/inmd_df.csv"
inmd_df = pd.read_csv(inmd_file)

#DF's entradas y salidas por distrito
salidas_dist_df = inmd_df['origin_district_name'].value_counts().sort_index().rename_axis('distrito').reset_index(name='Salidas')
entradas_dist_df = inmd_df['destination_district_name'].value_counts().sort_index().rename_axis('distrito').reset_index(name='Entradas')
compare_inmd_df = pd.merge(salidas_dist_df, entradas_dist_df, on='distrito')
compare_inmd_df = pd.melt(compare_inmd_df, id_vars=['distrito'], var_name='tipo', value_name='valor')

#Comparativas tipos de salidas por distrito
group_inmd_df = inmd_df.groupby(['origin_district_name', 'destination_district_name'], as_index=False).size()
group_inmd_df.rename(columns={'size':'desplazamientos'}, inplace=True )
distritos_df = pd.DataFrame(lista_distritos(group_inmd_df), columns=['Distrito'])
distritos_df['Internos'] = distritos_df.apply(lambda row: calc_distrito_internos(row), axis=1)
distritos_df['Externos'] = distritos_df.apply(lambda row: calc_distrito_externos(row), axis=1)
distritos_df = pd.melt(distritos_df ,id_vars=['Distrito'],var_name='tipo', value_name='valor')

