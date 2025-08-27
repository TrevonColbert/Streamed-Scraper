#Add any parameters to be accessed by other files

#Sports parameter (list of sports I am interested in at the time) (american-football, basketball, fight [for wwe & ufc], baseball??)

import requests

url = "https://streamed.pk/api/sports"

response = requests.get(url)

print(response.json())

