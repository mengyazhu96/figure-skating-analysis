Fancy Model #1
==============

## Model
```
for each skater s:
    for each elt group e:
        points_{s, e} ~ Normal(mu, sigma)
        # learn mu, sigma
```
elt groups
* `ch`: choreo sequences ChSq or ChSt
* `st`: step sequences contain 'St' and are not 'ChSt'
* `sp`: spins contain 'Sp'
* `1j`: single jumps (also zero-rev jumps like 'A' 'F')
* `2j`: double jumps
* `3j`: triple jumps
* `4j`: quad jumps
* `ss`: skating skills
* `tr`: transitions
* `pe`: performance
* `co`: composition/choreo
* `in`: interpretation

note all jump groups include combos where the first jump is the group type

Priors
* `points_{ch}` ~ N(2.0, 0.7)      [base value is 2.0]
* `points_{st}` ~ N(3.0, 1.0)      [base values from 1.8 to 3.4]
* `points_{sp}` ~ N(2.5, 0.6)
* `points_{1j}` ~ Expo(1.5)        [a lot of 0's]
* `points_{2j}` ~ N(4.0, 1.5)      [also some combos worth lots of points]
* `points_{3j}` ~ N(6.0, 1.5)
* `points_{4j}` ~ N(10.5, 2)
* `points_{s, comp_type}` ~ N(7.0, 0.3)

how to fit
* treat them all as independent distributions, with no predictors
* fit each group of elements independently pooled and then unpooled (skaters as groups)


## fits/ FILES
See [PyMC3](http://docs.pymc.io/notebooks/multilevel_modeling.html) for inspiration.
* `men_sorted.pickle`: list of skater names, sorted for consistency
* `men_nonmulti_elts.pickle`: fitted pooled/unpooled traces
  * `(traces, models, skater_shared)`
  * traces: `d[<elt_type>][<un>pooled_trace]`
  * models: `d[<elt_type>][<un>pooled]`
  * skater_shared: `d[<elt_type>]`
  ```
  unpooled_estimates = pd.Series(unpooled_trace['mu_' + elt_type].mean(axis=0), index=skaters)
  unpooled_se = pd.Series(unpooled_trace['mu_' + elt_type].std(axis=0), index=skaters)
  sorted(zip(skaters, unpooled_trace['mu_st'].mean(axis=0)), key=lambda x: x[1])
  ```
  * `points_{s, type}` ~ N(mu, sigma)
    * `sigma` ~ HalfCauchy(5)
    * mus: `('sp', 2.5), ('ch', 1.), ('st', 3.), ('1j', 1.5), ('2j', 4.), ('3j', 6.), ('4j', 10.5)`
    * `points_{s, 1j}` ~ Expo(1.5)
* `men_nonmulti_comps.pickle`
  * `(pooled_traces, pooled_models, unpooled_traces, unpooled_models, unpooled_skater_shared)`
  * same as above only no second indexing
  * prior: ~ N(7.0, 0.3)


## Implementation Files
[multi_elts_1.ipynb](../multi_elts_1.ipynb)
* fits the men's elements as above
* replaced unknown skaters with the skater group that had the median of that elt type
  (probably should do group distribution instead)

[multi_comp_1.ipynb](../multi_comp_1.ipynb)
* same idea as multi_elt_1

[compare_models.ipynb](../compare_models.ipynb)
* fit on all data up to 2017, predict on 2018 data
* compare with naive linear regression of reputation + normalized start order (per program)
  * see notes/basic_prediction.txt
  * `short = 20.8236 + 0.6155 * best_short + 12.3222 * normalized_short_start`
  * `long = 72.3915 + 0.3983 * best_free + 35.2871 * normalized_free_start`
* this model assumes we know what elements they execute, including popped jumps!!

## Results
Error Metrics
* Score: least squares distance from actual score
* Rank: sum of absolute distance from true rank

| Model      | Score     | Rank    |
| -----------|-----------|---------|
| OLS        | 50238     | 308     |
| Partial    | 91053     | 302     |
| Pooled     | 204946    | 376     |
| Unpooled   | 140457657 | 380     |

* thoughts
  * wow this is an improvement in at least rank prediction!
  * this model underpredicts, especially components
* next steps
  * adding predictors
  * weighting recent results more heavily
  * improving element grouping + assumptions
  * fixing components
  * can associate variance with skater too