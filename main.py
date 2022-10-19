from dotenv import load_dotenv, find_dotenv
import json, requests, os

load_dotenv(find_dotenv())

API_KEY = os.environ.get("API_KEY")

city = None
baseURL = "http://api.openweathermap.org/data/2.5/weather?"
completeURL = f"{baseURL}appid={API_KEY}&q={city}"

response = requests.get(completeURL).json()

testResponse = {"deg": 214}

directions=["North","North North East","North East","East North East","East","East South East","South East",
            "South South East","South","South South West","South West","West South West","West","West North West",
            "North West","North North West"]

print(directions[int((testResponse["deg"]/22.5))%16])
