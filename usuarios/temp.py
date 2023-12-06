import requests

def obtener_temperatura():
    parameters = {'key': '8lapa45o2ynexdd1frdb78ll4mxrdyn4h6xd624y',
                'lat':'-33.482672626788144',
                'lon':'-70.62155116475428'}

    url = "https://www.meteosource.com/api/v1/free/point?lat=29S&lon=37W&sections=all&timezone=GMT&language=en&units=metric&key=8lapa45o2ynexdd1frdb78ll4mxrdyn4h6xd624y"

    data = requests.get(url, parameters).json()
    temp = data["current"]["temperature"]
    return temp