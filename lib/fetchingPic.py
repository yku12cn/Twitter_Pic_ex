#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import tweepy
import json

#Twitter API credentials
def get_all_tweets(consumer_key,consumer_secret,access_key,access_secret,twitter_name):

    #authorize api, api init
    apikey = tweepy.OAuthHandler(consumer_key, consumer_secret)
    apikey.set_access_token(access_key, access_secret)
    TweepyAPI = tweepy.API(api.key)

    tweets_list = [] #Init list for tweets   

    new_tweets = api.user_timeline(screen_name = screen_name,count=10)

    #save most recent tweets
    alltweets.extend(new_tweets)

    #save the id of the oldest tweet less one
    oldest = alltweets[-1].id - 1

    #keep grabbing tweets until there are no tweets left to grab
    while len(new_tweets) > 0:
        #all subsiquent requests use the max_id param to prevent duplicates
        new_tweets = api.user_timeline(screen_name = screen_name,count=10,max_id=oldest)
        #save most recent tweets
        alltweets.extend(new_tweets)
        #update the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1
        if(len(alltweets) > 15):
                break
        print("...%s tweets downloaded so far" % (len(alltweets)))
               
    #write tweet objects to JSON
    file = open('tweet.json', 'w') 
    print("Writing tweet objects to JSON please wait...")
    for status in alltweets:
        json.dump(status._json,file,sort_keys = True,indent = 4)

    #close the file
    print("Done")
    file.close()


if __name__ == '__main__':
    c_key = "e3pD1SHGteou0O1DeCyUuWxEE"
    c_secret = "cv7wfmUyjsOcOuuX7008rIaKTJRs9Y50cHBcytPCsEF6Y86mYP"
    a_key = "305028337-k5wMBBqLydIqFX4rnaR3RFEwAVDOBpFNsQi0Xn8N"
    a_secret = "1dSzpoXoB8la6Bub09HZv7Xy26s2kLcZQWHQb7r56nwJ0"
    #pass in the username of the account you want to download
    get_all_tweets(c_key,c_secret,a_key,a_secret,"@bing")



