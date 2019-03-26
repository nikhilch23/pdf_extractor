import urllib.request   #import the library used to query a website
from bs4 import BeautifulSoup
import requests 
#wiki = "https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"

#page = urllib.request.urlopen(wiki) #Query the website and return the html to the variable 'page'
#soup = BeautifulSoup(page, 'lxml')  

#print(soup.prettify())

image_url = "https://www.python.org/static/community_logos/python-logo-master-v3-TM.png"

r = requests.get(image_url)

with open("python_logo.png",'wb') as f:
	f.write(r.content)

	