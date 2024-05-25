import os
import requests
from constants import DEFAULT_DAYS
from dotenv import load_dotenv
from mapper import ResponseMapper


class WeatherAPI:
    def __init__(self):
        load_dotenv()
        self.url = os.getenv("WEATHER_API_URL")
        self.api_key = os.getenv("WEATHER_API_KEY")
        self.api_host = os.getenv("WEATHER_API_HOST")

    def get_weather(self, city):
        querystring = {"q": city, "days": DEFAULT_DAYS}
        headers = {
            "X-RapidAPI-Key": self.api_key,
            "X-RapidAPI-Host": self.api_host
        }
        response = requests.get(self.url, headers=headers, params=querystring)
        if response.status_code == 200:
            data = response.json()
            location = data["location"]
            current = data["current"]
            return ResponseMapper.map_response(current, location)
        else:
            return None
