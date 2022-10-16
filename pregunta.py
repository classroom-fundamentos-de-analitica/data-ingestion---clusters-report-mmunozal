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

    df = pd.read_fwf(
        "clusters_report.txt", widths = [8,10,20,100], header = None,
        names = ["cluster","cantidad_de_palabras_clave","porcentaje_de_palabras_clave", "-"],
        skip_blank_lines = False, converters = {"porcentaje_de_palabras_clave": 
        lambda x: x.rstrip(" %").replace(",",".")}).drop([0,1,2,3], axis=0)

    porcentaje = df["-"]
    df = df[df["cluster"].notna()].drop("-", axis=1)
    df = df.astype({ "cluster": int, "cantidad_de_palabras_clave": int, "porcentaje_de_palabras_clave": float})

    porcentaje_total = []
    text = ""
    for lin in porcentaje:
        if isinstance(lin, str): text += lin+" "
        else:
            text = ", ".join([" ".join(x.split()) for x in text.split(",")])
            porcentaje_total.append(text.rstrip("."))
            text = ""
            continue

    df["principales_palabras_clave"] = porcentaje_total

    return df
