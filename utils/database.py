import os
import config;
import pymongo;
client = pymongo.MongoClient(config.mongo_uri)
##TODO: Change DB Name according to need
db = client.database