from bs4 import BeautifulSoup
import requests, csv
artist_lines = []
title_line = []
object_info_lines = [] 
for i in range (307):
	payload = {"pg" : i}
	link = requests.get("http://www.metmuseum.org/collection/the-collection-online/search?where=Europe&noqs=true&ft=*&deptids=9&when=A.D.+1600-1800&rpp=90&", params = payload)
	link_html = link.text
	with open ("MMA_Search_Results,_Drawings,_Europe,_1600-1800_Artists.csv","w") as file:
		with open ("MMA_Search_Results,_Drawings,_Europe,_1600-1800_Title.csv","w") as f:
			with open ("MMA_Search_Results,_Drawings,_Europe,_1600-1800_Object_Info.csv", "w") as g:	
				soup = BeautifulSoup(link_html)
				artist_tag = soup.find_all("div", attrs={"class" : "artist"})
				artist_name = str(artist_tag)
				artist_lines.append(artist_name, "\n")
				title_tag = soup.find_all("div", attrs={"class" : "objtitle"})
				title = str(title_tag)
				title_line.append(title, "\n")
				info_tag = soup.find_all("div", attrs={"class" : "objectinfo"})
				info = str(info_tag)
				object_info_lines.append(info, "\n")
				file.writelines(artist_lines)
				f.writelines(title_line)
				g.writelines(object_info_lines)
				print (artist_lines, title_line, object_info_lines)
print ("Done!!")
