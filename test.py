import urllib.request   #import the library used to query a website
from bs4 import BeautifulSoup
import requests 
import os
import urllib
#wiki = "https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"

#page = urllib.request.urlopen(wiki) #Query the website and return the html to the variable 'page'
#soup = BeautifulSoup(page, 'lxml')  

#print(soup.prettify())

image_url = "https://www.python.org/static/community_logos/python-logo-master-v3-TM.png"
pdf_url = "https://ibbi.gov.in//webadmin/pdf/order/2019/Mar/12th Mar 2019 in the matter of Vadali Infotech Private Limited C.P. (IB)-4463-MB-2018_2019-03-19 15:01:36.pdf"

#r = requests.get(pdf_url)

#with open("python_logo.png",'wb') as f:
#	f.write(r.content)

#r = requests.get(image_url)

#with open("python_logo.pdf",'wb') as pdf:
#	pdf .write(r.content)


path = os.getcwd()

urllib.urlretrieve('https://ibbi.gov.in//webadmin/pdf/order/2019/Mar/12th Mar 2019 in the matter of Vadali Infotech Private Limited C.P. (IB)-4463-MB-2018_2019-03-19 15:01:36.pdf', path)

  
print ("The current working directory is %s" % path)

