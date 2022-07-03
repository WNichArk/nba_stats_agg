
from bson import encode
from team import Team
from mongo_connect_test import database
import pymongo
import bson
from constants.constants import call_test

count = 1
if count == 1:
    print(call_test())
    #Calls get_database function of mongo_connect_test (class built for )
    #db = database().get_database("nba-stats-agg-mongo")

    #This explicity creates or calls a collection ("table") 
    #teams = db['teams_test_1']

    #Convert object to dictionary, encode to bson and insert
    # team1 = Team("Rockets", "Houston", "Some Guy", 35)
    # s = bson.encode(team1.__dict__)
    # teams.insert_one(team1.__dict__)

    #Query
    #myquery = {"name":"Rockets"}
    #rockets = teams.find(myquery)
    #for r in rockets:
        #print(r)


