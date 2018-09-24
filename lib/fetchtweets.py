#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import tweepy
import json
from read_key import * 

#Twitter API credentials
def fetchtweets(consumer_key,consumer_secret,access_key,access_secret,twitter_name,depth):
    
    onefetch_count = 10
    if depth < onefetch_count :
        onefetch_count = depth

    #authorize api, api init
    apikey = tweepy.OAuthHandler(consumer_key, consumer_secret)
    apikey.set_access_token(access_key, access_secret)
    TweepyAPI = tweepy.API(apikey)

    tweets_list = [] #Init list for tweets   

    #perform the first fetch
    onefetch = TweepyAPI.user_timeline(screen_name = twitter_name,count=onefetch_count)
    tweets_list.extend(onefetch)
    oldest = tweets_list[-1].id - 1 # the newer one has a larger ID
    print(len(tweets_list)," tweets downloaded..Progress: ",round(len(tweets_list)/depth*100,1),"%",sep="")
    
    #start continuous fetching.
    while (len(onefetch) > 0)&(len(tweets_list)<depth):  #This will hit 0 when there is nothing to fetch
        onefetch = TweepyAPI.user_timeline(screen_name = twitter_name,count=onefetch_count,max_id=oldest)
        #maxID is to make sure there is no overlap
        tweets_list.extend(onefetch)
        oldest = tweets_list[-1].id - 1
        print(len(tweets_list)," tweets downloaded..Progress: ",round(len(tweets_list)/depth*100,1),"%",sep="")
        if (depth-len(tweets_list)) < onefetch_count:
            onefetch_count = depth-len(tweets_list)
    
    print(len(tweets_list),"tweets fetched in total")
    #output to JSON
    file = open('tweet.json', 'w') 
    print("Output result...")
    for status in tweets_list:
        json.dump(status._json,file,sort_keys = True,indent = 4)

    file.close()
    print("Success!")


if __name__ == '__main__':
    mykeys = read_key("/home/yku12/tweepy_key.key")
    #pass in the username of the account you want to download
    fetchtweets(mykeys[0],mykeys[1],mykeys[2],mykeys[3],"@bing",42)



