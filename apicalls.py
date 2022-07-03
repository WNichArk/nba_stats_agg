import constants.constants as cs
import requests

class NBA():

    def get_seasons():
        url = "https://api-nba-v1.p.rapidapi.com/seasons"

        headers = {
            "X-RapidAPI-Key": cs.RAPID_API_KEY,
            "X-RapidAPI-Host": cs.RAPID_API_HOST_NBA,
            "X-RapidAPI-Requests-remaining": ""
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
        response = requests.request("GET", url, headers=headers, params=querystring)
        return response

    def get_teams():

        url = "https://api-nba-v1.p.rapidapi.com/teams"

        headers = {
            "X-RapidAPI-Key": cs.RAPID_API_KEY,
            "X-RapidAPI-Host": cs.RAPID_API_HOST_NBA
        }

        response = requests.request("GET", url, headers=headers)

        return response

    def get_players_by_team_and_season(team_id, season):
        url = "https://api-nba-v1.p.rapidapi.com/players"

        querystring = {"team":team_id,"season":season}

        headers = {
            "X-RapidAPI-Key": cs.RAPID_API_KEY,
            "X-RapidAPI-Host": cs.RAPID_API_HOST_NBA
        }

        response = requests.request("GET", url, headers=headers, params=querystring)

        return response

    def get_statistics_by_player_and_season(player_id, season):
        url = "https://api-nba-v1.p.rapidapi.com/players/statistics"

        querystring = {"id":player_id,"season":season}

        headers = {
            "X-RapidAPI-Key": cs.RAPID_API_KEY,
            "X-RapidAPI-Host": cs.RAPID_API_HOST_NBA
        }

        response = requests.request("GET", url, headers=headers, params=querystring)

        return response
    
    def get_statistics_by_team_and_seasion(team_id, season):
        url = "https://api-nba-v1.p.rapidapi.com/teams/statistics"

        querystring = {"id":team_id,"season":season}

        headers = {
            "X-RapidAPI-Key": cs.RAPID_API_KEY,
            "X-RapidAPI-Host": cs.RAPID_API_HOST_NBA
        }

        response = requests.request("GET", url, headers=headers, params=querystring)

        return response