# Example Task 0 - Grabbing the title of a page

import requests

# Step 1: Use the requests library to grab the page
# Note, this may fail if you have a firewall blocking Python/Jupyter 
# Note sometimes you need to run this twice if it fails the first time
res = requests.get("http://www.example.com")

# print(type(res)) # <class 'requests.models.Response'>

# print(res.text)

import bs4

soup = bs4.BeautifulSoup(res.text,"lxml")

# print(soup)

title_tag = soup.select('title')

# print(title_tag) # [<title>Example Domain</title>]

p_tag = soup.select('p')

# print(p_tag) # 

h1_tag = soup.select('h1')

# print(h1_tag) #


# print(title_tag[0].getText()) # Example Domain


# Example Task 1 - Grabbing all elements of a class

# First get the request
res = requests.get('https://en.wikipedia.org/wiki/Grace_Hopper')

# Create a soup from request
soup = bs4.BeautifulSoup(res.text,"lxml")

# print(soup)

# print(soup.select(".vector-settings"))

first_item = soup.select(".vector-settings")[0]

# print(first_item.getText())

# Example Task 3 - Getting an Image from a Website

res = requests.get("https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)")

soup = bs4.BeautifulSoup(res.text,'lxml')

image_info = soup.select('.thumbimage')

# print(image_info)

# print(len(image_info))

computer = image_info[0]

# print (type(computer))

# print(computer['src'])

image_link = requests.get('https://upload.wikimedia.org/wikipedia/commons/thumb/b/be/Deep_Blue.jpg/399px-Deep_Blue.jpg')

# print(image_link.content)

f = open('my_new_file_name.jpg','wb')

f.write(image_link.content)

f.close()

# Example Project - Working with Multiple Pages and Items

base_url = 'http://books.toscrape.com/catalogue/page-{}.html'

res = requests.get(base_url.format('1'))

soup = bs4.BeautifulSoup(res.text,"lxml")

# print(soup.select(".product_pod"))

products = soup.select(".product_pod")

example = products[0]

# print(type(example))

# print(example.attrs)

# print(list(example.children))

# print(example.select('.star-rating.Three'))

# print(example.select('.star-rating.Two'))

# print(example.select('a'))

# print(example.select('a')[1])

print(example.select('a')[1]['title'])