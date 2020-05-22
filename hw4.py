"""
Homework 4
Ecem Ersözlü

"""

import pandas as pd
import os
import numpy as np

os.chdir('/home/eers/Documents/HW4')
tt = pd.read_csv('immSurvey.csv')
tt.head()

alphas = tt.stanMeansNewSysPooled
sample = tt.textToSend

from sklearn.feature_extraction.text import CountVectorizer
vec = CountVectorizer()
X = vec.fit_transform(sample)
X

pd.DataFrame(X.toarray(), columns=vec.get_feature_names())

from sklearn.feature_extraction.text import TfidfVectorizer
vec = TfidfVectorizer()
X = vec.fit_transform(sample)
pd.DataFrame(X.toarray(), columns=vec.get_feature_names())

from sklearn.model_selection import train_test_split #cross_validation changed into model_selection
Xtrain, Xtest, ytrain, ytest = train_test_split(X, alphas,
random_state=1)

from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import ConstantKernel, RBF
rbf = ConstantKernel(1.0) * RBF(length_scale=1.0)
gpr = GaussianProcessRegressor(kernel=rbf, alpha=1e-8)

gpr.fit(Xtrain.toarray(), ytrain)

mu_s, cov_s = gpr.predict(Xtest.toarray(), return_cov=True)

np.corrcoef(ytest, mu_s)

#The correlation coefficient is 0.68328523 as the model stands

#Adding bigrams
bigram_vectorizer = CountVectorizer(ngram_range=(2, 2), token_pattern=r'\b\w+\b', min_df=1)
X = bigram_vectorizer.fit_transform(sample)

pd.DataFrame(X.toarray(), columns=bigram_vectorizer.get_feature_names())

Xtrain, Xtest, ytrain, ytest = train_test_split(X, alphas, random_state=1)

rbf = ConstantKernel(1.0) * RBF(length_scale=1.0)
gpr = GaussianProcessRegressor(kernel=rbf, alpha=1e-8)

gpr.fit(Xtrain.toarray(), ytrain)

mu_s, cov_s = gpr.predict(Xtest.toarray(), return_cov=True)

np.corrcoef(ytest, mu_s)

#The correlation coefficient is 0.47034325, thus lower when we use bigrams. 
#We see a lower correlation when we get closer to ground-truth.

