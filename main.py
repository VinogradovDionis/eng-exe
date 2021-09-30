import eel
import requests
from bs4 import BeautifulSoup
import random


@eel.expose
def words():

	url = 'http://poligloty.blogspot.com/2013/08/1000-english-words.html'
	response = requests.get(url)
	soup = BeautifulSoup(response.text, 'lxml')
	quotes = soup.find_all('span', face="Verdana, sans-serif")

	a = []
	n = 0
	for quote in quotes:
	    a.append(quote.text)
	    random.shuffle(a)
	b =[]
	for i in range(30):
	    b.append(a[i])
	#b = "\n".join(map(str, b))
	for j in range(30):
	    return b[j]

	
	
print(words())


eel.init("web")
eel.start("main.html", size=(700,700))