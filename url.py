#!/usr/bin/env python

from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uRqst
from urllib.parse import urljoin

web_url = input("Enter url: ")



def make_soup(web_url):

	http_client_HTTPResponse = uRqst(web_url)
	web_html = http_client_HTTPResponse.read()
	http_client_HTTPResponse.close()
	beautiful_soup = soup(web_html, "html.parser")
	return beautiful_soup


def fetch_url():

	beautiful_soup = make_soup(web_url)
	a_tags = beautiful_soup.findAll("a")
	links = [each.get('href') for each in a_tags]
	for each in links:
		if(each[0:4] == "http" or each[0:5] == "https"):
			print(each)
		else:
			full_link = urljoin(web_url,each)
			print(full_link)

	print(str(len(a_tags))+" Url links found..." )



if __name__ == '__main__':
	fetch_url()

