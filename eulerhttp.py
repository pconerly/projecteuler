import httplib
import BeautifulSoup

h1 = httplib.HTTPConnection(r'projecteuler.net')
h1.request("GET", "/index.php?section=problems&id=12")
r1 = h1.getresponse()
print r1.status, r1.reason
data1 = r1.read()
print data1
