#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import urllib.request
import urllib.parse
import http.cookiejar
import re
import os

def downloadpic(jsonfile_name = "tweet.json",outputfolder="pictureset",deepsearch=0):
    
    fakeHeader = {}
    fakeHeader['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36'
    
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
            if not deepsearch == 0:
                print("performing deep search",end="")
                try:
                    aherf = atweet["entities"]["urls"][0]["expanded_url"]
                    webreq = urllib.request.Request(urllib.parse.quote(aherf,safe=';/:?='),headers=fakeHeader)
                    resp = urllib.request.urlopen(webreq)
                    pagecode = resp.read().decode('utf-8')
                    aherf = re.findall(r"img data-aria-label-part src\=\"(.*?)\" alt=",pagecode)
                    if len(aherf) > 0:
                        print("  Success!")
                        picturelist.append(aherf[0])
                    else:
                        print("  Fail..")
                except:
                    print("  Fail..")

    print("Find",len(picturelist),"pictures")

    print("Start downloading pictures")
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

