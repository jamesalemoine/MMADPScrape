from bs4 import BeautifulSoup
import requests, csv
line = []
for i in range (307):
	payload = {"pg" : i}
	link = requests.get("http://www.metmuseum.org/collection/the-collection-online/search?where=Europe&noqs=true&ft=*&deptids=9&when=A.D.+1600-1800&rpp=90&", params = payload)
	link_html = link.text
	with open ("MMA_Search_Results,_Drawings,_Europe,_1600-1800.csv","w") as file:
		soup = BeautifulSoup(link_html)
		artist_tag = soup.find_all("div", attrs={"class" : "artist"})
		artist_name = str(artist_tag)
		line.append(artist_name)
		title_tag = soup.find_all("div", attrs={"class" : "objtitle"})
		title = str(title_tag)
		line.append(title)
		info_tag = soup.find_all("div", attrs={"class" : "objectinfo"})
		info = str(info_tag)
		line.append(info)
		file.writelines(line)
		print (line)
print ("Done!!")
