import requests
import json 
#yhaa se table me insert krwana hhh
#data is comng from client and hove to insert in our DB

URL="http://127.0.0.1:8000/studentapi/"
# it return data through id......
def get_data(id=None):
    data={}
    if id is not None:
        data={'id':id}
    json_data=json.dumps(data)
    r=requests.get(url=URL,data=json_data)
    data=r.json()
    print(data)
get_data(3)
    # it add data to DB
def post_data():
    data={
        'name':'Ravi',
        'roll':106,
        'city':'Dhanbad'
    }

    json_data=json.dumps(data)
    r=requests.post(url=URL,data=json_data)
    data=r.json()
    print(data)

#post_data()
    
def update_dataa():

    print("----------1 ")
    data={
        'id':3,
        'name':'Rohan',
        'city':'Bokare'
    }
    print("----------2 ")
    json_data=json.dumps(data)
    print("------3 ")
    r=requests.put(url=URL,data=json_data)
    data=r.json()
    print(data)

#update_dataa()


def delete_dataa():   
    data={
        'id':6,
        
    }
 
    json_data=json.dumps(data)
    print("------3 ")
    r=requests.delete(url=URL,data=json_data)
    data=r.json()
    print(data)

#delete_dataa()



   
