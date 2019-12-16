#!/usr/bin/python3

import sys
import requests
import datetime
import json

def getAttacks(argv):
    api_uuid = sys.argv[1]
    api_secret = sys.argv[2]
    client_id = sys.argv[3]
    stime = int(datetime.datetime.strptime(sys.argv[4],
    '%d/%m/%Y').timestamp())
    etime = int(datetime.datetime.strptime(sys.argv[5],
    '%d/%m/%Y').timestamp())

    Headers = {"X-WallarmAPI-UUID": api_uuid, \
               "X-WallarmAPI-Secret": api_secret, \
               "Content-Type": "application/json"}    

    Request_Body = json.loads('{"filter":{"clientid": \
    [ ' + str(client_id) + '],"time":[[' + str(stime) + ',\
    ' + str(etime) + ']]},"offset":0,"limit":10,"order_desc":true}')
    print(Request_Body)
    attacks = requests.post("https://api.wallarm.com/v1/objects/attack", \
                            headers=Headers, json=Request_Body)    
    print(attacks.json())
    return

getAttacks(sys.argv)