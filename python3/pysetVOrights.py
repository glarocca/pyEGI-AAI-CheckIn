#!/usr/bin/env python3

import requests
import json
import argparse
from pprint import pprint

def getVOMembership(login, password, url):
    print ("\n[.] Get VO membership information for: %s"
           % (user_data["VoMembers"][0]["Person"]["Id"]))
    cur = requests.get(url=url, auth=(login, password))
    membership = cur.json()
    print ("\n[ Response ]")
    pprint ("%s" %membership[0])

def updateVOMembership(login, password, url, data):
    print ("\n[.] Update VO membership information for a given EGI ID")
    cur = requests.put(url=url, auth=(login, password), json=data)
    data = cur.json()
    print ("\n[ Response ]")
    pprint ("%s" %data)

def setVOMembership(login, password, url, data):
    print ("\n[.] Set VO membership information for a given EGI ID")
    headers = {'Content-Type': 'application/json'}
    print ("[ Request ] = %s" %url)
    pprint ("[ Payload ] = %s" %data)
    cur = requests.post(url=url, auth=(login, password), json=data)
    data = cur.json()
    print ("\n[ Response ]")
    pprint ("%s" %data)

def main():
   pass

parser = argparse.ArgumentParser(
    description="Visualize and modify user's VO membership information"
    "Configuration file: ./JSON/config.json"
    "User configuration file: ./JSON/user.json"
  )

group = parser.add_mutually_exclusive_group(required=True)

group.add_argument(
    "-g",
    "--get",
    action="store_true",
    help="Get VO membership information for a given EGI ID",
  )

group.add_argument(
    "-s",
    "--set",
    action="store_true",
    help="Set VO membership for a given EGI ID",
  )

group.add_argument(
    "-u",
    "--update",
    action="store_true",
    help="Update VO membership for a given EGI ID",
  )
args = parser.parse_args()

with open('./JSON/config.json') as config_file:
    config_data = json.load(config_file)
    login = config_data["login"]
    password = config_data["password"]
    url = config_data["url"]

with open('./JSON/user.json') as user_file:
    user_data = json.load(user_file)

#print ("[ Request ] = %s" %url)
#print ("[ Payload ] = %s" %user_data)

if args.get:
    url = url +  "/%s"  % (user_data["VoMembers"][0]["Person"]["Id"])
    getVOMembership(login, password, url)

if args.set:
    setVOMembership(login, password, url, user_data)

if args.update:
    updateVOMembership(login, password, url, user_data)

if __name__ == "__main__":
    main()
