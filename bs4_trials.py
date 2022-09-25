import requests
import pandas as pd
import openpyxl
import bs4

res = requests.get('https://www.macraesbluebook.com/')
soup = bs4.BeautifulSoup(res.text, 'html')

hi = soup.select('.a_mbb')
for i in hi:
	list1 = i.text
	data = list1.split()
	print(data)
	df = pd.DataFrame()
	df['Name'] = data
	for x in df['Name']:
		df.to_excel('result.xlsx', index = False)
		
