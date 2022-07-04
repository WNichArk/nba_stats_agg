from os import stat_result
import apicalls as api
from bson import ObjectId, encode
from team import Team
from mongo_connect_test import database
import pymongo
import bson
from constants.constants import call_test
import time


    #Calls get_database function of mongo_connect_test (class built for )
db = database().get_database("nba-stats-agg-mongo")

    #This explicity creates or calls a collection ["table"] 
seasons = db['seasons']
games = db['games']
teams = db['teams']
players = db['players']
player_stats = db['player_stats']
team_stats = db['team_stats']
game_stats = db['game_stats']
dbstats = db['db_stats']

    #Convert object to dictionary, encode to bson and insert
    # team1 = Team("Rockets", "Houston", "Some Guy", 35)
    # s = bson.encode(team1.__dict__)
    # teams.insert_one(team1.__dict__) 

    #Query example
    # myquery = {"name":"Rockets"}
    # rockets = teams.find(myquery)
    # for r in rockets:
    #     print(r)

    #get seasons
def get_seasons():
    ff = api.NBA.get_seasons()
    for f in ff.json()['response']:
        seasons.insert_one({"season": f})

    #get all games from all seasons in db
def get_games():
    print("start get seasons")
    seas = seasons.find({}) #find all using ({})
    for s in seas:
        game_list = api.NBA.get_games_by_season(s['season'])
        time.sleep(5)
        for g in game_list.json()['response']:
            games.insert_one(g)

    # get teams
def insert_teams():
    print("start get teams")
    team_list = api.NBA.get_teams()
    for t in team_list.json()['response']:
        print("adding " + t['name'])
        teams.insert_one(t)

    # get actual nba team players
def get_franchise_nba_players():
    nba_teams = teams.find({"nbaFranchise": True})
    countnba = 0
    season = 2021
    for n in nba_teams:
        print("Get players from " + str(season) + " " + n['name'])
        plyrs = api.NBA.get_players_by_team_and_season(n["id"], season)
        player_list = plyrs.json()['response']
    #Add players
        for p in player_list:
            print("insert " + p["firstname"] + " " + p["lastname"])
            p["teamName"] = n["name"]
            p["teamId"] = n["id"]
            players.insert_one(p)
        print("start wait")
        time.sleep(0.5)
        countnba += 1
    print("total " + str(countnba))


    # get stats for players
def get_player_stats():
    player_list = players.find({})
    for p in player_list:
        stat_list = api.NBA.get_statistics_by_player_and_season(p["id"], 2021)
        print("Insert stats for " + p['firstname'] + " " + p['lastname'])
        player_stats.insert_many(stat_list.json()['response'])
        time.sleep(0.25)

def return_id(e):
    return int(e["id"])
   

    #get stats for teams
def get_team_stats():
    team_list = players.find({"leagues.standard.active":True
    })
    teamlistlist = list(team_list)
    teamlistlist.sort(key=return_id)
    print(str(len(teamlistlist)))
    for t in teamlistlist:
        stat_list = api.NBA.get_statistics_by_team_and_seasion(t["id"], 2021)
        print("Insert stats for " + t['firstname'])
        print(t["id"])
        team_stats.insert_many(stat_list.json()["response"])
    time.sleep(0.25)

def get_last_db_entry():
    db_stat_list = list(dbstats.find({}))
    last_db_stat = db_stat_list.pop()
    print(last_db_stat)
    return last_db_stat["game_id"]

    #get game stats. relies on indexes of gamelistReduced based on last game_id entered into dbstats
def get_game_stats(add_index, start_id = 0):
    game_list = games.find({"league":"standard"})
    gamelistlist = list(game_list)
    gamelistlist.sort(key=return_id)
    remaining = api.NBA.check_remaining_requests()["remaining"]
    print("Remaining: " + str(remaining))
    if len(gamelistlist) > remaining:
        if start_id < 1:
            last_game = list(dbstats.find({})).pop()["game_id"]
        else:
            last_game = start_id
        restart_item = next((i for i in gamelistlist if i["id"] == last_game), None)
        if add_index < 1:
            add_index = 1
        restart_index = gamelistlist.index(restart_item) + add_index
        print("Restart index: " + str(restart_index))
        print("Continue?")
        gamelistReduced = gamelistlist[restart_index: restart_index + remaining - 100]
        count = 1
        for g in gamelistReduced:
            remaining -= 1
            count += 1
            print("remain: " +str(remaining))
            print("count: " + str(count))
            if count < remaining - 100:
                gamestat = api.NBA.get_statistics_by_game(g["id"])
                gameplaceholder = gamestat.json()['response']
                try:
                    gameobj = {"id": g["id"]}
                    gameobj["team_1"] = gameplaceholder[0]
                    gameobj["team_2"] = gameplaceholder[1]
                    print(gameobj)
                    game_stats.insert_one(gameobj)
                    dbstats.insert_one({"message": "last gamestat added ID: " + str(g["id"]) + " Count: " + str(count), "game_id":g["id"]})
                except:
                    get_game_stats(add_index + 1)



def clean_list():
    gamelist = list(games.find({}))
    game_ids = [i["id"] for i in gamelist]
    #print(game_ids)
    for id in game_ids:
        if game_ids.count(id) > 1:
            print("Duplicate Id: " + str(id))
    gamestatlist = list(game_stats.find({}))
    game_stat_ids = [i["id"] for i in gamestatlist]
    for id in game_stat_ids:
        if game_stat_ids.count(id) > 1:
            print("Duplicate game_stat_id: " + str(id))
    missing_game_stats = db["missing_game_stats"]
    for id in game_ids:
        if id not in game_stat_ids:
            print("Adding game: " + str(id))
            missing_game_stats.insert_one({"missing_game_id": id})
    count_deleted = 0
    # for id in game_stat_ids:
    #     if game_stat_ids.count(id) > 1:
    #         dupe = game_stats.find_one({"id": id})
    #         dupe_id = dupe["_id"]
    #         objId = ObjectId(dupe_id)
    #         print(dupe_id)
    #         dupelist = game_stats.find({"$and":[{"id": id}, {"_id": {"$ne" : objId}}]})
    #         print("Dupe Id: " + str(dupe["_id"]))
    #         print("-----")
    #         duple = list(dupelist)
    #         for i in duple:
    #             game_stats.delete_one(i)



    #print(game_stat_ids)


count = 1
if count == 1:
    #print(call_test())
    # get_last_db_entry()
    # get_game_stats(0, 9261)         
    clean_list()


    
  


