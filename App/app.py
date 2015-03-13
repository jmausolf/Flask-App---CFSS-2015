from flask import Flask, render_template, request, redirect, url_for
import pymysql

#Import Other Python Modules
import sys, csv, time, io, subprocess

#Import Past HW Modules 
sys.path.append('../Python_Scripts/')
from getparentURL import *
from readParent import *
from pages import *
from date import date
from CSVread import *

#Speech Parsers
from Speech_parser1 import *
from Speech_parser2 import *
from Speech_parser3 import *
from S2009_2010_Speech_parser3 import *

#Flask Database Info - Mac OSX, No Password
dbname="white_house_data"
host="localhost"
user="root"
passwd=""
db=pymysql.connect(db=dbname, host=host, user=user,passwd=passwd, charset='utf8')


app = Flask(__name__)

def createSpeechURLs(dateone, datetwo):
    """Function to make a new playlist, save the file to a MySQL database, and render the HTML file."""
    import urllib2,sys
    from bs4 import BeautifulSoup

    cur = db.cursor()
    CREATE_TABLE_speech_urls = '''CREATE TABLE IF NOT EXISTS speech_urls (id INTEGER PRIMARY KEY AUTO_INCREMENT, speech_urls VARCHAR(260));'''
    #CREATE_TABLE_songs = '''CREATE TABLE IF NOT EXISTS songs (id INTEGER PRIMARY KEY AUTO_INCREMENT, playlistId INTEGER, songOrder INTEGER, artistName VARCHAR(260), albumName VARCHAR(260), trackName VARCHAR(260));'''
    cur.execute(CREATE_TABLE_speech_urls)
    #cur.execute(CREATE_TABLE_songs)
    db.commit()

    #####################################################################
    #Get URLS


    #Generate Parent URLs CSV
    getparentURLs()
    
    #Define initial parent URLs in Specified Date Range
    parent_urls = req_URLs(str(dateone), str(datetwo))


    print "___"*20


    #Get Number of Lines of Requested URLs
    with open('requested_parentURLs.csv', 'rU') as urls_file:
        reader = csv.reader(urls_file)
        lines = list(reader)
        XR = len(lines)
        print "Total requested urls:", XR
        
    # Create CSV of Subpage URLS 
    for URL in range(0, XR):
        rURL = '\n'.join(map(str, read_reqURLs(URL)))
        time.sleep(0.5)
        sub_pages_URLs(rURL)


    #Get Number of Lines of Subpages URLs
    with open('subpages.csv', 'rU') as urls_file:
        reader = csv.reader(urls_file)
        lines = list(reader)
        XS = len(lines)
        print "Total requested subpages:", XS


    def speech_urls(sub_pages_url):
        """Returns all the speech URLs extentions for a given sub-pages URL"""
        
        import urllib2,sys
        import pymysql
        from bs4 import BeautifulSoup

        #Base Page
        soup = BeautifulSoup(urllib2.urlopen(sub_pages_url).read())
        
        #Speech URLs
        content = soup.find("div", {"class":"view-content"})
        speeches = ["".join(x.findAll("a")) for x in content.findAll(href=True)]
        
        base_url = "http://www.whitehouse.gov"


        for link in content.findAll('a', href=True):
            ext = link['href']
            speech_url = base_url+ext
            cur = db.cursor()
            add_to_speech_urls = '''INSERT INTO speech_urls (speech_urls) VALUES ('%s')''' % (speech_url)
            cur.execute(add_to_speech_urls) 
            db.commit()



    # Create CSV of Speech URLS
    for URL in range(0, XS):
        subURL = '\n'.join(map(str, read_subURLs(URL)))
        time.sleep(0.5)
        speech_urls(subURL)






    #Add artist's name to the playlists table.
    #cur = db.cursor()
    #add_to_playlist = '''INSERT INTO speech_urls (speech_urls) VALUES ('%s')''' % (inputName)
    #cur.execute(add_to_playlist) 
    #db.commit()






