# -*- coding: utf-8 -*-

"""
Created on Tue May 31 16:32:02 2016

@author: jrbrad
"""

import requests
from lxml import objectify

parameter = 'tavg'
state = '44'
month = '08'
year = '2016'
url = 'https://www.ncdc.noaa.gov/cag/statewide/rankings/%s-%s-%s%s.xml'
# urlParameters = ()
#print(url % (state, parameter, year, month))

response = requests.get(url % (state, parameter, year, month)).content
root = objectify.fromstring(response)

my_wm_username = 'jcranson'

print(my_wm_username)
print(root['data'] [4] ["value"])
print(root['data'] [4] ["mean"])
print(root['data'] [4] ["departure"])
print(root['data'] [4] ["lowRank"])
print(root['data'] [4] ["highRank"])
