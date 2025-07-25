import requests
import json

class Generator:
    def __init__(self,nutrition_input:list,ingredients:list=[],params:dict={'n_neighbors':5,'return_distance':False}):
        self.nutrition_input=nutrition_input
        self.ingredients=ingredients
        self.params=params

    def set_request(self,nutrition_input:list,ingredients:list,params:dict):
        self.nutrition_input=nutrition_input
        self.ingredients=ingredients
        self.params=params

    def generate(self,):
        request={
            'nutrition_input':self.nutrition_input,
            'ingredients':self.ingredients,
            'params':self.params
        }
        #response=requests.post(url='http://backend:8080/predict/',data=json.dumps(request))
        response = requests.post(url='http://10.71.117.233:8080/predict/', data=json.dumps(request)) #mobile 
        #response = requests.post(url='http://192.168.29.101:8080/predict/', data=json.dumps(request)) #wifi


        return response
