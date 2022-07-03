from os import stat_result
import apicalls as api
from bson import encode
from team import Team
from mongo_connect_test import database
import pymongo
import bson
from constants.constants import call_test
import time

count = 1
if count == 1:
    #print(call_test())
    #Calls get_database function of mongo_connect_test (class built for )
    db = database().get_database("nba-stats-agg-mongo")

    #This explicity creates or calls a collection ("table") 
    seasons = db['seasons']
    games = db['games']
    teams = db['teams']
    players = db['players']
    player_stats = db['player_stats']
    team_stats = db['team_stats']

    #Convert object to dictionary, encode to bson and insert
    # team1 = Team("Rockets", "Houston", "Some Guy", 35)
    # s = bson.encode(team1.__dict__)
    # teams.insert_one(team1.__dict__)

    #Query
    # myquery = {"name":"Rockets"}
    # rockets = teams.find(myquery)
    # for r in rockets:
    #     print(r)

    #get seasons
    # ff = api.NBA.get_seasons()
    # for f in ff.json()['response']:
    #     seasons.insert_one({"season": f})

    #get all games from all seasons in db
    # print("start get seasons")
    # seas = seasons.find({})
    # for s in seas:
    #     game_list = api.NBA.get_games_by_season(s['season'])
    #     time.sleep(5)
    #     for g in game_list.json()['response']:
    #         games.insert_one(g)

    # get teams
    # print("start get teams")
    # team_list = api.NBA.get_teams()
    # for t in team_list.json()['response']:
    #     print("adding " + t['name'])
    #     teams.insert_one(t)

    # get actual nba teams
    # nba_teams = teams.find({"nbaFranchise": True})
    # countnba = 0
    # season = 2021
    # for n in nba_teams:
    #     print("Get players from " + str(season) + " " + n['name'])
    #     plyrs = api.NBA.get_players_by_team_and_season(n["id"], season)
    #     player_list = plyrs.json()['response']
    # Add players
    #     for p in player_list:
    #         print("insert " + p["firstname"] + " " + p["lastname"])
    #         p["teamName"] = n["name"]
    #         p["teamId"] = n["id"]
    #         players.insert_one(p)
    #     print("start wait")
    #     time.sleep(0.5)
    #     countnba += 1
    # print("total " + str(countnba))


    # get stats for players
    # player_list = players.find({})
    # for p in player_list:
    #     stat_list = api.NBA.get_statistics_by_player_and_season(p["id"], 2021)
    #     print("Insert stats for " + p['firstname'] + " " + p['lastname'])
    #     player_stats.insert_many(stat_list.json()['response'])
    #     time.sleep(0.25)

    #get stats for teams
    # team_list = teams.find({"nbaFranchise": True})
    # for t in team_list:
    #     stat_list = api.NBA.get_statistics_by_team_and_seasion(t["id"], 2021)
    #     print("Insert stats for " + t['name'])
    #     team_stats.insert_many(stat_list.json()["response"])
    # time.sleep(0.25)

    res = api.NBA.get_seasons()
    print(res.headers['X-RateLimit-requests-Remaining'])

    



    
  


