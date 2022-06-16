import requests
import random
from bs4 import BeautifulSoup
from bs4 import SoupStrainer
import tkinter as tk

# This is a program that will produce motivational quotes on screen

# Function to create a pop up window 
def popupmsg(msg, title):
	root = tk.Tk()
	root.title(title)
	label = tk.Label(root, text=msg)
	label.pack(side="top",fil="x",pady=10)
	B1 = tk.Button(root, text="Close", command=root.destroy)
	B1.pack()
	root.mainloop()

# website to be scraped for quotes
url = "https://www.shopify.com/blog/motivational-quotes"

# Accessing a webiste and getting the html data
urlResponse = requests.get(url) # variable to hold the response to the request in a string
onlyOlTags = SoupStrainer('ol')
htmlSoup = BeautifulSoup(urlResponse.text, 'html.parser',parse_only=onlyOlTags)

######### DEBUGGING #########
print(urlResponse.text)

# list of quotes 
quotes = []
# finding all of the tags that are a list of quotes
quoteTags = htmlSoup.find_all(lambda tag: tag.name == 'li' and not tag.attrs)
for tag in quoteTags:
	quotes.append(tag.text)

# randomly picking a quote to display
random.seed()
quoteIndex = random.randint(0,len(quotes)-1)
displayQuote = quotes[quoteIndex]

# creating a pop up window to display the quote
popupmsg(displayQuote, "Motivational Quote")