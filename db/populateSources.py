import urllib2
from BeautifulSoup import BeautifulSoup
import newspaper
import sys

for source in newspaper.popular_urls():
    try: 
        soup = BeautifulSoup(urllib2.urlopen(source))
        print source + " - " + soup.title.string
    except:
        print "Error fetching ", source, "\n --> ", sys.exc_info()[0]
