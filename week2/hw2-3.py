import pymongo
import sys
from pymongo import MongoClient

def find():
    query = {'type':'homework'}
    selector = {'student_id':1, '_id':0, 'type':1,'score':1}
    try:
        cur = scores.find(query,selector)
        cur = cur.sort([('student_id',pymongo.ASCENDING),('score',pymongo.DESCENDING)])

    except:
        print "Error: ", sys.exc_info()[0]

    first_record = 1
    delete_count = 0
    for doc in cur:
        if (first_record == 1):
            first_record = 0
            last_student_id = doc['student_id']
            last_student_score = doc['score']
        else:
            if ( last_student_id != doc['student_id'] ):
                print "Deleting Last id ", last_student_id , " Last score ", last_student_score
                #scores.remove({'student_id':last_student_id,'score':last_student_score})
                delete_count += 1
                
            last_student_id = doc['student_id']
            last_student_score = doc['score']

        print doc
            
    print "Deleting Last id ", last_student_id , " Last score ", last_student_score
    #scores.remove({'student_id':last_student_id,'score':last_student_score})
    delete_count += 1
    print "Deleted " , delete_count

conn =  MongoClient("mongodb://localhost")
db = conn.student
scores = db.grades
find()
