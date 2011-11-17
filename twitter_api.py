import optparse
import sys

from twitter import Twitter

import util

def search(searchTerm):
    """
    Print recent tweets containing `searchTerm`.
    """
    twitter = Twitter()
    result = twitter.search(q=searchTerm)
    for tweet in result['results']:
        util.safe_print(tweet['text'])

def trendingTopics():
    """
    Print the currently trending topics.
    """
    twitter = Twitter()
    result = twitter.trends._woeid(_woeid=1)
    for trend in result[0]['trends']:
        util.safe_print(trend['name'])

def userTweets(username):
    """
    Print recent tweets by `username`.
    """
    pass

def trendingTweets():
    """
    Print tweets for all the trending topics.
    """
    pass

def main(args):
    parser = optparse.OptionParser("""Usage: %prog [-s <search term> | -t | -u <username>]""")

    parser.add_option("-s", "--search",
                      type="string",
                      action="store",
                      dest="search_term",
                      default=None,
                      help="Display tweets containing a particular string.")
    parser.add_option("-t", "--trending-topics",
                      action="store_true",
                      dest="trending_topics",
                      default=False,
                      help="Display the trending topics.")

    (opts, args) = parser.parse_args(args)

    if opts.search_term:
        search(opts.search_term)
    elif opts.trending_topics:
        trendingTopics()

if __name__ == "__main__":
    main(sys.argv[1:])
