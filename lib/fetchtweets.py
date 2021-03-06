#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import tweepy
import json

#Twitter API credentials
def fetchtweets(logkeys,twitter_name,depth,tweetsfilename):

    #checking input variables
    assert len(logkeys) == 4
    assert type(logkeys[3]) == str
    assert type(twitter_name) == str
    assert type(depth) == int
    assert depth >= 0
    assert type(tweetsfilename) == str

    onefetch_count = 10
    if depth < onefetch_count :
        onefetch_count = depth

    #authorize api, api init
    apikey = tweepy.OAuthHandler(logkeys[0], logkeys[1])
    apikey.set_access_token(logkeys[2], logkeys[3])
    try:
        TweepyAPI = tweepy.API(apikey)
        print("Tweeter login successful")
    except:
        print("Tweeter login fail")

    tweets_list = [] #Init list for tweets

    if depth > 0:
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
        with open(tweetsfilename, "w") as outputfile:
            # with statement automatically closes file handle as needed
            print("Output results to {}".format(tweetsfilename))
            json_list = [status._json for status in tweets_list]
            json.dump(json_list, outputfile, indent = 4)

        print("Success!")
