Running Results Summary
=======================

## Results
Models are trained on all data until the 2016-2017 season (unless otherwise
specified) and tested on the 2017-2018 season (up to and including Four
Continents, but not Olympics yet).

### Men

| Model               | Score Loss | Rank Loss |
| --------------------|------------|-----------|
| Linear Regression   | 50238      | 308       |
| Model 1 (Partial)   | 91053      | 302       |
| Model 1 (Pooled)    | 204946     | 376       |
| Model 1 (Unpooled)  | 140457657  | 380       |
| Model 2             | 57356      | 316       |
| Model 2.5           | 44331      | 330       |
| Model 3             | 103961     | 304       |
| Model 3.5           | 84719      | 318       |
| Model 3.6           | 113863     | 312       |
| Model 3.7           | 125219     | 302       |
| Model 3.8           | 181680     | 318       |
| Model 4             | 138112     | 308       |

### Ladies

| Model               | Score Loss | Rank Loss |
| --------------------|------------|-----------|
| Linear Regression   | 58255      | 336       |
| Model 2             | 80983      | 428       |
| Model 2.5           | 60781      | 432       |


## Error Metrics
* Score: least squares distance from actual total score of each skater
* Rank: sum of absolute distance from true rank per competition

## Models
### [Linear Regression](basic_prediction.md)
For each program, model the segment score using the skater's highest historical
score in that segment and the normalized start order within the segment
(between 0 and 1):
```
segment_score = b0 + b1 * segment_reputation + b2 * start_order + normal noise
```

#### Fitted Coefficients

| Discipline | Program | b0      | b1      | b2      |
|------------|---------|---------|---------|---------|
| Men        | short   | 20.8236 | 0.6155  | 12.3222 |
|            | free    | 72.3915 | 0.3983  | 35.2871 |
| Ladies     | short   | 21.8275 | 0.5289  | 10.5243 |
|            | free    | 71.8259 | 0.1939  | 35.1033 |
| Pairs      | short   | 26.6549 | 0.5133  | 10.4161 |
|            | free    | 57.2884 | 0.3892  | 28.9112 |

### [Model 1](elt_comp_model_1.md)
Models fits points distribution on each kind of element and component.
* The _pooled_ model fits a single distribution per element or component
  type, thus "pooling" skaters and not considering variation between skaters.
* The _unpooled_ model fits element and component distributions for each
  skater, but does not consider consistency across skaters (no group
  distribution).
* The _partial pooling_ model uses the parameter priors as priors on a _group_
  distribution for each element and component type. Then each skater's
  element/component distribution is considered to be a draw from this group
  distribution.

### [Model 2](elt_comp_model_2.md)
Similar to the partial pooling model of Model 1, but with the following
differences:
* Priors are tweaked slightly. The prior on component means is 10 times a Beta
  distribution, because components scores do have actual bounds.
* Components distributions are trained only on the last two years of data
  (2015-2016 and 2016-2017) instead of the entire dataset. This is because
  component scores in general have gotten higher, and a skater's components
  in the past year is more telling than anything before that for prediction
  purposes.

### [Model 2.5](elt_comp_model_2.5.md)
The same as Model 2 except that components are predicted as the highest
historical model for that skater instead of estimating any randomness.

### [Model 3](elt_comp_model_3.md)
Adds predictors to the model scheme. The mean for a skater's element or
component type is:
```
mu_{elt/comp type, skater} ~ 
    N(a_skater + b * weeks_since_IJS + c_skater * weeks_since_skater_start, sigma^2)
```
where `weeks_since_IJS` is the number of elapsed weeks since the first
datapoint (2005-10-23) and `weeks_since_skater_start` is the number of elapsed
weeks since the first time the skater appeared in the dataset. This model also
_does not split components into types_, and fits only one component
distribution per skater.

Note this model takes much longer to fit than any of the others, but the goal
is to take into account (1) score inflation generally over time and (2) skater
improvement over time.

Small variants to this model include:
* Model 3.5: replace components prediction with that of Model 2.5 (highest historical
  component score, per-category).
* Model 3.6: replace components prediction with that of Model 2 (train
  separate component types distributions on the last two years of data).
* Model 3.7: use log of week measures
* Model 3.8: use log of week measures, don't index c per skater (only group
  model)

### [Model 4](elt_comp_model_4.md)
Uses model 3.7, adds linear predictors for type of competition:
* regular Grand Prix (refeference)
* GPF
* EC or FC
* WC
* OWG

