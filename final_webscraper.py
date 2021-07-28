import requests
from bs4 import BeautifulSoup
import pandas

#url=input("Enter the desired url to scrape.")
url="https://www.flipkart.com/search?q=laptops&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&as-pos=1&as-type=HISTORY&as-backfill=on"
r = requests.get(url)
c = r.content	

soup = BeautifulSoup(c,"html.parser")
#print(soup.prettify)

name=[]
price=[]
rating=[]


name1=[]
price1=[]
rating1=[]


#print(name.text)

pages=soup.find_all("a",{"class":"ge-49M"})[-1].text
pages=int(pages)
#print(pages)


for x in range(0,pages,1):
	base_url="https://www.flipkart.com/search?q=laptops&otracker=AS_Query_HistoryAutoSuggest_2_0&otracker1=AS_Query_HistoryAutoSuggest_2_0&marketplace=FLIPKART&as-show=on&as=off&as-pos=2&as-type=HISTORY&as-backfill=on&page="
	url_new=base_url+str(x+1)
	print(url_new)
	print("\n")

	r = requests.get(url_new)
	c = r.content

	name=soup.find_all("div",{"class":"_4rR01T"})
	price=soup.find_all("div",{"class":"_30jeq3 _1_WHN1"})
	rating=soup.find_all("div",{"class":"_3LWZlK"})

	a=0
	for i in name: 
		
		'''
		print(name[a].text)
		print(price[a].text)
		print(rating[a].text)
		print(" \n")
		'''

		name1.append(name[a].text)
		price1.append(price[a].text)
		rating1.append(rating[a].text)

		a=a+1


df = pandas.DataFrame({'NAME':name1,'PRICES':price1,'RATINGS':rating1})

print(df)

#saving to a csv file

df.to_csv("data.csv")