This project focus on fetching pictures on a certain twitter's tweets

function fetchtweets(key[4],"@whichtwitter",howmany,"output.json")  
requires four inputs:  
  key[4] is a list with a length of 4. The list should consists of:  
    [Consumer API keys,Consumer API secret keys,Access token,access token secret]  
  "@whichtwitter" is a string indicating which wtitter you want to fetch  
  howmany is an integer, indicating how many tweets you want to fetch  
  "output.json" is a string indicating the name for your final output file  
this function is used for fetching tweets of a certain twitter.  

function read_key("key_filename")  
requires one input "key_filename", indicating the file you store your twitter api's key.  
This function will return a list key[4] which can be used directly in fetchtweets()  
the key file shall look like:  
  GTxxxxxxxxxxxxxxxxxxTL  
  MdxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxpxXi  
  30xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxu  
  nGGxxxxxxxxxxxxxxxxxxxxxxxxidxxxxxxxxxxxxD  
There should be only 4 lines in this file.  
Each line represents 'Consumer API keys','Consumer API secret keys','Access token','access token secret' respectivelly in that order.  

function downloadpic("output.json","pictureset",deepsearch=0)  
requires three inputs:  
  "output.json" is the output file's name of fetchtweets() which has all the information about the tweets for that certain twitter.  
  "pictureset" is the name of the folder which you want to store all the downloaded pictures in.  
  deepsearch is a flag, indicating whether you want to perform a deeper search if the default one fails. Deepsearch is not a very reliable function and can take up some time to finish. However, if you turn this on, you can get almost every picture you can see in that twitter.
