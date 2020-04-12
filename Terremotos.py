# Se importan las librerias que se van a usar
import requests
import csv
from bs4 import BeautifulSoup as bs
import re

# Se recupera el recurso especifico de la pagina web para trabajar con el
url = requests.get("http://ds.iris.edu/seismon/eventlist/index.phtml")

# Se indica que el valor recuperado en el url esta en formato html
soup = bs(url.content, 'html.parser')

# Se crea el fichero  en formato csv donde se va a almacenar la informacion extraida
filename = "DatasetTerremotos.csv"
csv_writer = csv.writer(open(filename, 'w'))

# Se buscar todas las lineas de la tabla y para cada una de ellas se realiza el sigueinte proceso
for tr in soup.find_all("tr"):
    # Se declara una lista vacia
    data = []
    # Se buscan todos los valores de cabeceras existentes en la linea de la tabla
    for th in tr.find_all("th"):
        # Se concatenan los valores de la cabecera, eliminando espacios y saltos de linea
        data.append(re.sub(r'(\s+|\n)', ' ', th.text.strip()))
    
    # En el caso de que existan cabeceras, se escribe la informacion en el fichero
    if data:
        csv_writer.writerow(data)
        continue

    # Se buscan todos los datos existentes en la linea de la tabla
    for td in tr.find_all("td"):
        data.append(td.text.strip())

    # En el caso de que existan datos, se escribe la informacion en el fichero
    if data:
        csv_writer.writerow(data)