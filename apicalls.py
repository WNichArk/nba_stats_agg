import constants.constants as cs
import requests

class NBA():

    remaining_requests = 0

    def get_seasons():
        url = "https://api-nba-v1.p.rapidapi.com/seasons"

        headers = {
            "X-RapidAPI-Key": cs.RAPID_API_KEY,
            "X-RapidAPI-Host": cs.RAPID_API_HOST_NBA
        }

        response = requests.request("GET", url, headers=headers)
        return response
    
    def get_games_by_season(season):

        url = "https://api-nba-v1.p.rapidapi.com/games"

        querystring = {
            "season":season           
             }
        headers = {
            "X-RapidAPI-Key": cs.RAPID_API_KEY,
            "X-RapidAPI-Host": cs.RAPID_API_HOST_NBA           
             }
        if NBA.check_remaining_requests()["continue"]:
            response = requests.request("GET", url, headers=headers, params=querystring)
            return response
        else:
            return []

    def get_teams():

        url = "https://api-nba-v1.p.rapidapi.com/teams"

        headers = {
            "X-RapidAPI-Key": cs.RAPID_API_KEY,
            "X-RapidAPI-Host": cs.RAPID_API_HOST_NBA
        }
        if NBA.check_remaining_requests()["continue"]:
            response = requests.request("GET", url, headers=headers)
            return response
        else:
            return []

    def get_players_by_team_and_season(team_id, season):
        url = "https://api-nba-v1.p.rapidapi.com/players"

        querystring = {"team":team_id,"season":season}

        headers = {
            "X-RapidAPI-Key": cs.RAPID_API_KEY,
            "X-RapidAPI-Host": cs.RAPID_API_HOST_NBA
        }
        if NBA.check_remaining_requests()["continue"]:
            response = requests.request("GET", url, headers=headers, params=querystring)
            return response
        else:
            return []

    def get_statistics_by_player_and_season(player_id, season):
        url = "https://api-nba-v1.p.rapidapi.com/players/statistics"

        querystring = {"id":player_id,"season":season}

        headers = {
            "X-RapidAPI-Key": cs.RAPID_API_KEY,
            "X-RapidAPI-Host": cs.RAPID_API_HOST_NBA
        }

        if NBA.check_remaining_requests()["continue"]:
            response = requests.request("GET", url, headers=headers, params=querystring)
            return response
        else:
            return []
    
    def get_statistics_by_team_and_seasion(team_id, season):
        url = "https://api-nba-v1.p.rapidapi.com/teams/statistics"

        querystring = {"id":team_id,"season":season}

        headers = {
            "X-RapidAPI-Key": cs.RAPID_API_KEY,
            "X-RapidAPI-Host": cs.RAPID_API_HOST_NBA
        }
        if NBA.check_remaining_requests()["continue"]:
            response = requests.request("GET", url, headers=headers, params=querystring)
            return response
        else:
            return []

    def get_statistics_by_game(game_id):
        url = "https://api-nba-v1.p.rapidapi.com/games/statistics"

        querystring = {"id":game_id}

        headers = {
            "X-RapidAPI-Key": cs.RAPID_API_KEY,
            "X-RapidAPI-Host": cs.RAPID_API_HOST_NBA
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        return response

    def check_remaining_requests():
        res = NBA.get_seasons()
        remaining = res.headers['X-RateLimit-requests-Remaining']
        print("Request remaining: " + str(remaining))
        if int(remaining) < 100:
            return {"continue": False, "remaining": int(remaining)}
        else:
            return {"continue": True, "remaining": int(remaining)}

    