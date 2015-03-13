from date import date

def read_parentURLs(i):
	"""Reads the URLs from the Parent URLs CSV"""
	import csv
	with open('parentURLs.csv', 'rb') as urls_file:
		reader = csv.reader(urls_file)
		lines = list(reader)
		URL = lines[i]
		return URL

def read_reqURLs(i):
	"""Reads the URLs from the Requested Parent URLs CSV"""
	import csv
	with open('requested_parentURLs.csv', 'rb') as urls_file:
		reader = csv.reader(urls_file)
		lines = list(reader)
		print len(lines)
		URL = lines[i]
		return URL




def req_URLs(date1, date2):
	"""Returns the requested parent URL's for speeches and remarks in a 
	given date range. Date1 = "YYYY/MM" Date2 = "YYYY/MM"""

	a = date(date1)
	b = date(date2)

	if a==b:
		print '\n'.join(map(str, read_parentURLs(a)))

	elif a != b:
		f = open('requested_parentURLs.csv', 'w')
		for URL in range(a, b+1):
			requested_URL = '\n'.join(map(str, read_parentURLs(URL)))
			f.write(u'%s\n' % (requested_URL))
		f.close()


# Test Requested Parent Date URLS's
#req_URLs("2011/01", "2011/01") #Dates are the same
#req_URLs("2010/09", "2011/05") #Dates are different
#req_URLs("2009/01", "2015/03") #Dates are different



def read_URLs(filename):
	"""Reads the URLs from the Parent URLs CSV"""
	import csv
	with open(filename, 'rb') as urls_file:
		reader = csv.reader(urls_file)
		lines = list(reader)
		for x in range(0, len(lines)):
			URL = lines[x]
		return URL


#read_URLs('requested_parentURLs.csv')[0:5]



