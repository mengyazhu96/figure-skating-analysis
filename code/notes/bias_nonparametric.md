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

Independence assumptions? So this is saying all judges' marks for all skaters
are i.i.d. But I think maybe we should have to split it up into tech/components
at least? And what if there are other factors that influence the probability
(e.g. Olympic excitement, skate order)? But then I suppose those factors would
influence the judges uniformly (or we would assume that).

Marks within a single skater's program being i.i.d. makes sense (except maybe
splitting up element types/components/etc. if judges have "nationalistic
preferences" for particular kinds of elements.)

Marks between skaters being i.i.d.... "the incident of a judge scoring above
the median mark is independent of a judge sharing a skater's nationality." So
yes these would be i.i.d. because skater performances are independent.

A judge scores mostly skaters that don't match his/her nationality. So if a
judge on average scores everyone lower than the median, then this metric will
be off.

Ooh maybe for components I should sum the five marks and take the median of
that!


## Data

All element + component marks from 2016-2017 and 2017-2018 season (up to and
including FCC 2018). We initially have 247278 data points, but 138831 of these
represent judges scoring exactly the same as the median.

## Results

Split up into potentially relevant mini-datasets. "top-6" takes only data
points where the segment rank is 6 or higher. "p_hat" is S/N.

| Data Slice       | top 6 | p-value         | S     | N      | p_hat |
|------------------|-------|-----------------|-------|--------|-------|
| all              |       | 1.11 x 10^(-16) | 61106 | 108447 | 0.563 |
| all              | x     | ""              | 29363 | 50291  | 0.584 |
| short elements   |       | ""              | 11069 | 19841  | 0.558 |
| short elements   | x     | ""              | 1321  | 1672   | 0.790 |
| short components |       | ""              | 17744 | 31391  | 0.565 |
| short components | x     | ""              | 2367  | 2772   | 0.854 |
| free elements    |       | ""              | 17140 | 30704  | 0.558 |
| free elements    | x     | ""              | 2151  | 2763   | 0.779 |
| free components  |       | ""              | 15153 | 26511  | 0.572 |
| free components  | x     | ""              | 2147  | 2532   | 0.848 |
| men              |       | ""              | 17958 | 32992  | 0.544 |
| men              | x     | ""              | 7489  | 13323  | 0.562 |
| ladies           |       | ""              | 17497 | 31510  | 0.555 |
| ladies           | x     | ""              | 7472  | 13071  | 0.572 |
| pairs            |       | ""              | 11794 | 20807  | 0.567 |
| pairs            | x     | ""              | 7729  | 13200  | 0.586 |
| dance            |       | ""              | 13857 | 23138  | 0.599 |
| dance            | x     | ""              | 6673  | 10697  | 0.624 |

Pulling only the datapoints where skater-judge match:

| Data Slice       | top 6 | p-value         | S     | N      | p_hat |
|------------------|-------|-----------------|-------|--------|-------|
| men              |       | ""              | 2206  | 2793   | 0.790 |
| men              | x     | ""              | 1100  | 1344   | 0.818 |
| ladies           |       | ""              | 2043  | 2544   | 0.803 |
| ladies           | x     | ""              | 1066  | 1294   | 0.824 |
| pairs            |       | ""              | 1685  | 2111   | 0.798 |
| pairs            | x     | ""              | 1241  | 1478   | 0.840 |
| dance            |       | ""              | 2052  | 2291   | 0.896 |
| dance            | x     | ""              | 1110  | 1194   | 0.930 |

### Olympics
Reported: p-value, p_hat, S, N

p-value threshold: 0.05/100 = 5 x 10^(-4)

men 1.61546491739e-08 0.550 1645 2989
* top6 1.30417898703e-12 0.632 437 692
* **bottom 0.133253895541 0.520 379 729**
* **elt 0.00059304840887 0.542 806 1488**
* comp 2.11687584728e-06 0.559 839 1501
* **short 0.170347335209 0.512 772 1508**
    * top6 7.21421617278e-06 0.623 188 302
    * **bottom 0.570904711993 0.495 248 501**
    * **elt 0.531625746865 0.498 316 635**
        * **top6 0.000833756942951 0.629 88 140**
        * **bottom 0.444476172415 0.502 103 205**
    * **comp 0.0878837578065 0.522 456 873**
        * **top6 0.00104326174383 0.617 100 162**
        * **bottom 0.614299872637 0.490 145 296**
