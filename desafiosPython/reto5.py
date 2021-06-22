import pandas as pd
import csv
import urllib.request
from io import StringIO

def analizarDatos(archivo: str, porcentaje: float) -> dict:

    datos = pd.read_csv(archivo, sep=';')

    freq = datos['HORA'].value_counts() 
    listFreq = dict(freq)

    it = listFreq.items()
    hPico = list(it)[0][0]
    valor = (list(it)[0])
    valor1 = list(valor)
    valor2 = int(valor1[1])
    proy = valor2 + (valor2 * porcentaje)

    result = {'Hora pico':hPico, 'valor':valor2, 'proyección':proy}
    return result
                        
analizar = analizarDatos('https://raw.githubusercontent.com/ciaocamilo/misiontic2022/main/usos_1206.csv', 0.01)
print(analizar)