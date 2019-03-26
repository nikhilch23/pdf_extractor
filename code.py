import pandas as pd
import numpy as np
from urllib.request import urlopen
from bs4 import BeautifulSoup

num=1

url = "https://www.ibbi.gov.in/orders/nclt?page=" + str(num)
html = urlopen(url)

soup = BeautifulSoup(html, 'lxml')

# print(soup.prettify())

#title = soup.title
#print(title)

#ext = soup.get_text()
#print(text)

table = soup.find('table', class_="cols-4 responsive-enabled")
link = table.find_all('a')

for i in link:
	print(i)