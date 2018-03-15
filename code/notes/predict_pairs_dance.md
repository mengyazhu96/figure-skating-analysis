Prediction for Pairs and Dance
==============================

## Results

Pairs

| Model   | Rank Loss | Score Loss |
|---------|-----------|------------|
| OLS     | 58        | 9898       |
| Model 1 | 82        | 34737      |
| Model 2 | | |
| Model 3 | | |

Dance

| Model   | Rank Loss | Score Loss |
|---------|-----------|------------|
| Model 1 | | |
| Model 2 | | |
| Model 3 | | |


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
