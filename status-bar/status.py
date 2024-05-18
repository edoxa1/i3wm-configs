#!/usr/bin/env python3

import os
import requests

uri = "https://api.open-meteo.com/v1/forecast?latitude=51.1801&longitude=71.446&current_weather=true&hourly=temperature_2m"
response = requests.get(uri)


print(f"{response.json()['current_weather']['temperature']}*C")
# -modi "run,drun,Weather:weather.py" -show Weather
