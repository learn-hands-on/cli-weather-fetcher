from dotenv import load_dotenv, find_dotenv
import json, requests, os

load_dotenv(find_dotenv())

API_KEY = os.environ.get("API_KEY")

city = None
baseURL = "http://api.openweathermap.org/data/2.5/weather?"
completeURL = f"{baseURL}appid={API_KEY}&q={city}"

response = requests.get(completeURL).json()