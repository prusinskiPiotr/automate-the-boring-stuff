#! python3 
# quickweather - Prints the weather for a location from the command line

import json, requests, sys

# Compute location from command line arguments.
if len(sys.argv) < 2:
    print('Usage: Prints the weather for a location from the command line.')
    sys.exit()
location = ' '.join(sys.argv[1:])

print(location)

# TODO: Download the JSON data from openWeatherMap.org's API.
url = "http://samples.openweathermap.org/data/2.5/weather?q=" + location + "&appid=5ffca13023ed75ffa78ea18a8226875a"
# response = requests.get(url)
# response.raise_for_status()

print(url)
# TODO: Load JSON data into a Python variable.
