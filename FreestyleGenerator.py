import sys
from RapScrape import RapScraper
import random
from collections import defaultdict


class FreestyleGenerator():
	artist=""
	wordDict=defaultdict(set)
	wordList=[]
	def __init__(self,artist):
		self.artist=artist


	def train(self):
		songLyricList=RapScraper(self.artist).scrape()
		for song in songLyricList:
			songWordList=song.split()
			length=len(songWordList)
			for i in range(length-1):
				self.wordDict[songWordList[i]].add(songWordList[i+1])
		
		self.wordList=self.wordDict.keys()

	def generate(self,artist,length):
		self.train()
		options=len(self.wordList)
		rand=random.randint(options)
		seed=self.wordList[rand]
		freeStyle=""
		for i in range(length):
			follows=self.wordDict[seed]
			followsLen=len(follows)
			randNextInt=random.randint(0,followsLen)
			next=follows[randNextInt]
			freeStyle+=" "+next
			seed=next
		

		return freeStyle

	def generate(self,length):
		self.train()
		options=len(self.wordList)
		rand=random.randint(0,options)
		print options
		seed=self.wordList[rand]
		freeStyle=""
		for i in range(length):
			follows=list(self.wordDict[seed])
			followsLen=len(follows)
			randNextInt=random.randint(0,followsLen-1)
			next=follows[randNextInt]
			freeStyle+=" "+next
			seed=next

		return freeStyle

if __name__=="__main__":
	new=FreestyleGenerator("Eminem")
	print new.generate(40)


