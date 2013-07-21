db.posts.aggregate([{"$unwind": "$comments"}, {"$group": {"_id": "$comments.author", "count": {"$sum": 1}}}],{"$sort":{"$_id.count":-1}})

db.zips.aggregate([	
{"$match": {"state": {"$in": ["NY", "CA"]}}},
{"$group": {"_id": {"state": "$state", "city": "$city"}, "city_pop": {"$sum": "$pop"}}},
{"$match": {"city_pop": {"$gt": 25000}}},
{"$group": {"_id": null, "totalaverage": {"$avg": "$city_pop"}}}
])


db.grades.aggregate([
{"$unwind": "$scores"},
{"$match": {"scores.type": {"$ne": "quiz"}}},
{"$group": {"_id": {"sid": "$student_id", "cid": "$class_id"}, "s_avg": {"$avg": "$scores.score"}}},
{"$group": {"_id": "$_id.cid", "c_avg": {"$avg": "$s_avg"}}},
{"$sort" : {"c_avg": 1}}
])


db.zips.aggregate([ {"$project": {"_id": 0, "zipcode": "$_id", "first_c": {"$substr" : ["$city",0,1]}, "pop": 1, "city": 1 }}, {"$match"  : {"first_c": {"$regex":/[0-9]/}}}, {"$group"  : {"_id": null, "tot_pop": {"$sum": "$pop"}}} ])


