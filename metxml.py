
import xml.etree.ElementTree as etree

from xml.etree.ElementTree import Element, SubElement, ElementTree

root = Element('index')

import csv

from bs4 import BeautifulSoup

import requests

import json



number = 1

url = "collection/the-collection-online/search?where=Europe&deptids=9&when=A.D.+1600-1800&rpp=90&pg=1"
next_link = True

while next_link != None:
	url = 'http://www.metmuseum.org/' + url
	painting_page = requests.get(url)

	if painting_page.status_code != 200:	
		print ("There was an error with", url)

	page_html = painting_page.text
	soup = BeautifulSoup(page_html)

	artist = soup.find(attrs = {"class" : "artist"})
	title = soup.find(attrs = {"class" : "objtitle"})
	info = soup.find(attrs = {"class" : "objectinfo"})

	next_link = soup.find("a",text="Next")

	if next_link != None:
		url = next_link['href']

		number = number + 1


	child = SubElement(root, 'work')
	subChild = SubElement(child, 'number')
	subChild.text = str(number)
	subChild = SubElement(child, 'artist')
	subChild.text = str(artist.text)
	subChild = SubElement(child, 'title')
	subChild.text = str(title.text)
	subChild = SubElement(child, 'info')
	subChild.text = str(info.text)

ElementTree(root).write("met.xml")







