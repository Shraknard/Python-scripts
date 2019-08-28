#IRC code example

from __future__ import division
import os
import random
import socket
import sys
import time
import math

channel = "#Chan"
server = "irc.server"
botnick = "yoloswag24"

irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)                                 #cree un socket
print "connecting to:"+server
irc.connect((server, 6667))                                                             #connects to the server
irc.send("USER " + botnick + " " + botnick +" " + botnick + " :This is a fun bot!\n")   #user authentication
irc.send("NICK " + botnick + "\n")
irc.send("JOIN " + channel + "\n")                                                      #join the chan

while 1:
    text = irc.recv(4096)
    print text

    if text.find('PING') != -1:                                         #check if 'PING' is found
        irc.send('PONG ' + text.split() [1] + '\r\n')                   #Return 'PONG' back to the server (prevents pinging out!)
        irc.send("PRIVMSG Candy : !ep2\r\n")                            #join the chan
    if text.find('Candy'):
            if "BOT PRIVMSG yoloswag24" in text:                        #On check que les cas ou il y a Candy
                    s = text.split('\n')
                    s2 = s[10].split(':')
                    res = s2[2].decode('base64')                        #Decode le base64
                    irc.send("PRIVMSG Candy :!ep2 -rep "+str(res)+"\n") #On envoi la reponse au bot
            time.sleep(2)                                               #Sleep pour eviter de spam le serveur
