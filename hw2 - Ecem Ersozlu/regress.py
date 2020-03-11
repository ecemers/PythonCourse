# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 22:50:12 2020

@author: Ecem
"""
import numpy as np
from scipy import stats
import math as m
import matplotlib.pyplot as plt 

def regress(data):
    df = data.dropna()
#    x1 = df.iloc[:, 0:1]
#    x2 = df.iloc[:, 1:2]
#    x = np.hstack((x1, x2))
    x = df.iloc[:, 0:2].values
    y = df.iloc[:, 2:3].values
    n = len(y)
    k = len(df.columns)
    x = np.hstack([np.ones((len(x),1)), x])
    b = np.linalg.inv(x.T @ x) @ x.T @ y
    e = y - x@b
    varb = ((e.T @ e) / n-k-1) * np.linalg.inv(x.T @ x)
    Variance = e.T @ e
    SE = m.sqrt(Variance)
#alpha is 0.5
    t = stats.t.ppf(0.975, n-k-1)
    interval = [float(b[1]) - SE*t, float(b[1]) + SE*t]
    print("β:%s\nStandard Error:%f\nConfidence Interval:%s\n" %(varb, SE, interval))
    return plt.plot((df.iloc[:, 0:1].values), y) 