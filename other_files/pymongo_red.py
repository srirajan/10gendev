import pymongo
import sys
from pymongo import MongoClient

def find():
    print "find "
    query = {'media.oembed.type':'video'}
    selector = {'media.oembed..url':1, '_id':0}
    try:
        cur = scores.find(query,selector)

    except:
        print "Error: ", sys.exc_info()[0]
    sanity = 0
    for doc in cur:
        print doc
        sanity = sanity + 1
        if (sanity >10):
            break;

conn =  MongoClient("mongodb://localhost")
db = conn.reddit
scores = db.articles
find()
