Fancy Model #2
==============

## Model

Data Likelihood
* `points_{elt/comp type, skater}` ~ N(mu_skater, sigma_{type})
* Note Exponential response for `1j` results in a misspecified model error.

Parameter Models (Grouped)
* `mu_{elt/comp type, skater}` ~ N(mu, sigma)
    * but comp type is trained only with last two years ('15-'16 and '16-'17)
* `sigma_{elt/comp type}` ~ HalfCauchy(5)   [noninformative]

Priors
* any `sigma` ~ HalfCauchy(5)   [noninformative]
* `mu_ch` ~ N(2.0, 0.5)
* `mu_st` ~ N(3.0, 0.5)
* `mu_sp` ~ N(2.5, 0.5)
* `mu_1j` ~ N(0.67, 0.01)
* `mu_2j` ~ N(4.0, 0.5)
* `mu_3j` ~ N(6.0, 0.7)
* `mu_4j` ~ N(10.5, 1.0)
* `mu_comp` ~ 10 * Beta(20, 6)


## Results
* Score Difference: 57356
    * Better than fancy model #1, worse than OLS
* Rank Difference: 316
    * Worse than fancy model #1 and OLS
* Components are much better, but still underpredict 981/1320 times
* Performs terribly on skaters we haven't seen before (Dmitri Aliev, Vincent Zhou)