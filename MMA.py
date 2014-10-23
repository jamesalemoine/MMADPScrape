from bs4 import BeautifulSoup
import requests, json
mma = []
url = "collection/the-collection-online/search/629772?rpp=30&pg=1&rndkey=20141023&ft=*&deptids=9&when=A.D.+1600-1800&where=Europe&pos=1"
with open ("Met.json", "w") as file:
	next_link = True
	while next_link != None:	
		url = "http://www.metmuseum.org/" + url
		link = requests.get(url)
		link_html = link.text
		soup = BeautifulSoup(link_html)
		artist_tag = soup.find_all("h2")
		for artist_item in artist_tag:
			print (artist_item.text)
			artist_name = artist_item.text
		title_tag = soup.find_all("h3")
		for title_item in title_tag:
			print (title_item.text)
			title = title_item.text
		info_tag = soup.find_all("div", attrs={"class" : "tombstone"})
		for info_item in info_tag:
			print(info_item.text)
		next_link = soup.find("a", attrs={"class" : "next"})
		if next_link != None:
			url = next_link["href"]
		one_object = { "Artist" : artist_item.text, "Title" : title_item.text, "Info" : info_item.text}
		mma.append(one_object)
		file.write(json.dumps(mma, indent=4))
print ("Done!!")

