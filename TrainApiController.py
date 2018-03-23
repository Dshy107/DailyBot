# Project: DailyBot
# FileName: TrainApiController
# Current User: Rasmus laptop
# Date Created: 09/03/2018
# Developed in PyCharm

import requests

api_adress = "http://xmlopen.rejseplanen.dk/xml/rest/hafasRestDepartureBoard.xsd/location?=input%20input"

station = input("Station name: ")
url = api_adress
