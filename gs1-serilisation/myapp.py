import requests
URL="http://127.0.0.1:8000/stuinfo/4"

r=requests.get(url=URL)

data=r.json()
print(data)
 
#python applocation who communicate with our api

#just like a destop application who fetch data from webapp
