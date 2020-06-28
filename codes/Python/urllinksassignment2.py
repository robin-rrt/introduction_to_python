import urllib.request , urllib.parse, urllib.error
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
for i in range(7):
   html = urlopen(url, context=ctx).read()
   soup = BeautifulSoup(html, "html.parser")
   tags = soup('a')
   tag = tags[17]
   url= tag.get('href',None)
   name= tag.contents[0]
print (name)

#for i in range(3):
    #html = urlopen(url, context=ctx).read()
    #soup = BeautifulSoup(html, "html.parser")
    #tags = soup('a')
    #tag = tags[2]
    #url= tag.get('href',None)
    #name= tag.contents[0]
    #print(name)










#for tag in tags:
    # Look at the parts of a tag
    #print('TAG:', tag)
    #print('URL:', tag.get('href', None))
    #print('Contents:', tag.contents[0])
    #print('Attrs:', tag.attrs)
