import requests
from bs4 import BeautifulSoup as B
inp = input()

link = 'http://hindi-english.org/index.php?inp='+inp
page = requests.get(link)
soup = B(page.content,"html.parser")
lis = []
for td in soup.find_all("td"):
	for a in td.find_all('a'):
		lis.append(a.getText())
print(lis[1])