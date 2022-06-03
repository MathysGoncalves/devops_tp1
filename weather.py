import requests, json, os

base_url = "http://api.openweathermap.org/data/2.5/weather?"

def get_wheather(lat, lon, api_key):

    complete_url = base_url + "lat=" + str(lat) + "&lon=" + str(lon) + "&appid=" + str(api_key)
    response = requests.get(complete_url)
    x = response.json()
    if x["cod"] != "404":
        y = x["main"]
        print(y["temp"])
    else : 
        print("Try another coord")


if __name__ == '__main__':

    get_wheather(os.environ.get('LAT'), os.environ.get('LONG'), os.environ.get('API_KEY'))
