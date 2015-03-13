
def speech_urls(sub_pages_url):
    """Returns all the speech URLs extentions for a given sub-pages URL"""
    
    import urllib2,sys
    from bs4 import BeautifulSoup

    #Base Page
    soup = BeautifulSoup(urllib2.urlopen(sub_pages_url).read())
	
    #Speech URLs
    content = soup.find("div", {"class":"view-content"})
    speeches = ["".join(x.findAll("a")) for x in content.findAll(href=True)]
    
    base_url = "http://www.whitehouse.gov"

    try:
        f=open('speechurls.csv', 'a')
        for link in content.findAll('a', href=True):
            ext = link['href']
            speech_url = base_url+ext
            f.write(u'%s\n' % (speech_url))
    finally:
        f.close()

    """
    for link in content.findAll('a', href=True):
        ext = link['href']
        print base_url+ext
    """

    #print speeches




#speech_urls("http://www.whitehouse.gov/briefing-room/Speeches-and-Remarks/2009/09?page=2")


#speech_urls("http://www.whitehouse.gov/briefing-room/Speeches-and-Remarks/2013/03?page=1")

#speech_urls("http://www.whitehouse.gov/briefing-room/Speeches-and-Remarks/2015/02?page=0")
