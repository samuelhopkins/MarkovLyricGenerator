import sys
from LyricScrape import LyricScraper
import random
from collections import defaultdict

def noClosures(string):
	if ("[" in string or
		 "]" in string or
		 "(" in string or
		 ")" in string):
		return False
	else:
		return string

class FreestyleGenerator():
	artist=""
	wordDict=defaultdict(list)
	wordList=[]
	strength=1
	def __init__(self,artist,strength):
		self.artist=artist
		self.strength=strength



	def train(self):
		strength=self.strength
		Scraper=LyricScraper(self.artist)
		songLyricList=Scraper.scrape()
		for song in songLyricList:
			songWordList=song.split()
			length=len(songWordList)
			for i in range(length-strength):
				j=i+strength
				while (j < length-1) and (noClosures(songWordList[j]) is False):
					j+=1

				kindex=i
				keyTup=()
				step=0
				limit=strength
				while step < limit and (kindex+step < length):
					if (noClosures(songWordList[kindex+step])):
						keyTup+=(songWordList[kindex+step],)
					else:
						limit+=1
					step+=1
				self.wordDict[keyTup].append(songWordList[j])
				i=j
		self.wordList=self.wordDict.keys()
		print len(self.wordList)/(20 * Scraper.pages)

	def generate(self,length):
		self.train()
		strength=self.strength
		options=len(self.wordList)
		rand=random.randint(0,options)
		seed=self.wordList[rand]
		freeStyle=""
		for i in range(length):
			follows=self.wordDict[seed]
			followsLen=len(follows)
			nextTup=()
			for j in range(1,strength):
				nextTup+=(seed[j],)

			randNextInt=random.randint(0,followsLen)
			next=follows[randNextInt]
			freeStyle+=" "+next
			nextTup+=(next,)
			seed=nextTup
		

		return freeStyle



if __name__=="__main__":
	new=FreestyleGenerator(sys.argv[1],int(sys.argv[2]))
	print new.generate(int(sys.argv[3]))



