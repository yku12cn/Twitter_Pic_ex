#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from lib.read_key import * 
from lib.fetchtweets import *
from lib.downloadpic import *

if __name__ == '__main__':
    fetchtweets(read_key("/home/yku12/tweepy_key.key"),"@bing",1,"tweetlog.json")
#    downloadpic("tweetlog.json","package")


