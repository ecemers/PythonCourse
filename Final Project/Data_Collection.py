#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ecem Ersözlü

Final - Getting Data
"""

import numpy as np
import pandas as pd
import os

os.chdir('/home/eers/Documents/Final')

#Affective Polarizatipn Index from V-Dem
vdem = pd.read_csv("Political polarization.csv")
AP = pd.DataFrame(vdem)
AP = AP.set_index("Year")
AP = AP.fillna(method='bfill')
AP = AP.fillna(0)
countries = pd.Series(AP.columns)
years = pd.Series(AP.index)
APbycountry = pd.Series(AP.mean())
APbycountry = pd.DataFrame(APbycountry).set_index(countries)
APbycountry.columns = ["Affective"]


#Ideological Polarization Index from Dalton's Party Polarization Index
cses = pd.read_csv("PPI.csv")
IP = pd.DataFrame(cses)
IPbycountry = IP.set_index("Country")
IPbycountry.rename(columns={"Polarization": "Ideological"}, inplace=True)

#Merging for analysis
APbycountry = APbycountry.drop({"Argentina", "Latvia", "Peru"}) #no Module 3 or 4 IP data
#API = np.array(APbycountry['Affective'])
#API = API.reshape(38,1)
df = pd.concat([IPbycountry, APbycountry.reindex(IPbycountry.index)], axis=1)
df.to_csv('/home/eers/Documents/Final/data.csv')


