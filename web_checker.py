import urllib2
import requests
def search():
     web=raw_input("insert web site(without www.,ex:google.co.id,youtube.com):")
     req=urllib2.urlopen("http://www."+web,timeout=5).getcode==200
     print "Web exist"
   
a=True
try:
    
 search()        

     
except urllib2.URLError as e:
    print "Web not found"
    search()
except socket.timeout as e:
    print "request timed out"
    search()
