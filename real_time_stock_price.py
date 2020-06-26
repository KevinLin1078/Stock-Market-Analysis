def main():
	global price_text
	import requests, time, datetime
	from bs4 import BeautifulSoup

	first, last, symbols = "https://markets.businessinsider.com/stocks/", "-stock", [ 'dal', 'ba', 'dis']


	while(True):
		temp= []
		pages = [requests.get(first + symbol + last ) for symbol in symbols]
		for i, page in enumerate(pages):
			soup = BeautifulSoup(page.content, 'html.parser')
			price = soup.find('span', class_="push-data aktien-big-font text-nowrap no-padding-at-all").contents 
			timing =  soup.find('span', class_="push-data", attrs={"data-format" : "utcToApplicationOffset:-4;"}).contents
			temp.append(" ".join( [ symbols[i].upper()  ,price[0]  ]))
			
		print(temp)
				

		del temp, pages
		
		time.sleep(30)



main()