* free 2.09809947194e-12 0.589 873 1481
    * top6 1.38647370251e-08 0.638 249 390
    * **bottom 0.0101254897756 0.575 131 228**
    * elt 5.65461029534e-06 0.574 490 853
        * top6 4.00561918568e-06 0.640 155 242
        * **bottom 0.0506838267665 0.570 69 121**
    * comp 1.28095489771e-08 0.610 383 628
    * top6 0.000348957193755 0.635 94 148
    * **bottom 0.040676524103 0.579 62 107**

ladies 2.51032528098e-12 0.565 1583 2802
* top6 1.81696004531e-06 0.592 367 620
* **bottom 0.119976291301 0.522 363 696**
* elt 4.16261174319e-06 0.562 717 1276
* comp 5.57592889638e-08 0.567 866 1526
* short 3.86264686902e-10 0.581 830 1429
    * top6 2.59297999738e-08 0.662 180 272
    * **bottom 0.0186998205032 0.546 267 489**
    * elt 5.7159561172e-06 0.592 328 554
        * top6 2.63366546853e-05 0.678 82 121
        * **bottom 0.034668512065 0.566 99 175**
    * comp 5.3498038205e-06 0.574 502 875
        * top6 8.12145801965e-05 0.649 98 151
        * **bottom 0.0971092970329 0.535 168 314**
* **free 0.000147870438808 0.548 753 1373**
    * **top6 0.0738461438102 0.537 187 348**
    * **bottom 0.834734266634 0.464 96 207**
    * **elt 0.0169113580446 0.539 389 722**
       * **top6 0.164090979802 0.532 109 205**
       * **bottom 0.955686959943 0.410 41 100**
     * **comp 0.00110541570691 0.559 364 651**
       * **top6 0.120802097623 0.545 78 143**
       * **bottom 0.349587492004 0.514 55 107**

pairs 2.74655520549e-10 0.566 1224 2161
* top6 3.59617216116e-05 0.578 368 637
* **bottom 0.0674041642552 0.531 291 548**
* elt 1.33099184846e-05 0.564 593 1051
* comp 2.11986173815e-06 0.568 631 1110
* short 4.37171698842e-09 0.585 655 1119
     * top6 5.31110565088e-05 0.615 169 275
     * **bottom 0.0567354528089 0.538 220 409**
     * elt 2.42818982354e-06 0.605 280 463
          * top6 9.91184992772e-05 0.670 75 112
          * **bottom 0.592015860196 0.488 81 166**
     * comp 0.00010152800163 0.572 375 656
          * **top6 0.0206862114997 0.577 94 163**
          * **bottom 0.0103652315172 0.572 139 243**
* **free 0.00131967635603 0.546 569 1042**
     * **top6 0.0258318366785 0.550 199 362**
     * **bottom 0.367269658636 0.511 71 139**
     * **elt 0.0538415562397 0.532 313 588**
          * **top6 0.162904428138 0.532 108 203**
          * **bottom 0.587843392447 0.481 39 81**
     * **comp 0.00278209278595 0.564 256 454**
          * **top6 0.0283279984169 0.572 91 159**
          * **bottom 0.179071650903 0.552 32 58**

dance 1.11022302463e-16 0.607 1291 2126
* top6 4.24993373827e-13 0.661 316 478
* bottom 8.3226609231e-06 0.586 357 609
* elt 1.32893696048e-13 0.617 590 956
* comp 4.12414546958e-12 0.599 701 1170
* short 2.31841235099e-09 0.591 605 1024
     * top6 3.78721062955e-06 0.650 139 214
     * bottom 0.000123981395064 0.594 218 367
     * elt 1.21428425526e-06 0.622 224 360
          * top6 0.000220142503257 0.700 49 70
          * bottom 0.000377945136228 0.643 83 129
     * comp 5.93892048371e-05 0.574 381 664
          * top6 0.00097126598504 0.625 90 144
          * **bottom 0.0161061492563 0.567 135 238**
* free 1.11022302463e-16 0.623 686 1102
     * top6 7.71093622287e-09 0.670 177 264
     * **bottom 0.00860257459905 0.574 139 242**
     * elt 8.6955720402e-09 0.614 366 596
          * top6 1.47895236002e-06 0.690 98 142
          * **bottom 0.215010441988 0.531 69 130**
     * comp 7.84951104116e-10 0.632 320 506
          * top6 0.000370397613706 0.648 79 122
          * **bottom 0.00294508649021 0.625 70 112**