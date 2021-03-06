import pandas as pd
import numpy as np
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import requests
import os

folders = ['ADMITTED', 'OTHERS', 'RESOLUTION', 'LIQUIDATION']
for f in folders:
	path = os.path.join(os.getcwd(),f)
	if not os.path.exists(path):
		os.mkdir(path)

count = 0
for x in range(1,160):

	url = "https://www.ibbi.gov.in/orders/nclt?page={}".format(x)
	html = urlopen(url)
	soup = BeautifulSoup(html, 'lxml')
	table = soup.find('table', class_="cols-4 responsive-enabled")
	rows = table.find_all('tr')


	for row in rows[1:]:
		date = list(row.children)[1].get_text().strip()
		orders = list(row.children)[-2].get_text().strip()
		pdf_url = row.find('a')
		index1 = re.search("https", str(pdf_url)).start()
		index2 = re.search(";", str(pdf_url)).start()
		pdf_url = str(pdf_url)[index1:index2-2]			

		if count == 0:
			pass
		else:
			if orders in folders:
				r = requests.get(pdf_url)
				with open("{order}/{date}_{count}.pdf".format(order=orders,date=date, count=count),'wb') as pdf:
					pdf.write(r.content)
				print("{date}_{count}.pdf downloaded in {order} folder".format(date=date, count=count, order=orders))
		count = count + 1
