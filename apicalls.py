import constants.constants as cs
import requests

class NBA():

    def run_open():
        url = "https://api-nba-v1.p.rapidapi.com/seasons"

        headers = {
            "X-RapidAPI-Key": cs.RAPID_API_KEY,
            "X-RapidAPI-Host": cs.RAPID_API_HOST_NBA
        }

        response = requests.request("GET", url, headers=headers)

        return response.text
