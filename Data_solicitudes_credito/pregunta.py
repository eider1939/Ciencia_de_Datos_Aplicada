"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""


import pandas as pd

from datetime import datetime
def fecha(x):
    try:
        return datetime.strptime(x, '%d/%m/%Y')
    except:
        return datetime.strptime(x, '%Y/%m/%d') 
        
def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";")

    #
    # Inserte su código aquí
    #
    df.drop(['Unnamed: 0'], axis=1,inplace=True)
    df.drop_duplicates(inplace=True)
    df.dropna(axis=0,inplace=True)
    #convertir la columan sexo a mayuculas para obtner solo dos valores distintos
    df['sexo']=df['sexo'].str.lower()
    #convertitmos la columna tipo_de_emprendimiento a string y a mayusculas
    df['tipo_de_emprendimiento']=df['tipo_de_emprendimiento'].astype(str)
    df['tipo_de_emprendimiento']=df['tipo_de_emprendimiento'].str.lower()
    # modificaciones columna idea_negocio str,lower,replace
    df['idea_negocio']=df['idea_negocio'].str.lower()
    df['idea_negocio']=df['idea_negocio'].map(lambda x: x.replace(" ",'_'))
    df['idea_negocio']=df['idea_negocio'].map(lambda x: x.replace("-",'_'))

    #convertimo la columna barrio a string luego elimnamos lo espacion y convertirmos a mayusculas
    df['barrio']=df['barrio'].astype(str)
    df['barrio']=df['barrio'].str.lower()
    df['barrio']=df['barrio'].map(lambda x: x.replace("-",' '))
    df['barrio']=df['barrio'].map(lambda x: x.replace("_",' '))
    
    #columna comuna_ciudadano
    df['comuna_ciudadano']=df['comuna_ciudadano'].astype(float)
    #columna fecha_de_beneficio
    df['fecha_de_beneficio']=df['fecha_de_beneficio'].apply(lambda x: fecha(x))
    df['fecha_de_beneficio']=df['fecha_de_beneficio'].dt.strftime('%d/%m/%Y')
    #columna monto_del_credito
    df['monto_del_credito']=df['monto_del_credito'].map(lambda x: x.replace("$ ",''))
    df['monto_del_credito']=df['monto_del_credito'].map(lambda x: x.replace(",",''))
    df['monto_del_credito']=df['monto_del_credito'].map(lambda x: x.replace(".00",''))
    df['monto_del_credito']=df['monto_del_credito'].astype(float)
    #columna línea_credito
    df['línea_credito']=df['línea_credito'].str.lower()
    df['línea_credito']=df['línea_credito'].map(lambda x: x.replace(" ",'_'))
    df['línea_credito']=df['línea_credito'].map(lambda x: x.replace("-",'_'))
    df.drop_duplicates(inplace=True)
    df.dropna(axis=0,inplace=True)
    return df