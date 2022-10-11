"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""

import pandas as pd
import numpy as np
import math

def ingest_data():
  archivo=pd.read_fwf(
    "clusters_report.txt",
    colspecs="infer",
    widths=[8,10,20,100],
  )
  datos=archivo.drop([0,1],axis=0)
  datos = pd.DataFrame(datos)
  cluster=datos.iloc[:,0]
  palabras=datos.iloc[:,1]
  porcentaje=datos.iloc[:,2]
  cluster = cluster.dropna()
  palabras = palabras.dropna()
  porcentaje = porcentaje.dropna()
  df = pd.DataFrame(columns=['cluster','cantidad de palabras clave','porcentaje de palabras clave','principales palabras clave'])
  for i in range(0,13):
    df = df.append({'cluster': cluster.iloc[i]}, ignore_index=True)
    df['cantidad de palabras clave'].fillna(palabras.iloc[i],inplace=True)
    df['porcentaje de palabras clave'].fillna(porcentaje.iloc[i],inplace=True)
  final=df
  return final
