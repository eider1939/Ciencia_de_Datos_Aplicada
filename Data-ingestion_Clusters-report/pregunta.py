"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""
from numpy import append
import pandas as pd

def remove_space(data):
    data_sin_espacios=[]
    for i in range(0,len(data)):
        data_fila=[]
        for line in data[i]:
            if line != "" and line != " ":
                line=line.replace('_', ' ')
                line=line.strip()
                data_fila.append(line)
        data_sin_espacios.append(data_fila)
    return data_sin_espacios

def join_text(data_sin_espacios):
    cont_index=0
    list_index_pop=[]
    for j in range(0,len(data_sin_espacios)):
        if len(data_sin_espacios[j])>1:
            cont_index=j
        elif len(data_sin_espacios[j])==1:
            list_index_pop.append(j)
            texto=data_sin_espacios[cont_index][3]
            data_sin_espacios[cont_index][3]=str(texto)+' '+str(data_sin_espacios[j][0])
    return data_sin_espacios,list_index_pop

def remove_row_len_1(datos,list_index_pop):
    data_lista=[]
    for k in datos:
        if len(k)>1:
            data_lista.append(k)
    return data_lista

def ingest_data():

    #
    # Inserte su código aquí
    #
    with open('clusters_report.txt') as f:
        data = [line for line in f.readlines()]
    data = data[4:]
    data = [line.replace('\n', '') for line in data]
    data = [line.replace(' ', '_') for line in data]
    data = [line.split("___",7) for line in data]
    datos=remove_space(data)
    datos,list_index_pop=join_text(datos)
    data_lista=remove_row_len_1(datos,list_index_pop)
    columnas = ['cluster', 'cantidad_de_palabras_clave', 'porcentaje_de_palabras_clave', 'principales_palabras_clave']
    df = pd.DataFrame(data_lista, columns = columnas)
    # cambiar type a las columnas cluster y cantidad_de_palabras_clave
    df['cluster']=df['cluster'].astype(int)
    df['cantidad_de_palabras_clave']=df['cantidad_de_palabras_clave'].astype(int)
    #eliminar el % de la columna
    df['porcentaje_de_palabras_clave']=df['porcentaje_de_palabras_clave'].map(lambda x: x.replace(',', '.'))
    df['porcentaje_de_palabras_clave']=df['porcentaje_de_palabras_clave'].str.replace(r"\s\%", '', regex=True).astype(float)
    
    #eliminacion de espacios en la columna principales_palabras_clave
    df['principales_palabras_clave'] = df['principales_palabras_clave'].map(lambda x: x.strip())
    df['principales_palabras_clave'] = df['principales_palabras_clave'].map(lambda x: x.replace('   ', ' '))
    df['principales_palabras_clave'] = df['principales_palabras_clave'].map(lambda x: x.replace('   ', ' '))
    df['principales_palabras_clave'] = df['principales_palabras_clave'].map(lambda x: x.replace('  ', ' '))
    df['principales_palabras_clave'] = df['principales_palabras_clave'].map(lambda x: x.replace('.',''))



    return df
