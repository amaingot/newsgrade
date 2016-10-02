import urllib2
from BeautifulSoup import BeautifulSoup
import newspaper
import settings
import sys
import MySQLdb as mdb

con = mdb.connect(settings.db_endpoint, settings.db_username,  
                  settings.db_password, settings.db_name)

for source in newspaper.popular_urls():
    try: 
        soup = BeautifulSoup(urllib2.urlopen(source))
        print source + " - " + soup.title.string
        cur = con.cursor()

        cmd = 'INSERT INTO newsgrade.sources' + '(name, url, last_fetched, last_error, source_type, source_subtype, metadata)' + 'VALUES (' + soup.title.string + ', ' + source + ', NULL, NULL, "news", NULL,NULL);'
        cur.execute(cmd)
        print "success!"
        exit()
    except:
        print "Error fetching ", source, "\n --> ", sys.exc_info()
        exit()
