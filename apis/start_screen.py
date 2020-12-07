import requests
from random import *
from datetime import date

while True:
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
    print(req.json()['media_type'], req.json()['url'])
    if req.json()['media_type'] == 'image':
        apod_url = req.json()['url']
        break

print(apod_url)
print(req.headers)
