#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: eers
"""

import pystan

varying_intercept = """
data {
  int<lower=0> J; 
  int<lower=0> N; 
  int<lower=1,upper=J> country[N];
  vector[N] x;
  vector[N] y;
} 
parameters {
  vector[J] a;
  real b;
  real mu_a;
  real<lower=0,upper=100> sigma_a;
  real<lower=0,upper=100> sigma_y;
} 

transformed parameters {
  vector[N] y_hat;
  for (i in 1:N)
    y_hat[i] = a[country[i]] + x[i] * b;
}
model {
  sigma_a ~ uniform(0, 100);
  a ~ normal (mu_a, sigma_a);
  b ~ normal (0, 1);
  sigma_y ~ uniform(0, 100);
  y ~ normal(y_hat, sigma_y);
}
"""

varying_intercept_data = {'N': len(AP),
                          'J': countsno,
                          'country': countries + 1,
                          'x': IP,
                          'y': AP}

varying_intercept_fit = pystan.stan(model_code=varying_intercept, data=varying_intercept_data, iter=1000, chains=2, control=(dict(adapt_delta=0.99)))

"""WARNING:pystan:DeprecationWarning: pystan.stan was deprecated in version 2.17 and will be removed in version 3.0. Compile and use a Stan program in separate steps.
INFO:pystan:COMPILING THE C++ CODE FOR MODEL anon_model_f99bc7fa32e3642983a8134dfd5ce1d1 NOW.
WARNING:pystan:Rhat above 1.1 or below 0.9 indicates that the chains very likely have not mixed
WARNING:pystan:6 of 1000 iterations ended with a divergence (0.6 %).
WARNING:pystan:Try running with adapt_delta larger than 0.99 to remove the divergences.
WARNING:pystan:Chain 1: E-BFMI = 0.0358
WARNING:pystan:Chain 2: E-BFMI = 0.153
WARNING:pystan:E-BFMI below 0.2 indicates you may need to reparameterize your model