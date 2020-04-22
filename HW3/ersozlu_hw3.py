#cd C:\Users\Ecem\Documents\Okul\2019-Spring\INTL550
#cd /home/eers/Documents

import pandas as pd
import pystan

#Importing data
rdata = pd.read_csv('trend2.csv')
data = rdata.dropna()
data.columns = data.columns.map(str.strip)

#Indexing
country = data.country.str.strip()
counts = country.unique()
countsno = len(counts)
year = data.year.unique()

#Local copies of variables
country_lookup = dict(zip(counts, range(countsno)))
year_lookup = dict(zip(year, range(len(year))))
countries = data['cc'] = country.replace(country_lookup).values
years = data['year'] = data.year.replace(year_lookup).values
gini_net = data.gini_net.values
rgdpl = data.rgdpl.values
church2 = data.church2.values


#First Model,varying country-year intercepts with diffuse prior (from varying_intercept & hierachical_intercept)
varying_intercept_model1 = """

data {
  int<lower=0> J1;
  int<lower=0> J2;
  int<lower=0> N;
  int<lower=1,upper=J1> countries[N];
  int<lower=1,upper=J2> years[N];
  vector[N] x1;
  vector[N] x2;
  vector[N] y;
}

parameters {
  vector[J1] a1;
  vector[J2] a2;
  vector[2] b;
  real mu_a1;
  real mu_a2;
  real<lower=0,upper=100> sigma_a1;
  real<lower=0,upper=100> sigma_a2;
  real<lower=0,upper=100> sigma_y;
  real alpha;
}

transformed parameters {
  vector[N] y_hat;
  vector[N] m;
  for (i in 1:N) {
    m[i] = alpha + a1[countries[i]] + a2[years[i]] + x1[i] * b[1];
    y_hat[i] = m[i] + x2[i] * b[2];
  }
}
 
model {
  sigma_a1 ~ uniform(0, 100);
  mu_a1 ~ normal(0, 1);
  a1 ~ normal (mu_a1, sigma_a1);
  sigma_a2 ~ uniform(0, 100);
  mu_a2 ~ normal(0, 1);
  a2 ~ normal (mu_a2, sigma_a2);
  b ~ normal (0, 1);
  sigma_y ~ uniform(0, 100);
  y ~ normal(y_hat, sigma_y);
}
"""

varying_intercept_model1_data = {'N': len(church2),
                                 'J1': countsno,
                                 'J2': len(years),
                                 'countries': countries + 1,
                                 'years': years + 1,
                                 'x1': gini_net,
                                 'x2': rgdpl,
                                 'y': church2
                                 }

varying_intercept_model1_fit = pystan.stan(model_code=varying_intercept_model1, data=varying_intercept_model1_data, iter=1000, chains=2)


#Second Model, varying country-year intercepts with informative prior
varying_intercept_model2 = """

data {
  int<lower=0> J1;
  int<lower=0> J2;
  int<lower=0> N;
  int<lower=1,upper=J1> countries[N];
  int<lower=1,upper=J2> years[N];
  vector[N] x1;
  vector[N] x2;
  vector[N] y;
} 

parameters {
  vector[J1] a1;
  vector[J2] a2;
  vector[2] b;
  real mu_a1;
  real mu_a2;
  real<lower=0,upper=100> sigma_a1;
  real<lower=0,upper=100> sigma_a2;
  real<lower=0,upper=100> sigma_y;
  real alpha;
} 

transformed parameters {
  vector[N] y_hat;
  vector[N] m;
  for (i in 1:N) {
    m[i] = alpha + a1[countries[i]] + a2[years[i]] + x1[i] * b[1];
    y_hat[i] = m[i] + x2[i] * b[2];
  }
}

 
model {
  sigma_a1 ~ uniform(0, 100);
  mu_a1 ~ normal(0, 1);
  a1 ~ normal (mu_a1, sigma_a1);
  sigma_a2 ~ uniform(0, 100);
  mu_a2 ~ normal(0, 1);
  b[1] ~ normal (0, 100);
  b[2] ~ normal (0, 1);
  sigma_y ~ uniform(0, 100);
  y ~ normal(y_hat, sigma_y);
}

"""

varying_intercept_model2_data = {'N': len(church2),
                                 'J1': countsno,
                                 'J2': len(years),
                                 'countries': countries + 1,
                                 'years': years + 1,
                                 'x1': gini_net,
                                 'x2': rgdpl,
                                 'y': church2
                                 }

varying_intercept_model2_fit = pystan.stan(model_code=varying_intercept_model2, data=varying_intercept_model2_data, iter=1000, chains=2)

