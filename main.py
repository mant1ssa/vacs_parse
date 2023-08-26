import requests
import json

test = requests.get("https://api.hh.ru/vacancies")
test = test.json()

print(test)