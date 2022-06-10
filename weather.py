import requests, os
from flask import Flask
from flask import request

base_url = "http://api.openweathermap.org/data/2.5/weather?"
app = Flask(__name__)

@app.route('/')
def get_wheather():
    lat = request.args.get("lat")
    lon = request.args.get("lon")
    print("-------------->", lat, lon)
    complete_url = base_url + "lat=" + str(lat) + "&lon=" + str(lon) + "&appid=" + str(os.environ.get('API_KEY'))
    response = requests.get(complete_url)
    x = response.json()
    if x["cod"] != "404":
        y = x["main"]
        print(y["temp"])
    else : 
        print("Try another coord")
    return str(y["temp"])


if __name__ == '__main__':

    app.run(port = 8081,debug=True)
    get_wheather()
