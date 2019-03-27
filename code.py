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


count1 = 0
count2 = 0
count3 = 0
count4 = 0
for x in range(1,2):

	url = "https://www.ibbi.gov.in/orders/nclt?page=" + str(x)
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
	date=""
	num=1
	for j in row:
		c=0
		column = j.find_all('td')
		for k in column:
			c=c+1
			if c==3:
				orderstag = str(k)
				index = re.search("[A-Z]",orderstag).start()
				orders = orderstag[index:-6].strip()
			if c==1:
				datetag = str(k)
				index4 = re.search("[0-9]",datetag).start()
				date = datetag[index4:-6].strip()		
			links = j.find('a')
			string = str(links)
			index1 = re.search("https", string).start()
			index2 = re.search(";", string).start()
			link = str(links)[index1:index2-2]	
		pdf_url = link	
		if num!=1:
			if orders == "ADMITTED":
				r = requests.get(pdf_url)
				with open("ADMITTED/"+date+"_"+str(count1)+".pdf",'wb') as pdf:
					pdf.write(r.content)
				print(date+"_"+str(count1)+".pdf"+" downloaded"+"in ADMITTED folder")
				count1 = count1 + 1
			if orders == "OTHERS":
				r = requests.get(pdf_url)
				with open("OTHERS/"+date+"_"+str(count2)+".pdf",'wb') as pdf:
					pdf.write(r.content)
				print(date+"_"+str(count2)+".pdf"+" downloaded")
				count2 = count2 + 1
			if orders == "RESOLUTION":
				r = requests.get(pdf_url)
				with open("RESOLUTION/"+date+"_"+str(count3)+".pdf",'wb') as pdf:
					pdf.write(r.content)				
				print(date+"_"+str(count3)+".pdf"+" downloaded")
				count3 = count3 + 1
			if orders == "LIQUIDATION":
				r = requests.get(pdf_url)
				with open("LIQUIDATION/"+date+"_"+str(count4)+".pdf",'wb') as pdf:
					pdf.write(r.content)				
				print(date+"_"+str(count4)+".pdf"+" downloaded")
				count4 = count4 + 1								
		num = num+1
