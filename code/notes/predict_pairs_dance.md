Prediction for Pairs and Dance
==============================

## Results

Ladies

| Model   | Rank Loss | Score Loss |
|---------|-----------|------------|
| OLS     | 336       | 58255      |
| Model 1 | 436       | 91204      |
| Model 2 | 432       | 60781      |
| Model 3 | 408       | 82094      |


Pairs

| Model   | Rank Loss | Score Loss |
|---------|-----------|------------|
| OLS     | 58        | 9898       |
| Model 1 | 82        | 34737      |
| Model 2 | 72        | 15945      |
| Model 3 | 78        | 16349      |

Dance

| Model   | Rank Loss | Score Loss |
|---------|-----------|------------|
| OLS     | 134       | 10611      |
| Model 1 | 170       | 46161      |
| Model 2 | 184       | 22540      |
| Model 3 | 170       | 20180      |


## Element Categories
Pairs
```
('st', 'sp', 'tw', 'th', 'li', 'ds', 'ch', 'ju')
```
* `st`: step sequence or spiral sequence
* `sp`: either pair spin or sbs spin
* `tw`: twist
* `th`: throw
* `li`: lift
* `ds`: death spiral
* `ch`: choreo sequence
* `ju`: sbs jump

Dance
```
('tw', 'st', 'pd', 'li', 'l2', 'sp', 'ch')
```
* `tw`: synchronized twizzles
* `st`: step sequence (any: pattern step, diagonal step, circular, etc.)
* `pd`: dance pattern (e.g. Rhumba pattern, Golden Waltz pattern)
* `li`: lift
* `l2`: combined two lifts (e.g. SlLi4+RoLi4, wc2017 17. Alisa AGAFONOVA
  / Alper UCAR); base value looks like just the sum.
* `sp`: dance spin
* `ch`: choreographic sequence (sequence, lift, twizzles)

Note with dance we ignore all data up through the 2009-2010 season because of
the annoying program change. Lots of elements changed so it's not worth
modeling. Same for components because short dance had fewer components which
included Timing.

## Model 1
Analogue of [Model 1: partial pooling](elt_comp_model_1.md).

### Group Distribution Priors
Pairs
* `mu_st` ~ N(3.0, 1e5)
* `mu_sp` ~ N(3.5, 1e5)
* `mu_tw` ~ N(5.0, 1e5)
* `mu_th` ~ N(4.0, 1e5)
* `mu_li` ~ N(6.0, 1e5)
* `mu_ds` ~ N(4.0, 1e5)
* `mu_ch` ~ N(2.0, 1e5)
* `mu_ju` ~ N(3.0, 1e5)

Dance
* `mu_tw` ~ N(6.0, 1e5)
* `mu_st` ~ N(7.0, 1e5)
* `mu_pd` ~ N(4.0, 1e5)
* `mu_li` ~ N(4.0, 1e5)
* `mu_l2` ~ N(8.0, 1e5)
* `mu_sp` ~ N(4.0, 1e5)
* `mu_ch` ~ N(2.0, 1e5)

## Model 2
Analogue of [Model 2.5](elt_comp_model_2.5.md)

### Group Distribution Priors

Pairs
* `mu_st` ~ N(3.0, 0.5)
* `mu_sp` ~ N(3.5, 0.5)
* `mu_tw` ~ N(5.0, 1.0)
* `mu_th` ~ N(4.0, 1.0)
* `mu_li` ~ N(6.0, 0.7)
* `mu_ds` ~ N(4.0, 0.5)
* `mu_ch` ~ N(2.0, 0.5)
* `mu_ju` ~ N(3.0, 1.0))

Dance
* `mu_tw` ~ N(6.0, 1.0)
* `mu_st` ~ N(7.0, 1.0)
* `mu_pd` ~ N(4.0, 0.5)
* `mu_li` ~ N(4.0, 0.5)
* `mu_l2` ~ N(8.0, 0.5)
* `mu_sp` ~ N(4.0, 0.5)
* `mu_ch` ~ N(2.0, 0.5)

## Model 3
Analogue of [Model 3.7](elt_comp_model_3.md).

Same priors as Model 2, but with the components breakdwon of Model 3.7.