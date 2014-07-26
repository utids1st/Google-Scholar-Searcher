from bs4 import BeautifulSoup

import urllib2

opener = urllib2.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]

url = "http://scholar.google.com/scholar"

appendix = "?q=computer&btnG=&as_sdt=1%2C5&as_sdtp="

data = opener.open(url + appendix).read()

soup = BeautifulSoup(data)
for div in soup.find_all('div', {'class' : 'gs_r'}):
    print(div.prettify())