@app.route('/')
def make_index_resp():
    # Routes to local http://127.0.0.1:5000/    
    return(render_template('index.html'))


@app.route('/github_pkg/')
def make_github_pkg():
    # Routes to local http://127.0.0.1:5000/    
    return(render_template('github_pkg.html'))


@app.route('/ipython/')
def launch_ipython():  
    return(render_template('ipython.html'))


@app.route('/thankyou/')
def thankyou():  
    return(render_template('parsed_response.html'))


@app.route('/speech_urls/')
def speech_URLS_resp():
    cur = db.cursor()
    db.commit()
    sql = '''
        SELECT id, speech_urls
        FROM speech_urls
        ORDER BY id '''
    cur.execute(sql)
    speech_urls = cur.fetchmany(size=50)
    return render_template('speechurls.html', speech_urls=speech_urls)


@app.route('/speech_urls/more/')
def more_speech_URLS_resp():
    cur = db.cursor()
    db.commit()
    sql = '''
        SELECT id, speech_urls
        FROM speech_urls
        ORDER BY id '''
    cur.execute(sql)
    speech_urls = cur.fetchall()
    return render_template('more_speechurls.html', speech_urls=speech_urls)


@app.route('/getSpeechURLS/',methods=['GET','POST'])
def get_SpeechURLS():
    if request.method == 'GET':
        # Execute when user visits page
        return(render_template('getspeechURLS.html'))
    elif request.method == 'POST':
        # Execute when user completes form
        dateone = request.form['dateone']
        datetwo = request.form['datetwo']

        #Use to avoid having the debugger crash from Spotify
        #try:
        createSpeechURLs(dateone, datetwo)
        return(redirect('/speech_urls/'))
        #except:


@app.route('/getSpeech/',methods=['GET','POST'])
def get_parsedSpeech():
    if request.method == 'GET':
        return(render_template('getspeech.html'))
    elif request.method == 'POST':
        speechURL = request.form['url']
        print speechURL
        try:
            WHT(speechURL)
            print "ran WHT1"
        except:
            try:
                WHT2(speechURL)
                print "ran WHT2"
            except:
                try:
                    pre_WHT3(speechURL)
                    print "ran pre_WHT3"
                except:
                    try:
                        WHT3(speechURL)
                        print "ran WHT3"
                    except:
                        print "ERROR: NO SPEECH PARSED. EXCEPTION CODE: 99"
                        pass

        return(redirect('/speech_urls/'))



@app.route('/getSpeech_embed/',methods=['GET','POST'])
def get_parsedSpeech_embed():
    if request.method == 'GET':
        return(render_template('getspeech_embed.html'))
    elif request.method == 'POST':
        speechURL = request.form['url']
        print speechURL
        try:
            WHT(speechURL)
            print "ran WHT1"
        except:
            try:
                WHT2(speechURL)
                print "ran WHT2"
            except:
                try:
                    pre_WHT3(speechURL)
                    print "ran pre_WHT3"
                except:
                    try:
                        WHT3(speechURL)
                        print "ran WHT3"
                    except:
                        print "ERROR: NO SPEECH PARSED. EXCEPTION CODE: 99"
                        pass

        return(redirect('/thankyou/'))


@app.route('/getSpeech2/')
def get_parsedSpeech2():

    with open('2011-01-25_ID1.txt', 'r') as f:
        text = f.read()

        text = '<div style="white-space; pre-wrap;">'+text+"</div>"
        return(text)





@app.route('/show_speech/')
def show_speech_resp():
    cur = db.cursor()
    db.commit()
    sql = '''
        SELECT id, speech
        FROM parsed_speeches
        ORDER BY id '''
    cur.execute(sql)
    show_speech = cur.fetchall()
    return render_template('show_speech.html', show_speech=show_speech)



if __name__ == '__main__':
    app.debug=True
    app.run()