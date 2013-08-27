import urllib2
import json as simplejson
import random
import sqlite3 as lite

productIds = []
apiKeys = ["98bbbd30b3e4f621d9cb544a790086d6"]

file = open("productIds3.txt", "r")
for line in file:
  productIds.append(line.strip())
print productIds
file.close()

connection = lite.connect("productInfo.db")

with connection:

  cursor = connection.cursor()
  cursor.execute("DROP TABLE IF EXISTS ProductInfo")
  cursor.execute("CREATE TABLE ProductInfo(Id INT, Name TEXT, Calories INT)")
  for productId in productIds:
    url = "http://api.uwaterloo.ca/public/v2/foodservices/product/" + \
    str(productId) + ".json?key=" + str(apiKeys[random.randint(0, len(apiKeys) - 1)])
    req = urllib2.Request(url)
    opener = urllib2.build_opener()

    f = opener.open(req)
    data = simplejson.load(f)
    if data["meta"]["status"] == 200:
      if data["data"]["product_name"] != None:
        print "INSERT INTO ProductInfo VALUES(" + str(data["data"]["product_id"]) + ", " + str(data["data"]["product_name"]) + ", " + str(data["data"]["calories"]) + ")"
        cursor.execute("INSERT INTO ProductInfo VALUES(" +
            str(data["data"]["product_id"]) + ", '" +
            str(data["data"]["product_name"]) + "', " + str(data["data"]["calories"]) + ")")

print productIds



