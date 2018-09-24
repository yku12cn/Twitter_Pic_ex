#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from lib.read_key import * 
from lib.fetchtweets import *
from lib.downloadpic import *

if __name__ == '__main__':
    mykeys = read_key("/home/yku12/tweepy_key.key")
    fetchtweets(mykeys[0],mykeys[1],mykeys[2],mykeys[3],"@bing",40)
    downloadpic("tweet.json","package")


