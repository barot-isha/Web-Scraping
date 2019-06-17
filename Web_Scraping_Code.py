import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline

import bs4 as bs
from bs4 import BeautifulSoup
from urllib.request import urlopen #we are importing requests library
import sys
import urllib.request 
from PyQt5.QtWebEngineWidgets import QWebEnginePage
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl
from pandas import DataFrame

import requests
url = "en.wikipedia.org/wiki/List_of_United_States_cities_by_population"
r  = requests.get("http://" +url)
html = r.text

soup = BeautifulSoup(html,'lxml') #Beautiful Soup is a Python package for parsing HTML and XML documents
print(soup.prettify()) #Prettify() function in BeautifulSoup will enable us to view how the tags are nested in the document

all_tables=soup.find_all('table')
print(all_tables)

right_table=soup.find('table', class_='wikitable sortable')
print(right_table)

links= right_table.findAll('a')
print(links)

Countries=[]
for link in links:
    Countries.append(link.get('title'))

print(Countries)

df= pd.DataFrame()
df['Country'] = Countries
df.fillna(value=pd.np.nan, inplace=True)
df=df.dropna()
df = df.reset_index(drop=True)
print(df)

df.to_csv("final_scrapdata.csv")