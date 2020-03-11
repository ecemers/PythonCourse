# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 22:50:12 2020

@author: Ecem
"""
import numpy as np
from scipy import stats
import pandas as pd
import math as m
import wbdata

#getting indicators
wbdata.get_indicator(source=14)
#'SG.GEN.PARL.ZS' = % of women in national parliament
#'NY.GDP.MKTP.CD' = GDP (current US$)  
#'SH.STA.MMRT2' = Maternal mortality ratio (modeled estimate, per 100,000 live births)
indicators = {"SG.GEN.PARL.ZS": "Female_MPs", "NY.GDP.MKTP.CD": "GDP", "SH.STA.MMRT": "Maternal_Mortality"}

#getting data
countries = [i['id'] for i in wbdata.get_country(incomelevel="LIC", display=False)] 
Gender = wbdata.get_dataframe(indicators, country=countries, convert_date=True, keep_levels=True)
Gender.to_csv('C:/Users/Ecem/class/hwdata.csv')

data = Gender
x1 = Gender.iloc[:, 0:1]
x2 = Gender.iloc[:, 1:2]
y = Gender.iloc[:, 2:3]
x = np.hstack((x1, x2))

from regress import regress
regress(Gender)