# importing the libraries and modules required
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import time

while(True):
	now = datetime.now()
	
	# time of web-scrapping
	current_time = now.strftime("%H:%M:%S")
	print(f'At time : {current_time} IST')

	response = requests.get('https://coinmarketcap.com/')
	text = response.text
	html_data = BeautifulSoup(text, 'html.parser')
	headings = html_data.find_all('tr')[0]
	headings_list = []
	for x in headings:
		headings_list.append(x.text)
	headings_list = headings_list[:10]

	data = []

	for x in range(1, 6):
		row = html_data.find_all('tr')[x]
		column_value = row.find_all('td')
		dict = {}
		
		for i in range(10):
			dict[headings_list[i]] = column_value[i].text
		data.append(dict)
		
	for values in data:
		print(values)
		print('')
	time.sleep(600)
