Fancy Model #2.5
================

## Model

Data Likelihood
* `points_{elt type, skater}` ~ N(mu_skater, sigma_{type})
* Predict `points_{comp type, skater}` as the highest historical mark for that
  skater.

Parameter Models (Grouped)
* `mu_{elt type, skater}` ~ N(mu, sigma)
* `sigma_{elt type}` ~ HalfCauchy(5)   [noninformative]

Priors
* any `sigma` ~ HalfCauchy(5)   [noninformative]
* `mu_ch` ~ N(2.0, 0.5)
* `mu_st` ~ N(3.0, 0.5)
* `mu_sp` ~ N(2.5, 0.5)
* `mu_1j` ~ N(0.67, 0.01)
* `mu_2j` ~ N(4.0, 0.5)
* `mu_3j` ~ N(6.0, 0.7)
* `mu_4j` ~ N(10.5, 1.0)

## Results

* Rank Difference: 330
    * worse than OLS + fancy model
* Score Difference: 44331
    * best yet