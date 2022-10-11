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
  ayuda1= frase.iloc[0]+frase.iloc[1]+frase.iloc[2]+frase.iloc[3]
  ayuda2=frase.iloc[4]+frase.iloc[5]+frase.iloc[6]+frase.iloc[7]+ frase.iloc[8]
  ayuda3= frase.iloc[9]+frase.iloc[10]+frase.iloc[11]
  ayuda4=frase.iloc[12]+frase.iloc[13]+frase.iloc[14]+frase.iloc[15]
  ayuda5= frase.iloc[16]+frase.iloc[17]+frase.iloc[18]+frase.iloc[19]
  ayuda6=frase.iloc[20]+frase.iloc[21]+frase.iloc[22]+frase.iloc[23]
  ayuda7=frase.iloc[24]+frase.iloc[25]+frase.iloc[26]+ frase.iloc[27]
  ayuda8= frase.iloc[28]+frase.iloc[29]+frase.iloc[30]+frase.iloc[31]
  ayuda9=frase.iloc[32]+frase.iloc[33]+frase.iloc[34]+frase.iloc[35]
  ayuda10= frase.iloc[36]+frase.iloc[37]+frase.iloc[38]+frase.iloc[39]
  ayuda11=frase.iloc[40]+frase.iloc[41]
  ayuda12= frase.iloc[42]+frase.iloc[43]+frase.iloc[44]+frase.iloc[45]+frase.iloc[46]
  ayuda13=frase.iloc[47]+frase.iloc[48]+frase.iloc[49]+frase.iloc[50]
  ayuda14=''
  ayudatotal=[ayuda1,ayuda2,ayuda3,ayuda4,ayuda5, ayuda6,ayuda7,ayuda8,ayuda9,ayuda10,ayuda11,ayuda12,ayuda13,ayuda14]
  df = pd.DataFrame(columns=['cluster','cantidad_de_palabras_clave','porcentaje_de_palabras_clave','principales_palabras_clave'])

  for i in range(0,13):
    df = df.append({'cluster': int(cluster.iloc[i])}, ignore_index=True)
    df['cantidad_de_palabras_clave'].fillna(int(palabras.iloc[i]),inplace=True)
    df['porcentaje_de_palabras_clave'].fillna(porcentaje.iloc[i].rstrip(" %"),inplace=True)
    df['porcentaje_de_palabras_clave'] = [float(str(j).replace(",", ".")) for j in df["porcentaje_de_palabras_clave"]]
    df['principales_palabras_clave'].fillna(ayudatotal[i], inplace=True)
  final=df
  return final
