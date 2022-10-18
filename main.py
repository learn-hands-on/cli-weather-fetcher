from dotenv import load_dotenv, find_dotenv
import json, requests, os

load_dotenv(find_dotenv())

API_KEY = os.environ.get("API_KEY")

city = None
baseURL = "http://api.openweathermap.org/data/2.5/weather?"
completeURL = f"{baseURL}appid={API_KEY}&q={city}"

response = requests.get(completeURL).json()

testResponse = {"deg": 214}

if testResponse["deg"]==0 or testResponse["deg"]==360:
    print("North")

elif testResponse["deg"]==90:
    print("East")
    
elif testResponse["deg"]==180:
    print("South")
elif testResponse["deg"]==270:
    print("West")
else:
 if testResponse["deg"]<270 and testResponse["deg"]>180:
    if testResponse["deg"]<225:
        print("South-South-West")
    elif testResponse["deg"]==225:
        print("North-West")
    else:
        print("North-South-West")
 elif testResponse["deg"]>270 and testResponse["deg"]<360:
    if testResponse["deg"]<315:
        print("South-North-West")
    elif testResponse["deg"]==315:
        print("North-West")
    else:
        print("North-North-West")
 elif testResponse["deg"]>0 and testResponse["deg"]<90:
    if testResponse["deg"]<45:
        print("North-North-East")
    elif testResponse["deg"]==45:
        print("North-East")
    else:
        print("South-North-East")
 elif testResponse["deg"]>90 and testResponse["deg"]<180:
    if testResponse["deg"]<135:
        print("North-South-East")
    elif testResponse["deg"]==135:
        print("South-East")
    else:
        print("South-South-East")