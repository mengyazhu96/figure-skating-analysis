Non-Parametric Test of Judging Bias
===================================

Campbell and Galbraith give a nonparametric test of judging bias for the 6.0
system which can be easily applied to IJS when you consider the GOEs and
component marks of each judge for each skater. It's like having 12-20 data
points per judge per skater instead of having 2-4.

For any element or component mark for a particular skater (the ith
obsevation), let m_i be the median of the judges' scores. Let the mark of a
single judge j on this observation be m_ij. Let n_ij be 1 if the skater and
judge nationalities match on observation i and -1 otherwise. Then
I((m_ij - m_i) * n_ij | m_j != m) is a random fair trial under the null
hypothesis that the judge's nationality and whether that judge scores above
the median mark (scores similarly to other judges) are independent.

If we sum this up across all datapoints:
```
S = sum_i sum_j I((m_ij - m_i) * n_ij | m_j != m)
```
under the null hypothesis S ~ Binomial(N, 0.5) where N is the number of m_ij
where m_ij != m_i.


## Data

All element + component marks from 2016-2017 and 2017-2018 season (up to and
including FCC 2018). We initially have 247278 data points, but 138831 of these
represent judges scoring exactly the same as the median.

## Results

Split up into potentially relevant mini-datasets. "top-6" takes only data
points where the segment rank is 6 or higher.

| Data Slice       | top 6 | p-value         | S     | N      | p_hat (S/N) |
|------------------|-------|-----------------|-------|--------|-------------|
| all              |       | 1.11 x 10^(-16) | 61106 | 108447 | 0.563       |
| all              | x     | ""              | 29363 | 50291  | 0.584       |
| short elements   |       | ""              | 11069 | 19841  | 0.558       |
| short elements   | x     | ""              | 1321  | 1672   | 0.790       |
| short components |       | ""              | 17744 | 31391  | 0.565       |
| short components | x     | ""              | 2367  | 2772   | 0.854       |
| free elements    |       | ""              | 17140 | 30704  | 0.558       |
| free elements    | x     | ""              | 2151  | 2763   | 0.779       |
| free components  |       | ""              | 15153 | 26511  | 0.572       |
| free components  | x     | ""              | 2147  | 2532   | 0.848       |
| men              |       | ""              | 2206  | 2793   | 0.790       |
| men              | x     | ""              | 1100  | 1344   | 0.818       |
| ladies           |       | ""              | 2043  | 2544   | 0.803       |
| ladies           | x     | ""              | 1066  | 1294   | 0.824       |
| pairs            |       | ""              | 1685  | 2111   | 0.798       |
| pairs            | x     | ""              | 1241  | 1478   | 0.840       |
| dance            |       | ""              | 2052  | 2291   | 0.896       |
| dance            | x     | ""              | 1110  | 1194   | 0.930       |