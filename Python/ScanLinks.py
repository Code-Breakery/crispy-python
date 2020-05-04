#Anshul raj
# Day on created :- May 4th 2020
import requests
from bs4 import BeautifulSoup as B
path = input("Input folder path : ") or '.'
url = input('Input link path : ')
page = requests.get(url)
soup = B(page.content,'html.parser')
with open(path+'/Page.html','w') as html:
	html.write(soup.prettify())
	html.close()
lst = []
for link in soup.find_all("a"):
	lst.append(link['href']+'\n')
with open(path+'/links.txt','w') as links:
	for item in lst:
	  if item.startswith("http") == False:
	  	links.write(url+item)
	  links.write(item)