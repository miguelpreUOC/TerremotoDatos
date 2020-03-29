import requests
import csv
from bs4 import BeautifulSoup as bs
import re

url = requests.get("http://ds.iris.edu/seismon/eventlist/index.phtml")
soup = bs(url.content, 'html.parser')

filename = "DatasetTerremotos.csv"
csv_writer = csv.writer(open(filename, 'w'))


for tr in soup.find_all("tr"):
    data = []
    for th in tr.find_all("th"):
        data.append(re.sub(r'(\s+|\n)', ' ', th.text.strip()))
    
    if data:
        print("Inserting headers : {}".format(','.join(data)))
        csv_writer.writerow(data)
        continue

    for td in tr.find_all("td"):
        data.append(td.text.strip())
    
    if data:
        print("Inserting data: {}".format(','.join(data)))
        csv_writer.writerow(data)