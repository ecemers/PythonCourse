#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ecem Ersözlü
Final Paper - Data Analysis Code
"""
import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
import math
from scipy import stats

os.chdir('/home/eers/Documents/Final')


#Importing data
data = pd.read_csv('data.csv')
data = data.set_index("Country")
data1 = data.drop({"Australia", "Greece", "United States"})
data1 = data1.dropna()
IP = data1["Ideological"].values #originally scaled 0-10
AP = data1["Affective"].values #originally scaled 0-4
data1.to_csv('/home/eers/Documents/Final/data1.csv')
counts = data1.index
data1.insert(0, "Country", counts, allow_duplicates=False)
counts = data1["Country"].str.strip()
countsno = len(counts)
country_lookup = dict(zip(counts, range(countsno)))
countries = data1["Country"] = counts.replace(country_lookup).values

#scaling 
IP = np.log(IP)
AP = np.log(AP)

#Linear regression
slope, intercept, r_value, p_value, std_err = stats.linregress(IP,AP)
#slope = -0.23782406497272232, r = np.corrcoef(IP, AP) = -0.3052086745177408, 
#p = 0.10740124510769342 (> alpha=0.05), SE = 0.14280526274633756

#95% confidence interval for correlation coefficient
t = stats.t.ppf(0.975, countsno-1)
CI = [(r_value - std_err*t), (r_value + std_err*t)]
#[-0.597731994613285, -0.012685354422196649]

#plotting
plt.figure(figsize=(20,20))
#plt.xlim(-2.5, 2)
#plt.ylim(-2.5, 2)
plt.xlabel("Ideological Polarization", )
plt.ylabel("Affective Polarization")
plt.title("Comparison of Polarization Types")
plt.grid(True)
plot = plt.scatter(IP, AP, marker="o", color="green")
labels = dict(zip(range(countsno), counts.values))
for i, c in enumerate(labels):
    c = labels[i]
    plt.annotate(c, (IP[i], AP[i]), ha="center")
plot.figure.savefig("Comp.png")

#Gaussian test
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF, ConstantKernel as C
Xtrain = pd.DataFrame(data1.Ideological)
ytrain = data1["Country"]
Xtest = pd.DataFrame(data1.Affective)
ytest = data1["Country"]

kernel = C(1.0, (1e-3, 1e3)) * RBF(10, (1e-2, 1e2))
gp = GaussianProcessRegressor(kernel=kernel, n_restarts_optimizer=9)
gp.fit(Xtrain, ytrain)

gp.fit(Xtest, ytest)
y_pred1, std = gp.predict(Xtest, return_std=True)
MSE = ((y_pred-ytest)**2).mean()
#1.2992207967113747e-22


