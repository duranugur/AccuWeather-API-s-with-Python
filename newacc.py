import json
import time
import urllib

API = "lRW9GqOmhreEIsy8GJYwOC1Lhjs7zeXx"
countryCode = "IN"
city = input("City Name:")
print(city)

key = ""
def getLocation(countryCode, city):
    search_address = "http://dataservice.accuweather.com/locations/v1/cities/" + countryCode + "/search?apikey=lRW9GqOmhreEIsy8GJYwOC1Lhjs7zeXx&q=" + city + "&details=true"
    # print (search_address)//I check it I see search address for adana.
    with urllib.request.urlopen(search_address) as search_address:
        data = json.loads(search_address.read().decode())
    # print(data)//I see location requiment
    location_key = data[0]['Key']
    return (location_key)


def getForcast(location_key):
    daily_forcastUrl = "http://dataservice.accuweather.com/forecasts/v1/daily/5day/" + location_key + "?apikey=lRW9GqOmhreEIsy8GJYwOC1Lhjs7zeXx&details=true"

    with urllib.request.urlopen(daily_forcastUrl) as daily_forcastUrl:
        data = json.loads(daily_forcastUrl.read().decode())
    # print(data)
    for key1 in data['DailyForecasts']:
        print("Weather Forcast for" + key1['Date'])
        print("Min Temp for Fahreheit):" + str(key1['Temperature']['Minimum']['Value']))
        print("Max Temp for Fahrenheit):" + str(key1['Temperature']['Maximum']['Value']))
        print("Day Forcast):" + str(key1['Day']['ShortPhrase']))
        print("----------------------")


key = getLocation(countryCode, city)
getForcast(key)
