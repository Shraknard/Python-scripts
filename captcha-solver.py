# Pour installer pytesseract
# sudo apt update
# sudo apt install tesseract-ocr
# sudo apt install libtesseract-dev
# pip3 install pytesseract
# sudo apt-get install python-requests
# text = pytesseract.image_to_string(Image.open("image.png"), lang='eng', config='--psm 7')

from PIL import Image
from bs4 import BeautifulSoup
from html.parser import HTMLParser
import urllib2
import urllib
import pytesseract
import requests
import os
import re              #regular expression
import sys

#RECUP IMAGE
url = "URL"
response = urllib2.urlopen(url)
content = response.read() 
html = content.decode("utf8") #trad bytecode in html
headers = response.info().headers
print("HEADERS = ")
print(headers)

dicts = {}
for parts in headers:
        tmp = parts.split(':', 1)
        tmp[1] = tmp[1][:-2]
        tmp[1] = tmp[1][1:]
        dicts.update({tmp[0]: tmp[1]})
print(dicts)
headers = dicts

#PARSING
tab = html.split(' ')
str2 = tab[10][:-1];
str2 = str2[27:]
str1 = "http://" + str2

def make_soup(url):
    html = urllib2.urlopen(url).read()
    return BeautifulSoup(html)

def get_images(url):
    soup = make_soup(url)
    #this makes a list of bs4 element tags
    images = [img for img in soup.findAll('img')]
    print (str(len(images)) + "images found.")
    print('Downloading images to current working directory.')
    #compile our unicode list of image links
    image_links = [each.get('src') for each in images]
    for each in image_links:
        filename=each.split('/')[-1]
        print("Name = " + filename)
               urllib.urlretrieve(each, filename)
    return filename

filename = get_images(url)

#Ouvre l'image et vire les pixels noirs
img = Image.open(filename)
px_map = img.load()
for i in range(img.size[0]):
    for j in range(img.size[1]):
        if px_map[i,j] == (0, 0, 0):
            px_map[i,j] = (255, 255 ,255)
img.save("image2.png")
img.close()

img = Image.open('image2.png')
text = pytesseract.image_to_string(img, lang='eng', config='--psm 7')
print("FLAG : " +text)
img.close()

print("YOLO2")
values = {'cametu':text}
r = requests.post(url, headers=headers, params=values)

print("YOLO3")
print("R = ")
print(r)

