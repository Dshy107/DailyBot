# Project: DailyBot
# FileName: MotionSensorController
# Current User: Rasmus laptop
# Date Created: 09/03/2018
# Developed in PyCharm

#Import requests library
import requests

# Variables
#       location
location = "Roskilde"

#       params dict to be sent to the API
PARAMS = {'address':location}

#       api-endpoint
URL = "http://vejr.eu/api.php?location="+location+"&degree=C"

#       quests to be sent and saving the response object
r = requests.get(url=URL, params=PARAMS)


