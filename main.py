# step 1: import requests
import requests
from dotenv import dotenv_values
print("hello")
print("hello")
dotenv = dotenv_values(".env")
# step 2: call api with given endpoint and key
api_result = requests.get('https://api.aviationstack.com/v1/flights?access_key=' + dotenv["api_key"])
print(dotenv["api_key"])
# requests the data from the endpoint
# step 3: convert to dictionary and grab only the "data" value
api_result = api_result.json()
data = api_result["data"] 
# step 4: loop through the flights and check which flights are active
for flight in data: # loops through all flights 
# step 5: if active, print the airline, date, departure airport and arrival airport
    if (flight["flight_status"] == "active"): # checks if flight is active 
        print("Flight airline: " + flight["airline"]["name"]) # airline
        print("Flight date: " + flight["flight_date"]) # date of flight
        print("Flight departure airport: " + flight["departure"]["airport"]) # departure airport
        print("Flight arrival airport: " + flight["arrival"]["airport"]) # arrival airport
        print("-----------------------------------------------")