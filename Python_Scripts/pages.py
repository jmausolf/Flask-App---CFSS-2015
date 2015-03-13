
def pages(url):
    """Returns the number of additional pages for a given parent URL"""
    
    import urllib2,sys
    from bs4 import BeautifulSoup

    #Base Page
    soup = BeautifulSoup(urllib2.urlopen(url).read())
	
    #Page Counter
    page_counter = soup.find("div", {"class":"item-list"})
    try:
        paragraph = ["".join(x.findAll(text=True)) for x in page_counter.findAll("li", {"class":"pager-item"})]
        return len(paragraph)
    except:
        return 0
    

#pages("http://www.whitehouse.gov/briefing-room/Speeches-and-Remarks/2010/09")
#pages("http://www.whitehouse.gov/briefing-room/Speeches-and-Remarks/2011/04")



def sub_pages_URLs(parent_url):
    base_url = parent_url+"?page="

	# Number of Pages
    total_pages = pages(parent_url)
    try:
        f=open('subpages.csv', 'a')
        for i in range(0, total_pages+1):
            sub_page_url = base_url+str(i)
            f.write(u'%s\n' % (sub_page_url))
    finally:
        f.close()


#sub_pages_URLs("http://www.whitehouse.gov/briefing-room/Speeches-and-Remarks/2010/09")
#sub_pages_URLs("http://www.whitehouse.gov/briefing-room/Speeches-and-Remarks/2009/09")




