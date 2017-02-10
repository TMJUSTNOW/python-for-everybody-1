# #socket for reading a file
# import socket
#
# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mysock.connect(('data.pr4e.org', 80))
# cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode()
# mysock.send(cmd)
#
# while True:
#     data = mysock.recv(512)
#     if (len(data) < 1):
#         break
#     print(data.decode())
# mysock.close()
#
#
#
# #socket for reading an image
# import socket
# import time
#
# HOST = 'data.pr4e.org'
# PORT = 80
# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mysock.connect((HOST, PORT))
# mysock.sendall(b'GET http://data.pr4e.org/cover.jpg HTTP/1.0\n\n')
# count = 0
# picture = b""
#
# while True:
#     data = mysock.recv(5120)
#     if (len(data) < 1): break
#     time.sleep(0.25)
#     count = count + len(data)
#     print(len(data), count)
#     picture = picture + data
#
# mysock.close()
#
# # Look for the end of the header (2 CRLF)
# pos = picture.find(b"\r\n\r\n")
# print('Header length', pos)
# print(picture[:pos].decode())
#
# # Skip past the header and save the picture data
# picture = picture[pos+4:]
# fhand = open("stuff.jpg", "wb")
# fhand.write(picture)
# fhand.close()
#
#
#
# #Using urllib
# import urllib.request, urllib.parse, urllib.error
#
# fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
# for line in fhand:
#     print(line.decode().strip())
#
#
#
# # Search for lines that start with From and have an at sign
# import urllib.request, urllib.parse, urllib.error
# import re
#
# url = input('Enter - ')
# html = urllib.request.urlopen(url).read()
# links = re.findall(b'href="(http://.*?)"', html)
# for link in links:
#     print(link.decode())
#
#
#
# #read a page with urllib and then extract the href attributes
# import urllib.request, urllib.parse, urllib.error
# from bs4 import BeautifulSoup
#
# url = input('Enter - ')
# html = urllib.request.urlopen(url).read()
# soup = BeautifulSoup(html, 'html.parser')
#
# # Retrieve all of the anchor tags
# tags = soup('a')
# for tag in tags:
#     print(tag.get('href', None))
#
#
#
#Exercise 1:
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    requrl = input('Enter desired url: \n')
    mysock.connect((requrl, 80))
except:
    print("Enter a valid url")
    exit()

cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())
mysock.close()



#Exercise 2:
