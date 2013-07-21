import pymongo

from pymongo import MongoClient


conn =  MongoClient('localhost', 27017)

db = conn.test

names = db.names

item = names.find_one()

print item['name']


