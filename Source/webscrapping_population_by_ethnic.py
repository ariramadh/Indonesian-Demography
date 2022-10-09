#Web Scraping 
#import library yang dibutuhkan
import pandas as pd
import requests
from bs4 import BeautifulSoup

#buatlah request ke website
website_url = requests.get('https://id.wikipedia.org/wiki/Demografi_Indonesia').text
soup = BeautifulSoup(website_url, 'html.parser')

#ambil table dengan class 'wikitable sortable'
# my_table = soup.find('table', {'class':'wikitable'})
my_table = soup.find_all('table')[3]

#cari data dengan tag 'td'
links = my_table.find_all('td')

#buatlah lists kosong 
suku = []
populasi = []
persentase = []

#memasukkan data ke dalam list berdasarkan pola HTML
for i, link in enumerate(links):
	if i in range(0, len(links), 3):
		suku.append(link.get_text())
	if i in range(1, len(links), 3):
		populasi.append(link.get_text())
	if i in range(2, len(links), 3):
		persentase.append(link.get_text()[:-1])

#buatlah DataFrame dan masukkan ke CSV
df = pd.DataFrame()
df['Kelompok Suku Bangsa'] = suku
df['Populasi'] = populasi
df['Persentase'] = persentase
df.to_csv('Population_by_Ethnic.csv' , index=False, encoding='utf-8', quoting=1)
print(df)