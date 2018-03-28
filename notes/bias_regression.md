Evaluating Bias Based on Regressions
====================================

https://github.com/statsmodels/statsmodels/issues/2728

http://www.statsmodels.org/dev/examples/notebooks/generated/regression_diagnostics.html

https://www.r-bloggers.com/genetic-data-large-matrices-and-glmnet/

https://stats.stackexchange.com/questions/122678/linear-regression-including-categorical-variables-with-hundreds-of-levels

https://stats.stackexchange.com/questions/227125/preprocess-categorical-variables-with-many-values

https://stackoverflow.com/questions/3169371/large-scale-regression-in-r-with-a-sparse-feature-matrix

https://www.r-project.org/conferences/useR-2010/abstracts/Maechler+Bates.pdf

https://stats.stackexchange.com/questions/146907/principled-way-of-collapsing-categorical-variables-with-many-categories

## Notes from Trying to Apply Emerson 2000 to Ladies OWG
* It's difficult because unobserved quality is inherently a function of skater
  which is highly correlated with country. When we straight up apply Emerson's
  model, the three Russian girls have their quality coefficients absorbed into
  the interaction terms.
* There's no good way to get rid of collinearity. A cleaner way to code
  Emerson's model is to use the auto-treatment of interaction terms:
```
judge_score ~ C(skater, Treatment) * C(segment_name, Treatment) +
              C(judge, Treatment) * C(country, Treatment)
```
  This way the supposed tendency of all judges to scores Russian skaters higher
  will be absorbed into the RUS coefficient rather than just present in all of
  the judge:country terms.
* Even with this fix, there's collinearity. The skater indicator will be highly
  correlated with (1) the country indicator and (2) the interactions that
  contains her country.
* If we want to determine a starting order bias, this is also hard because it's
  highly correlated with the skater.


## Questions to Ask Glickman
* Explain model
  * score_ij = lam_i + mu_j + beta_j,C(i) + eps_ji
  * \sum mu_j = 0
  * \sum_j beta_j,c = 0
  * \sum_c beta_j,c = 0
* General collinearity issues with predictors
  * lam_i will be correlated with beta_j, C(i)
* Is collinearity okay if I know how to combine the coefficients in a
  meaningful way?

Helpful things!
* ridge regression to overcome collinearity of skater + judge * country terms
* use just skater terms
* mixed linear effects model: s_ijk = lam_i + d_ik + beta_j,C(i)
  * i = skater
  * k = skater i's kth performance
  * d_ik ~ N(0, tau^2) and estimate tau
  * http://www.statsmodels.org/dev/mixed_linear.html ?

## Simple Same Country

### Reported Outliers

| Index | Skater | Outlier Score | All Scores | Skater Country | Judge | Judge Country | Segment |
|-------|--------|---------------|------------|----------------|-------|---------------|---------|
| 181276 | Alexander MAJOROV | 3.50 | 6.75,6.75,6.25,3.5,6.25,6.0,7.0,6.25,6.5 | SWE | Philippe MERIGUET | FRA | gprus2016_men_free |
| 181294 | Alexander MAJOROV | 4.25 | 7.0,7.25,6.5,4.25,6.25,6.25,7.25,6.75,6.75 | SWE | Philippe MERIGUET | FRA | gprus2016_men_free |
| 181303 | Alexander MAJOROV | 4.25 | 6.75,7.0,6.5,4.25,5.75,5.5,6.0,6.5,6.5 | SWE | Philippe MERIGUET | FRA | gprus2016_men_free |
| 231991 | Dabin CHOI        | 4.00 | 6.0,6.0,6.75,4.0,6.5,6.0,6.75,6.75,6.25 | KOR | Akos PETHES | HUN | gpchn2017_ladies_free |
| 180961 | Keiji TANAKA      | 5.00 | 7.25,7.25,7.25,5.0,6.75,6.75,7.0,6.5,7.25 | JPN | Philippe MERIGUET | FRA | gprus2016_men_free |
| 217739 | Anna POGORILAYA   | 5.75 | 7.0,7.25,7.5,7.5,7.5,7.5,7.75,5.75,6.5 | RUS | Mona ADOLFSEN | NOR | wc2017_ladies_free |
| 228309 | Anna POGORILAYA   | 5.75 | 6.75,6.0,5.75,5.75,5.75,6.25,6.25,6.75,7.25 | RUS | Roger GLENN | USA | gpcan2017_ladies_free |
| 228310 | Anna POGORILAYA   | 5.75 | 6.75,6.0,5.75,5.75,5.75,6.25,6.25,6.75,7.25 | RUS | Massimo ORLANDINI | ITA | gpcan2017_ladies_free |
| 228311 | Anna POGORILAYA   | 5.75 | 6.75,6.0,5.75,5.75,5.75,6.25,6.25,6.75,7.25 | RUS | Francoise DE RAPPARD | BEL | gpcan2017_ladies_free |
| 233410 | Lorraine MCNAMARA / Quinn CARPENTER | 4.50 | 4.5,8.25,7.75,7.5,7.75,7.5,8.5,7.25,7.25 | USA | Mark STORTON | AUS | gpchn2017_ice_dance_free |