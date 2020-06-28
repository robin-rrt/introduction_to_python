import urllib.request, urllib.parse, urllib.error
import SSL
import xml.etree.ElementTree as ET

#ignores SSL Errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url= input('Enter URL: ' )
site= urllib.request.urlopen(url, context=ctx).read()
print('Retrieved', len(site), 'characters')
print(site.decode())

tree = ET.fromstring(site)
counts = tree.findall('.//count')
print(counts)
