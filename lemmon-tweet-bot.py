# -*- coding: utf-8 -*-
import twython
import sys

if __name__ == '__main__':
    param = sys.argv
    if (len(param) != 2):
        print ("Usage: $ python " + param[0] + " tweet.txt")
        quit()  

    f = open(param[1])
    tweet_str = f.read()
    f.close()

    consumerKey = 'CONSUMERKEY'
    consumerSecret = 'CONSUMERSECRET'
    accessToken = 'ACCESSTOKEN'
    accessSecret = 'ACCESSSECRET'

    api = twython.Twython(app_key=consumerKey,
                  app_secret=consumerSecret,
                  oauth_token=accessToken,
                  oauth_token_secret=accessSecret)

    try:
        api.update_status(status=tweet_str)
    except twython.TwythonError as e:
        print e
