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
* General collinearity issues with predictors
* Is collinearity okay if I know how to combine the intercepts in a meaningful
  way?