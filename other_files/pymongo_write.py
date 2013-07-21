import pymongo
import sys
from pymongo import MongoClient


def main():
    conn =  MongoClient("mongodb://localhost")
    db = conn.m101
    people = db.people
    person = {'name':'Arnold', 'role':'Terminator'}
    try:
        people.insert(person)
    except:
        print "insert failed:",sys.exc_info()[0]

main()

