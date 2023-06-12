import requests

url = 'https://swapi.dev/api/'
response=requests.get(url).json()

planets_api=response.get('planets')
def check_planets(api):
    for i in range(1,6):
        req_planet=requests.get(f'{api}/{i}').json()
        diam = req_planet.get('diameter')
        print(diam)
check_planets(planets_api)