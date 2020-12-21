import requests
from random import *
from datetime import date

# Creates a forever loop
while True:
    # Gets today's date
    date = date.today()
    # Splits the date at every "-" because date format is "DD-MM-YYYY"
    split_date = str(date).split("-")
    # Gets a random number from 2015 to the current year for the Year variable
    Year = randint(2015, int(split_date[0]))
    # Checks if the random Year is equal to the current year
    if str(Year) == split_date[0]:
        # Creates a Month variable using a random number from January(1) to the current month
        Month = randint(1, int(split_date[1]))
    else:
        # Creates a Month variable using a random number from January(1) to December(12)
        Month = randint(1, 12)
    # Checks if the random Month is equal to the current month
    if str(Month) == split_date[1]:
        # Creates a Day variable using a random number from 1 to the current day in the month
        Day = randint(1, int(split_date[2]))
    else:
        # Creates a Day variable using a random number from 1 to 30
        Day = randint(1, 30)
    # Makes a request to the NASA APOD API using the Year, Month, and Day variables from above
    req = requests.get(f"https://api.nasa.gov/planetary/apod?api_key=Guv4egEEeC4kQxHBTEu4DDH26HGW4cWLNCYo2Npd&date={Year}-{Month}-{Day}")
    # Prints the media type of the image and the url of the image
    print(req.json()['media_type'], req.json()['url'])
    # Checks if the file is an image and not a video
    if req.json()['media_type'] == 'image':
        # Gets the url of the image
        apod_url = req.json()['url']
        # Breaks out of the forever loop
        break

# Prints the url of the image
print(apod_url)
# Prints the headers that the API returns
print(req.headers)
