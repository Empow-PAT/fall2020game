import requests
from random import *
from datetime import date

date = date.today()
split_date = str(date).split("-")
Year = randint(2015, int(split_date[0]))
Month = randint(1, int(split_date[1]))
if str(Year) == split_date[0]:
    Month = randint(1, int(split_date[1]))
else:
    Month = randint(1, 12)
if str(Month) == split_date[1]:
    Day = randint(1, int(split_date[2]))
else:
    Day = randint(1, 30)

req = requests.get(f"https://api.nasa.gov/planetary/apod?api_key=Guv4egEEeC4kQxHBTEu4DDH26HGW4cWLNCYo2Npd&date={Year}-{Month}-{Day}")

apod_json = req.json()

print(apod_json)
print(req.headers)

print(apod_json["url"])