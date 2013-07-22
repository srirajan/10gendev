
//group and push
db.zips.aggregate([{"$group":{"_id":"$city","states":{"$push":"$state"}}}])



