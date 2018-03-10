Fancy Model #4
==============

## Model

Check to see if the type of competition is useful in predicting.

Data Likelihood
* `points_{elt type/comp, skater}` ~ N(mu_skater, sigma_{type})
    * Note components are grouped, so we don't estimate for each type

Parameter Models (Grouped)
* `mu_{elt/comp, skater}` ~ 
     N(a + b x weeks since IJS + c_skater x weeks since skater started +
       d_gpf * is_gpf + d_ecfc * is_ecfc + d_wc * is_wc + d_owg * is_owg,
       sigma)
* `sigma_{elt/comp type}` ~ HalfCauchy(5)   [noninformative]

Priors
* any `sigma` ~ HalfCauchy(5)   [noninformative]
* `mu_a_ch` ~ N(2.0, 0.5)
* `mu_a_st` ~ N(3.0, 0.5)
* `mu_a_sp` ~ N(2.5, 0.5)
* `mu_a_1j` ~ N(0.67, 0.01)
* `mu_a_2j` ~ N(4.0, 0.5)
* `mu_a_3j` ~ N(6.0, 0.7)
* `mu_a_4j` ~ N(10.5, 1.0)
* `mu_a_comp` ~ 10 * Beta(20, 6)
* `mu_b` ~ N(0, 1e5)
* any `mu_c` ~ N(0, 1e5)
* any `mu_competitiontype` ~ N(0, 1e5)

## Results

| Model      | Rank | Score   |
|------------|------|---------|
| Model 4    | 308  | 138112  |
