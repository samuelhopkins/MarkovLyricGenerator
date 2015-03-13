import sys
from LyricScrape import LyricScraper
import random
import threading
from collections import defaultdict

#Neccessary to get rid of strings deliniating verses and chorus i.e. [Verse x2]
def noClosures(lyrics):
	for string in lyrics:
		if ("[" in string or
			 "]" in string or
			 "(" in string or
			 ")" in string):
			lyrics.remove(string)
	

class FreestyleGenerator():
	artist=""
	wordDict=defaultdict(list)
	wordList=[]
	def __init__(self,artist,strength):
		self.artist=artist
		#Correlation strength 
		self.strength=strength



	def train(self):
		strength=self.strength
		Scraper=LyricScraper(self.artist)
		songLyricList=Scraper.scrape()
		for song in songLyricList:
			songWordList=song.split()
			noClosures(songWordList)
			length=len(songWordList)
			for i in range(length-strength):
				keyTup=()
				step=0
				j=i
				while (step<strength):
					keyTup+=(songWordList[j],)
					j+=1
					step+=1
				self.wordDict[keyTup].append(songWordList[j])
		self.wordList=self.wordDict.keys()

#generate will generate a freestyle of "length" many words
	def generate(self,length):
		strength=self.strength
		options=len(self.wordList)
		rand=random.randint(0,options)
		seed=self.wordList[rand]
		freeStyle=u""
		for i in range(length):
			follows=self.wordDict[seed]
			followsLen=len(follows)
			if followsLen is 0:
				seed=self.wordList[random.randint(0,options-1)]
				i-=1
				continue
			nextTup=()
			nextTup+=seed[1:]
			randNextInt=random.randint(0,followsLen-1)
			next=follows[randNextInt]
			freeStyle+=" "+unicode(next)
			nextTup+=(next,)
			seed=nextTup
		

		return freeStyle






