from bs4 import BeautifulSoup
import requests
import re
start = "https://forums.atomicmassgames.com/forum/24-star-wars-legion-rules-questions/"
url = "https://forums.atomicmassgames.com/forum/24-star-wars-legion-rules-questions/page/{}"
req = requests.get(start)


soup = BeautifulSoup(req.text, features="lxml")

#check info on page
metaData = soup.find_all('span', {'class' : 'ipsType_break ipsContained'})
#print(metaData)

##metaDataLinks = [a for a in metaData]
##print(metaDataLinks)

# define where we will store info
titles = []
urls = []

# now we iterate through the metaData
print("Parsing data...")
for link in metaData:
	urls.append(re.sub(",","",link.a.get('href')))
	titles.append(re.sub(",","",link.get_text('title', strip=True)))
	
#iterate the pages

for page in range(2, 5):
	soup = BeautifulSoup(requests.get(url.format(page)).text, features="lxml")
	print(page)

	#check info on page
	metaData = soup.find_all('span', {'class' : 'ipsType_break ipsContained'})
	#print(metaData)

	##metaDataLinks = [a for a in metaData]
	##print(metaDataLinks)

	# now we iterate through the metaData
	print("Parsing data...")
	for link in metaData:
		urls.append(re.sub(",", "",link.a.get('href')))
		titles.append(re.sub(",","",link.get_text('title', strip=True)))
	
		

#showyourwork
##print(titles)
##print(urls)

import csv
myarr = []
myarr = zip(titles, urls)
##print(myarr)

with open("amgparse.csv", "w") as f:
	writer = csv.writer(f, delimiter='\t')
	writer.writerows(myarr)
	

# with open("amgparse.txt", "w") as g:
	# for element in myarr:
		# g.writelines(element)
		# g.writelines('/n')

print("scrape complete")

import compareparse