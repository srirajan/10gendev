import pymongo
import sys
from pymongo import MongoClient

def find():
    query = {}
    selector = {'student_id':1, '_id':1, 'name':1,'scores':1}
    try:
        cur = scores.find(query,selector)
    except:
        print "Error: ", sys.exc_info()[0]

    delete_count = 0
    for doc in cur:
        print "----------------------------"
        #print "ID : ", doc['_id']
        #print "Name : ", doc['name']
        #print "Scores: "
        #print doc['scores']
        newscores  = list(doc['scores'])
        newscores.sort(reverse=True)
        lowest_hw = {}
        for s in newscores:
           if (s['type'] == 'homework'):
               lowest_hw= s
        
        print "Remove"
        print doc
        scores.remove({'_id': doc['_id']})
        newscores.remove(lowest_hw)
        doc['scores'] = list(newscores)
        print "Insert"
        print doc
        scores.insert(doc)
            
conn =  MongoClient("mongodb://localhost")
db = conn.school
scores = db.students
find()
