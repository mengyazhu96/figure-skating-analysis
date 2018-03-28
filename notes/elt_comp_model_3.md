Fancy Model #3
==============

## Model

Data Likelihood
* `points_{elt type/comp, skater}` ~ N(mu_skater, sigma_{type})
    * Note components are grouped, so we don't estimate for each type

Parameter Models (Grouped)
* `mu_{elt/comp, skater}` ~ 
     N(a + b x weeks since IJS + c_skater x weeks since skater started, sigma)
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
* any `mu_b` ~ N(0, 1e5)
* any `mu_c` ~ N(0, 1e5)

### Subparts
* Model 3.5: replace components prediction with that of model 2.5 (highest
  historical component score, per-category)
* Model 3.6: replace components prediction with that of model 2
* Model 3.7: use log of week measures
* Model 3.8: use log of week measures, don't index c per skater (only group
  model)

## Results

| Model      | Rank | Score   |
|------------|------|---------|
| Model 3    | 306  | 52140   |
| Model 3.5  | 322  | 44896   |
| Model 3.6  | 326  | 40925   |
| Model 3.7  | 308  | 43757   |
| Model 3.8  | 322  | 72915   |

* I'm dumb

