#Web Scraping 
#import library yang dibutuhkan
from unicodedata import name
import pandas as pd
import requests
from bs4 import BeautifulSoup
import os.path
from re import search
from re import sub

namefile = os.path.basename(__file__)[:-3]
namefile = namefile[search("_", namefile).start()+1:]

#buatlah request ke website
website_url = requests.get('https://id.wikipedia.org/wiki/Demografi_Indonesia').text
soup = BeautifulSoup(website_url, 'html.parser')

#ambil table dengan class 'wikitable sortable'
# my_table = soup.find('table', {'class':'wikitable'})
my_table = soup.find_all('table')[1]

#cari data dengan tag 'td'
links = my_table.find_all('td')

#buatlah lists kosong 
pulau = []
populasi = []
persentase = []

#memasukkan data ke dalam list berdasarkan pola HTML
for i, link in enumerate(links):
	if i in range(0, len(links), 3):
		pulau.append(link.get_text()[:-1])
	if i in range(1, len(links), 3):
		populasi.append(int(float(sub(',','.',link.get_text()[:-1]))*1000000))
	if i in range(2, len(links), 3):
		persentase.append(sub(',','.',link.get_text()[:-1]))

#buatlah DataFrame dan masukkan ke CSV
df = pd.DataFrame()
df['Pulau'] = pulau
df['Populasi'] = populasi
df['Persentase'] = persentase
df.to_csv(namefile.title() +'.csv' , index=False, encoding='utf-8', quoting=1)
print(df)