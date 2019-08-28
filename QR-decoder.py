# python qr.py
#
# sudo apt-get install python-qrtools
# sudo apt-get install python-requests

from PIL import Image
from bs4 import BeautifulSoup
from html.parser import HTMLParser
import qrtools
import urllib2
import urllib          #Pour lire la page html
import requests        #Pour envoyer la requete

#Draw un "gros pixel" du QR code
def draw_square (x, y, px_map, size):
        x2 = x
        for i in range(size):
            for j in range(size):
                px_map[x2,y] = (4, 2 ,4)
                x2 += 1
            x2 = x
            y += 1

#Efface un "gros pixel" du QR code
def erase_square (x, y, px_map, size):
        x2 = x
        for i in range(size):
            for j in range(size):
                px_map[x2,y] = (255, 255 ,255)
                x2 += 1
            x2 = x
            y += 1

#Dessine un carre de positionnement de QR code 
def draw_position_square (x, y, px_map):
        px_size = 9;
        base_x = x
        base_y = y

        #Dessine le gros carre noir de base 7-7
        for i in range(7):
            for j in range(7):
                draw_square (x, y, px_map, px_size)
                y += px_size
            y = base_y
            x += px_size
        #Efface des carres noirs pour faire le carre interieur
        #Efface la ligne du haut
        y = base_y + px_size
        x = base_x + px_size
        for i in range(5):
            erase_square (x, y, px_map, px_size)
            x += px_size
        #Efface la ligne du bas
        y += px_size * 4
        x = base_x + px_size
        for i in range(5):
            erase_square (x, y, px_map, px_size)
            x += px_size
        #Efface la ligne de gauche        
        x = base_x + px_size        
        y = base_y + px_size
        for i in range(5):
            erase_square (x, y, px_map, px_size)
            y += px_size
        #Efface la ligne de droite
        x += px_size * 4
        y = base_y + px_size
        for i in range(5):
            erase_square (x, y, px_map, px_size)
            y += px_size

#Recup toutes les images de la page (ici 1 seule)
#def download_images(url, content, cookies):
#    soup = BeautifulSoup(content)
#    images = [img for img in soup.findAll('img')]
#    image_links = [each.get('src') for each in images]
#    for each in image_links:
#        ret = urllib.urlretrieve(each, "root-qr.png")

#NE MARCHE PAS PARCE QUE DOWNLOAD_IMAGE UTILISE PAS SESSION MAIS URLRETRIEVE
#En gros j'arrive pas a DL en envoyant les cookies recuperes avec session
#Donc je telecharge une image d'une autre URL

#RECUP L'IMAGE
url = "URL"
session = requests.Session()
response = session.get(url)
content = response.text 
cookies = session.cookies.get_dict()

soup = BeautifulSoup(content)
images = [img for img in soup.findAll('img')]
image_links = [each.get('src') for each in images]
url2 = "http://"+image_links[0][22:]
img_data = requests.get(url2, cookies=cookies).content
with open('root-qr.jpg', 'wb') as handler:
    handler.write(img_data)
#Reforme le QR code

#download_images(url, content, cookies) #Recup le qr depuis le site
img = Image.open("./root-qr.png")
px_map = img.load()
draw_position_square(18, 18, px_map)  #Haut gauche
draw_position_square(220, 18, px_map) #Haut droite
draw_position_square(18, 220, px_map) #Bas gauche
img.save("image2.png")
img.close()

#Traduit le QR
qr = qrtools.QR()
qr.decode("image2.png")
text = qr.data[-12:]
print ("FLAG = ", text)

#Send la reponse
values = {'metu':text}
print(session.post(url, values).text)