#-*- encoding: utf-8 -*-

def read_key(key_filename=""):
    key_file = open(key_filename,'r')
    keys = key_file.read().splitlines()
    assert len(keys) == 4
    #Order: Consumer API keys/Consumer API secret keys/Access token/access token secret, each occupying a line respectively.
    key_file.close()
#    print(keys)
    return keys


