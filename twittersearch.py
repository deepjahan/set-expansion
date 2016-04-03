from TwitterSearch import *
try:
	tso = TwitterSearchOrder() # create a TwitterSearchOrder object
	tso.set_keywords(['c++', 'java']) # let's define all words we would like to have a look for
#	tso.set_language('en') # we want to see German tweets only
	tso.set_include_entities(False) # and don't give us all those entity information

# it's about time to create a TwitterSearch object with our secret tokens
	ts = TwitterSearch(consumer_key = 'vnlzYxw1q3P0gau3DVdYMEvxM',consumer_secret = 'xVAUZdFoVDY590zjCUInnVMMZsxCn5CjWyQ0PpW3qwtWdDSi7t',access_token = '2553967664-FxKSUZ2i9dyq7Z10uogFQZSnBDHkcsB367ucRs4',access_token_secret = 'xDxDDAHgda11wv2EkJi2vN99TilIflKsZip3i1rLjIkjs')

# this is where the fun actually starts :)
	for tweet in ts.search_tweets_iterable(tso):
		print( '@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text'] ) )

except TwitterSearchException as e: # take care of all those ugly errors if there are some
	print(e)
