#First Parser Created Addresses Most White Hosue HTML Code
#WHT1 works when release and date are in <div class="release" INFO </div>
# and <div class="date"> INFO </div>. Otherwise use WHT2. 
#WHT2 works when the speech header is set up as <div id="content">
# <p allign="center" INFO p>.



def WHT(url):
    """Prints Text Output for a given URL from Whitehouse Speeches and Remarks"""
    
    import sys, csv, time, io, subprocess
    import urllib2, random
    import os
    from bs4 import BeautifulSoup

    soup = BeautifulSoup(urllib2.urlopen(url).read())

    # Get URL
    url2 = "Cite: \n"+url+"\n"


    # Get Date
    Date = soup.find("div", {"class":"date"})
    raw_date = Date.get_text()
    date = raw_date.replace(' ', '', 12)

    # Get Release
    Release = soup.find("div", {"class":"release"})
    raw_release = Release.get_text()
    release = raw_release.replace(' ', '', 12)+"\n\n"

    # Get Title
    Title = soup.find("h1", {"property":"dc:title"})
    title = Title.get_text()

    
    # Get Paragraph Body
    content = soup.find("div", {"id":"content"})
    paragraph = ["".join(x.findAll(text=True)) for x in content.findAll("p")]
    paragraph_body = "\n\n%s" % ("\n\n".join(paragraph))




    #Get File ID - Date & Time
    #Date
    year_id = url[43:47]
    month_id = url[48:50]
    day_id = url[51:53]
    date_id = year_id+'-'+month_id+'-'+day_id
    #Random ID
    randID1 = str(random.randrange(6, 10000, 1))
    randID2 = str(random.randrange(6, 10000, 1))

    try:
        path1 = date_id+"_"+"ID1"+".txt"
        path2 = date_id+"_"+"ID2"+".txt"
        path3 = date_id+"_"+"ID3"+".txt"
        path4 = date_id+"_"+"ID4"+".txt"
        path5 = date_id+"_"+"ID5"+".txt"
        if os.path.isfile(path1) == False:
            #print "no file ID1 found, create ID1"
            f = open(date_id+"_"+"ID1"+".txt", 'w')
            f.write(url2.encode('utf-8'))
            f.write(date.encode('utf-8'))
            f.write(release.encode('utf-8'))
            f.write(title.encode('utf-8'))
            f.write(paragraph_body.encode('utf-8'))
            f.close
            open_call1="open "+path1
            subprocess.call(open_call1, shell=True)
            return

        elif os.path.isfile(path1) == True:
            #print "found file ID1, check for ID2"
            if os.path.isfile(path2) == False:
                print "found ID1, no file ID2 found, make ID2"
                f = open(date_id+"_"+"ID2"+".txt", 'w')
                f.write(url2.encode('utf-8'))
                f.write(date.encode('utf-8'))
                f.write(release.encode('utf-8'))
                f.write(title.encode('utf-8'))
                f.write(paragraph_body.encode('utf-8'))
                f.close
                open_call2="open "+path2
                subprocess.call(open_call2, shell=True)
                return
            elif os.path.isfile(path2) == True:
                #print "found file ID2, check for ID3"
                if os.path.isfile(path3) == False:
                    print "found IDs 1-2, no file ID3 found, make ID3"
                    f = open(date_id+"_"+"ID3"+".txt", 'w')
                    f.write(url2.encode('utf-8'))
                    f.write(date.encode('utf-8'))
                    f.write(release.encode('utf-8'))
                    f.write(title.encode('utf-8'))
                    f.write(paragraph_body.encode('utf-8'))
                    open_call="open "+path3
                    subprocess.call(open_call, shell=True)
                    f.close
                    return
                elif os.path.isfile(path3) == True:
                    #print "found file ID3, check for ID4"
                    if os.path.isfile(path4) == False:
                        print "found IDs 1-3, no file ID4 found, make ID4"
                        f = open(date_id+"_"+"ID4"+".txt", 'w')
                        f.write(url2.encode('utf-8'))
                        f.write(date.encode('utf-8'))
                        f.write(release.encode('utf-8'))
                        f.write(title.encode('utf-8'))
                        f.write(paragraph_body.encode('utf-8'))
                        f.close
                        open_call="open "+path3
                        subprocess.call(open_call, shell=True)
                        return
                    elif os.path.isfile(path4) == True:
                        #print "found file ID4, check for ID5"
                        if os.path.isfile(path5) == False:
                            print "found IDs 1-4, no file ID5 found, make ID5"
                            f = open(date_id+"_"+"ID5"+".txt", 'w')
                            f.write(url2.encode('utf-8'))
                            f.write(date.encode('utf-8'))
                            f.write(release.encode('utf-8'))
                            f.write(title.encode('utf-8'))
                            f.write(paragraph_body.encode('utf-8'))
                            f.close
                            open_call="open "+path4
                            subprocess.call(open_call, shell=True)
                            return
                        elif os.path.isfile(path5) == True:
                            print "found IDs 1-5, create random ID"
                            f = open(date_id+"_"+"ID"+randID1+"-"+randID2+".txt", 'w')
                            f.write(url2.encode('utf-8'))
                            f.write(date.encode('utf-8'))
                            f.write(release.encode('utf-8'))
                            f.write(title.encode('utf-8'))
                            f.write(paragraph_body.encode('utf-8'))
                            f.close
                            return  

        
    finally:
        pass



    

##Test URLS
#2014
#url = "http://www.whitehouse.gov/the-press-office/2014/01/22/remarks-president-meeting-presidential-commission-election-administratio"

#WHT(url)





