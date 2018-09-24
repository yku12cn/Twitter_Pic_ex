#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import urllib.request
import urllib.parse
import http.cookiejar
import re
import os

def downloadpic(jsonfile_name = "tweet.json",outputfolder="pictureset"):
    
    #read from JSON
    print("Reading json...")
    inputjson = open(jsonfile_name, "r") 
    tweets = json.load(inputjson)
    print("Load",len(tweets),"tweets")
    
    #start looking for pictures
    picturelist=[]
    for atweet in tweets:
        try:
            mediapart = atweet["entities"]["media"][0]
            if mediapart["type"]=="photo":
                picturelist.append(mediapart["media_url_https"])
        except:
            pass

    print("Find",len(picturelist),"pictures")

    print("Start downloading pictures")
    fakeHeader = {}
    fakeHeader['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36'

    counter = 0
    succ = 0
    if not os.path.exists("./"+outputfolder): #Create Dir
        os.mkdir("./"+outputfolder)

    for alink in picturelist:
        try:
            webreq = urllib.request.Request(urllib.parse.quote(alink,safe=';/:?='),headers=fakeHeader)
            resp = urllib.request.urlopen(webreq)
            picfile = open("./"+outputfolder+"/"+re.findall(r"/([^/]*?)$",alink)[0],"wb")
            picfile.write(resp.read())
            picfile.close()
            succ = succ + 1
        except:
            pass
        
        counter = counter + 1
        print(counter," links tried. ",succ," successes. progress: ",round(counter/len(picturelist)*100,1),"%",sep="")

