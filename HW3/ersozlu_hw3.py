#cd C:\Users\Ecem\Documents\Okul\2019-Spring\INTL550
#cd /home/eers/Documents

import pandas as pd
import pystan
import seaborn as sns

#Importing data
rdata = pd.read_csv('trend2.csv')
data = rdata.dropna()
data.columns = data.columns.map(str.strip)

#Indexing
country = data.country.str.strip()
counts = country.unique()
countsno = len(counts)


#local copies of variables
country_lookup = dict(zip(counts, range(countsno)))
#year_lookup = dict(zip(data.year.unique()), range(len(data.year.unique())))
countries = data['cc'] = country.replace(country_lookup).values
#years = data['year'] = data.year.replace(year_lookup).values
gini_net = data.gini_net.values
rgdpl = data.rgdpl.values
church2 = data.church2.values


#First Model,varying country intercepts with diffuse prior (from varying_intercept & hierachical_intercept)

varying_intercept_model1 = """

data {
  int<lower=0> J; 
  int<lower=0> N; 
  int<lower=1,upper=J> countries[N];
  vector[N] x1;
  vector[N] x2;
  vector[N] y;
} 

parameters {
  vector[J] a;
  vector[2] b;
  real mu_a;
  real<lower=0,upper=100> sigma_a;
  real<lower=0,upper=100> sigma_y;
} 

transformed parameters {
  vector[N] y_hat;
  vector[N] m;
  for (i in 1:N) {
    m[i] = a[countries[i]] + x2[i] * b[1];
    y_hat[i] = m[i] + x1[i] * b[2];
  }
}
  
model {
  sigma_a ~ uniform(0, 100);
  mu_a ~ normal(0, 1);
  a ~ normal (mu_a, sigma_a);
  b ~ normal (0, 1);
  sigma_y ~ uniform(0, 100);
  y ~ normal(y_hat, sigma_y);
}
"""

varying_intercept_model1_data = {'N': len(church2),
                                 'J': countsno,
                                 'countries': countries + 1,
                                 'x1': gini_net,
                                 'x2': rgdpl,
                                 'y': church2
                                 }

varying_intercept_model1_fit = pystan.stan(model_code=varying_intercept_model1, data=varying_intercept_model1_data, iter=1000, chains=2)


#Second Model, varying country intercepts with informative prior

varying_intercept_model2 = """

data {
  int<lower=0> J; 
  int<lower=0> N; 
  int<lower=1,upper=J> countries[N];
  vector[N] x1;
  vector[N] x2;
  vector[N] y;
} 

parameters {
  vector[J] a;
  vector[2] b;
  real mu_a;
  real<lower=0,upper=100> sigma_a;
  real<lower=0,upper=100> sigma_y;
} 

transformed parameters {
  vector[N] y_hat;
  vector[N] m;
  for (i in 1:N) {
    m[i] = a[countries[i]] + x2[i] * b[1];
    y_hat[i] = m[i] + x1[i] * b[2];
  }
}
  
model {
  sigma_a ~ uniform(0, 100);
  mu_a ~ normal(0, 1);
  a ~ normal (mu_a, sigma_a);
  b1 ~ normal (0, 100);
  b2 ~ normal (0, 1);
  sigma_y ~ uniform(0, 100);
  y ~ normal(y_hat, sigma_y);
}
"""

varying_intercept_model2_data = {'N': len(church2),
                                 'J': countsno,
                                 'countries': countries + 1,
                                 'x1': gini_net,
                                 'x2': rgdpl,
                                 'y': church2
                                 }

varying_intercept_model2_fit = pystan.stan(model_code=varying_intercept_model1, data=varying_intercept_model1_data, iter=1000, chains=2)































