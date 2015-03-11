from bs4 import BeautifulSoup
import sys
import requests
from urlparse import urljoin


class RapScraper():
	artist=""
	BASE_URL="http://genius.com/search?q="
	def __init__(self,artist):
		artistList=artist.split()
		self.artist=("-").join(artistList)
		self.artist_URL=self.BASE_URL+"/"+self.artist+"/"
		print self.artist_URL

	def scrape(self):
		response=requests.get(self.artist_URL, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) \
			AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36'})
		lyricList=[]
		soup=BeautifulSoup(response.text,'lxml')
		for song_link in soup.select('ul.song_list > li > a'):
			link = urljoin(self.BASE_URL,song_link['href'])
			response = requests.get(link)
			soup = BeautifulSoup(response.text)
			lyrics= soup.find('div', class_='lyrics').text.strip()
			lyricList.append(lyrics)
		return lyricList

if __name__=="__main__":
	new=RapScraper("Andre 3000")
	print len(new.scrape())