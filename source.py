import requests
import os
from bs4 import BeautifulSoup
from glob import glob
from shutil import copyfile

class Translations:
	def __init__(self):
		
		# Send the initial request to Limitless and get the soup
		response = requests.get('http://limitlesstcg.com/translations/', auth=('user', 'pass'))
		html = response.text
		soup = BeautifulSoup(html, 'html.parser')
		
		# Let's get all of the cards
		self.cards = soup.findAll("div", {"class": "card-translation"})
		self.prettyCards = {}

	def getTranslations(self):
		self.op = input("English Translations? (y/n): ")

		if self.op == 'y':
			self.getEnglishCards()
			
		self.getPrettyCards()
		self.createDirectories()
		self.writeCardData()
		self.copyAdditionalFiles()
		self.saveImages()

		print("Done!")
		
	class prettyCard:
		def __init__ (self, card):
			self.name = card.findAll("span", {"class": "card-translation-name"})[0].getText().split(" (")[0]
			self.set = card.findAll("p", {"class": "card-translation-bottom"})[0].getText().lstrip().split(" ")[0]
			self.set_number = card.findAll("p", {"class": "card-translation-bottom"})[0].getText().lstrip().split(" ")[1].split('#')[1]
			self.imageName = self.set + "_" + self.set_number
			self.imageUrl = card.findAll("a")[0]['href']
			
			# Translated images aren't uploaded in the right order so I can't use them :(
			# translated_number = str(967 + int(self.set_number))
			# self.translatedImageUrl = "http://limitlesstcg.com/wp-content/media/scans/translations/" + translated_number + ".jpg"
	
	def getPrettyCards(self):
		for card in self.cards:
			prettyCard = self.prettyCard(card)
			
			# Save to global array for later
			if prettyCard.set not in self.prettyCards:
				self.prettyCards[prettyCard.set] = []
			self.prettyCards[prettyCard.set].append(prettyCard)

	def createDirectories(self):
		print("Walking users...")
		users = glob('C:/Users/*/')

		validDir = False

		while validDir == False:
			# Gets a list of users on machine
			users = [u.replace('C:/Users', '').replace('\\', '') for u in users]

			# validUsers is all users with a valid Lackey directory
			validUsers = []
			for u in users:
				if os.path.exists('C:/Users/' + u + "/Documents/LackeyCCGWin"):
					validUsers.append(u)
			print("Users with Lackey installed:", " ".join(validUsers))
			userChoice = input("Which user would you like to install to (just hit ENTER if you want installation in the current directory or not on Windows)? ")

			if userChoice in validUsers:
				self.rootDir = "C:/Users/" + userChoice + "/Documents/LackeyCCGWin/LackeyCCG/plugins/pokemon"
				validDir = True
			if userChoice == "":
				if not os.path.exists("./lackey"):
					os.mkdir("./lackey")
				self.rootDir = "./lackey"
				print("Export directory set to ./lackey")
				validDir = True

			print(userChoice, "is an invalid input.")

		print("Creating directories...")
		if not os.path.exists(self.rootDir + "/sets"):
			os.mkdir(self.rootDir + "/sets")
			if not os.path.exists(self.rootDir + "/sets/setimages"):
				os.mkdir(self.rootDir + "/sets/setimages")

		for set in self.prettyCards.keys():
			if not os.path.exists(self.rootDir + "/sets/setimages/" + set):
				os.mkdir(self.rootDir + "/sets/setimages/" + set)
			
	def writeCardData(self):
		print("Writing carddataNEW.txt...")
		file = open(self.rootDir + "/sets/carddataNEW.txt", "w")
		
		for set in self.prettyCards.keys():
			for prettyCard in self.prettyCards[set]:
				self.writeLine(file, prettyCard)

	def copyAdditionalFiles(self):
		print("Copying formats.txt...")
		copyfile("formats.txt", self.rootDir + "/formats.txt")

		print("Copying ListOfCardDataFiles.txt...")
		copyfile("ListOfCardDataFiles.txt", self.rootDir + "/ListOfCardDataFiles.txt")
		
	def writeLine(self, file, card):
		line = card.name + '\t' + card.set + '\t' + card.imageName + '\n'
		# print(line)
		file.write(line)
		
	def saveImages(self):
		imageUrl = ""

		for set in self.prettyCards.keys():
			for j in range(len(self.prettyCards[set])):
				prettyCard = self.prettyCards[set][j]
				print("Getting " + prettyCard.name + "'s image...")

				filename = self.rootDir + "/sets/setimages/" + prettyCard.set + "/" + prettyCard.imageName + ".jpg"

				# Check if file is already there
				if os.path.isfile(filename):
					print(filename + " already exists! Skipping...")
				else:
					if self.op == 'y':
						imageUrl = "http://limitlesstcg.com/wp-content/media/scans/translations/" + self.translations[set][j] + ".jpg"
					else:
						imageUrl = prettyCard.imageUrl

					r = requests.get(imageUrl, allow_redirects=True)
					open(filename, 'wb').write(r.content)

	def getEnglishCards(self):
		print("Fetching English Cards...")

		# Limitless has all of the numbers to the translated cards on this url
		# If we go here, we can scrape the HTML to get the number for each Pokemon
		# We import these numbers in a list called self.translations
		response = requests.get('http://limitlesstcg.com/translations/?view=data', auth=('user', 'pass'))
		html = response.text
		soup = BeautifulSoup(html, 'html.parser')

		# self.translations is a dictionary that files by setName, just like self.prettyCards!
		self.translations = {}
		

		for elem in soup.findAll("div", {"class": "ct-set-cards"}):

			# Throw the entire group for the set into self.translations[setName]
			# We remove everything after the number in our next loop
			setName = elem.decode_contents().split("<br/>")[0].split(",")[2]
			self.translations[setName] = elem.decode_contents().split("<br/>")

			print("Getting English Cards for " + setName + "...")

			# Remove all the ending garbage, just leave the numbers
			for i in range(len(self.translations[setName])):
				self.translations[setName][i] = self.translations[setName][i].split(",")[0]
		
t = Translations()
t.getTranslations()