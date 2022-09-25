# Import required modules
import requests
import bs4
import pandas as pd

# Make requests from webpage
url = 'https://www.macraesbluebook.com/'
result = requests.get(url)

# Creating soap object
soup = bs4.BeautifulSoup(result.text,'lxml')

data = []

# Find the span and get data from it
for i in soup.select('.td_tab_index'):
	print(i.text)
	data.append(i.text)

# Display number of cases
print(data)



# Creating dataframe
df = pd.DataFrame({"CompanyData": data})

# Exporting data into Excel
df.to_csv('Corona_Data.csv')

		
