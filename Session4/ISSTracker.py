# ISS Tracker
import requests

url = "http://api.open-notify.org/iss-now.json"

response = requests.get(url).json() # get the response from the API convert from JSON to dictionary
print(response)


latitude = float(response["iss_position"]["latitude"])
longitude = float(response["iss_position"]["longitude"])
# 
print(latitude)
print(longitude)