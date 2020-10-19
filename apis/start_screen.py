import requests
from random import *
from datetime import date
import json

date = date.today()
split_date = str(date).split("-")
Year = randint(2015, int(split_date[0]))
Month = randint(1, int(split_date[1]))
if str(Month) == split_date[1]:
    Day = randint(1, int(split_date[2]))
else:
    Day = randint(1, 30)

req = requests.get("https://api.nasa.gov/planetary/apod?api_key=Guv4egEEeC4kQxHBTEu4DDH26HGW4cWLNCYo2Npd&date={}-{}-{}".format(randint(2015, int(split_date[0])), randint(1, int(split_date[1])), randint(1, int(split_date[2]))))

apod_json = req.json()

print(apod_json)

print(apod_json["url"])