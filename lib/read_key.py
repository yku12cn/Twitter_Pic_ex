#-*- encoding: utf-8 -*-

def read_key(key_filename=""):
    key_file = open(key_filename,'r')
    keys = key_file.readlines()
    #Order: Consumer API keys/Consumer API secret keys/Access token/access token secret
    key_file.close()
#    print(keys)
    return keys


