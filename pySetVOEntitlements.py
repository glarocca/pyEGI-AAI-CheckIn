#!/usr/bin/env python

import requests
import json

login    = "***************"
password = "***************"
url = "https://aai.egi.eu/api/v1/VoMembers"

# Configure here and add the user's unique, non-reassignable, persistent pseudonymous EGI ID
EGI_ID = "<EGI_user_ID>" # e.g.: <ASCII>@egi.eu

def getVOMembership(login, password, url):
	print "\n[.] Get VO membership information for a given EGI ID"
	_url = url + "/" + EGI_ID
        print "[ Request ] = %s" %_url

        cur = requests.get(url=_url,
			   auth=(login, password))

        data = cur.json()

        print ("\n[ Response ]")
        print ("- %s" %data)

def updateVOMembership(login, password, url):
	print "\n[.] Update VO membership information for a given EGI ID"
        with open('./JSON/ltos-add-USER.json') as data_file:
		data = json.load(data_file)

        print "[ Request ] = %s" %url
        print "[ Payload ] = %s" %data	

        cur = requests.put(url=url, 
		    	   auth=(login, password), 
                           json=data)
        data = cur.json()
	
def setVOMembership(login, password, url):
	print "\n[.] Set VO membership information for a given EGI ID"
	headers = {'Content-Type': 'application/json'}

        with open('./JSON/ltos-add-USER.json') as data_file:
		data = json.load(data_file)

        print "[ Request ] = %s" %url
        print "[ Payload ] = %s" %data	

        cur = requests.post(url=url, 
			    auth=(login, password), 
                            json=data)

        data = cur.json()

        print ("\n[ Response ]")
        print ("- %s" %data)
        #print ("- %s" %data["message"])
        #print ("- %s" %data["code"])


def main():
        #Set VO membership for a given EGI ID
	setVOMembership(login, password, url)	
        
	#Update VO membership for a given EGI ID
	#updateVOMembership(login, password, url)	

        #Get VO membership information for a given EGI ID
	#getVOMembership(login, password, url)

if __name__ == "__main__":
        main()


