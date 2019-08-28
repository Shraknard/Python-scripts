#s = requests.Session() -> all cookies received will be stored in the session object

import urllib2
from html.parser import HTMLParser
import re
import requests

response = urllib2.urlopen('URL')
html = response.read()
headers = response.info().headers

print response.info().
print response.json

#PARSING
tab = html.split(' ')

n = 0
i = 0
Un1 = 0
for p in tab:
        if i == 12:
                a = int(p)
        elif i == 20:
                b = int(p)
        elif i == 16:
                op = p
        elif i == 24:
                p = p[:-5]
                Un = int(p)
        elif i == 28:
                p = p[:-9]
                p = p[-6:]
                Umax = int(p)
        i += 1

#CALCUL
while Un <= Umax:
        Un1 = (a + Un)
        if op == "+":
                Un1 += n * b
        else:
                Un1 -= n * b        
        Un += 1
print Un

#ENVOI DE LA REPONSE
url = "URL/ep1_v.php?result=" + str(Un)
r = requests.get(url, headers=headers)
print r.text
