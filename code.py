import pandas as pd
import numpy as np
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import requests
import os


try:
	path = os.path.join(os.getcwd(),"ADMITTED")
	os.mkdir(path)
except:
	pass
try:
	path = os.path.join(os.getcwd(), "OTHERS")
	os.mkdir(path)
except:
	pass
try:
	path = os.path.join(os.getcwd(), "RESOLUTION")
	os.mkdir(path)
except:
	pass
try:
	path = os.path.join(os.getcwd(), "LIQUIDATION")
	os.mkdir(path)
except:
	pass	


x = 0
for num in range(1,1):

	url = "https://www.ibbi.gov.in/orders/nclt?page=" + str(num)
	html = urlopen(url)

	soup = BeautifulSoup(html, 'lxml')

# print(soup.prettify())

#title = soup.title
#print(title)

#ext = soup.get_text()
#print(text)

	table = soup.find('table', class_="cols-4 responsive-enabled")

	row = table.find_all('tr')

	orders=""
	link=""
	datetag=""
	num=1
	for j in row:
		c=0
		column = j.find_all('td')
		for k in column:
			c=c+1
			#if c==3:
			#	orderstag = str(k)
			#	index = re.search("[A-Z]",orderstag).start()
			#	orders = orderstag[index:-6].strip()
			if c==1:
				datetag = str(k)
		print(datetag)
'''	
			links = j.find('a')
			string = str(links)
			index1 = re.search("https", string).start()
			index2 = re.search(";", string).start()
			link = str(links)[index1:index2-2]	
		pdf_url = link	
		if num!=1:
			if orders == "ADMITTED":
				try:
					r = requests.get(pdf_url)
					with open("ADMITTED/file" +str(x)+ ".pdf",'wb') as pdf:
						pdf.write(r.content)
				except:
					pass
			if orders == "OTHERS":
				try:
					r = requests.get(pdf_url)
					with open("OTHERS/file" +str(x)+ ".pdf",'wb') as pdf:
						pdf.write(r.content)
				except:
					pass
			if orders == "RESOLUTION":
				try:
					r = requests.get(pdf_url)
					with open("RESOLUTION/file" +str(x)+ ".pdf",'wb') as pdf:
						pdf.write(r.content)
				except:
					pass
			if orders == "LIQUIDATION":
				try:
					r = requests.get(pdf_url)
					with open("LIQUIDATION/file" +str(x)+ ".pdf",'wb') as pdf:
						pdf.write(r.content)
				except:
					pass								
			print("File "+str(x)+" Downloaded")
		num = num+1	
		x = x+1
'''
"""
for i in link:
	string = str(i)
	index1 = re.search("https", string).start()
	index2 = re.search(";", string).start()
	print(str(i)[index1:index2-2])	
"""	