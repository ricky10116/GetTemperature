# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 10:28:03 2019

@author: rshang
"""

import requests

def Gettemperature(city):
    param = {"product": "observation","name": city,"app_id": "DemoAppId01082013GAL","app_code": "AJKnXv84fjrb0KIHawS0Tg"}
    
    r=requests.get('https://weather.cit.api.here.com/weather/1.0/report.json?', params=param)
    #print(r.url)  
    str1 = r.text
    str2 = ",\"temperature\":\""
    get1=str1.find(str2)   # start
    remain = str1[get1+len(str2):]
    get2=remain.find("\",\"tem")   
    
    Temperature=str1[get1+len(str2):get1+len(str2)+get2]

    print("Temperature=",Temperature)
    print(type(Temperature))
    return Temperature

#Gettemperature("Taipei")
#Gettemperature()  
#https://weather.cit.api.here.com/weather/1.0/report.json?product=observation&name=Chicago&app_id=DemoAppId01082013GAL&app_code=AJKnXv84fjrb0KIHawS0Tg