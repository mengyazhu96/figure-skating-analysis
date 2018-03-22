Predicting Worlds 2018
======================

## Schedule
* men
  * short program: Thursday 3/22
  * free skate: Saturday 3/24
* ladies
  * short program: Wednesday 3/21
  * free skate: Friday 3/23
* pairs
  * short program: Wednesday 3/21
  * free skate: Thursday 3/22
* dance
  * short dance: Friday 3/23
  * free dance: Saturday 3/24

## Methods
At the World Championships, the top 24 ladies/men, top 16 pairs, and top 20
dance couples after the short program will qualify to the free skate. Thus we
will first predict short program scores, and then predict the free skate for
the skaters that qualify to the free skate.

* Personal Bests (PB): Predict each skater's personal best short program, and
  then if they qualify predict their personal best total score.
* Model 3: Assume a skater will repeat the same elements they last competed
  with. Fit Model 3 [(model 3.7 here)](elt_comp_model_3.md) on all of the data
  up to the 2018 Olympics.
* Reputation + start order OLS: We need the start orders for this model, so we
  will wait for the draws of start order and predict as the competition begins.

## Missing data
Ladies
* Alisa STOMAKHINA: does not appear in any previous event
* Elisabetta LECCARDI: does not appear in any previous event
* Stanislava KONSTANTINOVA: does not appear in any previous event
* Antonina DUBININA: has never qualified to the free skate

Antonina DUBININA does not qualify to the free skate in any of our predictive
scenarios, so we focus on the other three skaters, who all have junior results
that I Googled:
* Stanislava KONSTANTINOVA placed 4th at Junior Worlds 2018 and consistently
  scores around 65 for the short program, so we would expect her to qualify for
  the free skate. We predict 65 points for the short and 180 points overall
  (even though her actual personal best is just under 200).
* Elisabetta LECCARDI's personal best short program is around 53, but for
  simplicity we will assume she does not qualify for the free skate and predict
  her short program score to be 50.
* Alisa STOMAKHINA's personal best short program is around 41, so we predict
  her short program score to be 40.

Pairs
* Elizaveta KASHITSYNA / Mark MAGYAR: does not appear in any previous event

I couldn't find them anywhere, but I watched a YouTube video and would
expect them to score very low, so their short prediction is 45 points.

Dance
* Teodora MARKOVA / Simon DAZE: has never qualified to the free skate
* Adel TANKOVA / Ronald ZILBERBERG: has never qualified to the free skate
* Allison REED / Saulius AMBRULEVICIUS: does not appear in any previous event

MARKOVA/DAZE and TANKOVA/ZILDERBERG do not qualify to the free skate in our
predictions. REED/AMBRULEVICIUS beat TORN/PARTANEN at the 2017 Nebelhorn
Trophy, so we assign them a short prediction of 58 points which does not
qualify them for the free skate.


## Model 3
[predictions](worlds_predictions/model3.md)

## Predicting the PB Total Score
For missing data, do the same guesses as in Model 3.

[predictions](worlds_predictions/pb_total.md)

## OLS with Start Order
* [men](worlds_predictions/ols_men.md)
* [ladies](worlds_predictions/ols_ladies.md)
* [pairs](worlds_predictions/ols_pairs.md)
* [dance](worlds_predictions/ols_dance.md)


## My Tweaks on Model 3

Just for fun, and favoring my sentimental favorites :) Plus some mini
qualitative previews.

### Men
| Skater               | Score | Rank |
|----------------------|-------|------|
| Nathan CHEN          | 300+  | 1    |
| Shoma UNO            | 300+  | 2    |
| Boyang JIN           | 290   | 3    |
| Vincent ZHOU         | 280   | 4    |
| Mikhail KOLYADA      | 270   | 5    |
| Dmitri ALIEV         | 270   | 6    |
| Keiji TANAKA         | 250   | 7    |
| Max AARON            | 250   | 8    |
| Deniss VASILJEVS     | 240   | 9    |
| Michal BREZINA       | 240   | 10   |

The three men that have won the last seven world championships will not be at
worlds: Patrick Chan (2011-2013), Yuzuru Hanyu (2014 and 2017), and Javier
Fernandez (2015-2016). Thus we will by definition crown a new world champion.
Shoma UNO is fresh off the Olympic silver medal, but has been reporting some
foot pain in practice. Nathan CHEN had high hopes for gold at the Olympics, but
a devastating short program was only redeemed by the winning free skate at the
Olympics that still left him off the podium. He's looking for serious
redemption here. Boyang JIN is the two-time reigning world bronze medalist and
finished just off the podium at the Olympics; he tends to rise to the occasion
when others make mistakes. Vincent ZHOU had a breakthrough sixth-place finish
at the Olympics and has the technical goods but not the artirsty of the main
podium contenders. Mikhail KOLYADA was a podium contender this entire season,
but a disastrous showing at the Olympics has people questioning his mentality
coming in. Dmitri ALIEV had a personal best short program at the Olympics but
couldn't hold it together in the free skate; clean programs put him in the
conversation.


### Ladies
| Skater                   | Score  | Rank |
|--------------------------|--------|------|
| Alina ZAGITOVA           | 235    | 1    |
| Kaetlyn OSMOND           | 220    | 2    |
| Satoko MIYAHARA          | 220    | 3    |
| Carolina KOSTNER         | 210    | 4    |
| Maria SOTSKOVA           | 210    | 5    |
| Wakaba HIGUCHI           | 200    | 6    |
| Bradie TENNELL           | 200    | 7    |
| Mirai NAGASU             | 190    | 8    |
| Gabrielle DALEMAN        | 190    | 9    |

It doesn't look like anything is going to stop Alina ZAGITOVA, the newly
crowned 15 year-old Olympic champion. Her consistency and technical content
will make her hard to beat. Kaetlyn OSMOND just won the Olympic bronze and has
momentum on her side to continue her best season yet; she's likely the closest
contender for gold. Satoko MIYAHARA had two incredible programs at the Olympics
after a rough season, but finished just off the podium. Carolina KOSTNER is the
veteran likely in her last competition competing in her home country. That
makes her a sentimental favorite, but the technical content in her free skate
has not been there this season to make it happen. Maria SOTSKOVA is trying to
follow up a disappointing showing at the Olympics with the consistency that she
showed earlier in the season. Wakaba HIGUCHI is doing the same in trying to
make the most out of her Worlds spot after missing out on the Olympic spot to
Kaori Sakamoto. The American ladies are unlikely to place high enough to secure
three ladies spots for next year (the two best placements must sum to less than
13).

### Pairs
| Skater                                     | Score | Rank |
|--------------------------------------------|-------|------|
| Aljona SAVCHENKO / Bruno MASSOT            | 230   | 1    |
| Evgenia TARASOVA / Vladimir MOROZOV        | 215   | 2    |
| Xiaoyu YU / Hao ZHANG                      | 215   | 3    |
| Vanessa JAMES / Morgan CIPRES              | 215   | 4    |
| Valentina MARCHEI / Ondrej HOTAREK         | 215   | 5    |
| Natalia ZABIIAKO / Alexander ENBERT        | 205   | 6    |
| Julianne SEGUIN / Charlie BILODEAU         | 200   | 7    |
| Alexa SCIMECA KNIERIM / Chris KNIERIM      | 190   | 8    |
| Cheng PENG / Yang JIN                      | 190   | 9    |
| Kristina ASTAKHOVA / Alexei ROGONOV        | 190   | 10   |
| Kirsten MOORE-TOWERS / Michael MARINARO    | 190   | 11   |
| Nicole DELLA MONICA / Matteo GUARISE       | 185   | 12   |
| Tae Ok RYOM / Ju Sik KIM                   | 185   | 13   |
| Anna DUSKOVA / Martin BIDAR                | 185   | 14   |
| Ekaterina ALEXANDROVSKAYA / Harley WINDSOR | 180   | 15   |
| Deanna STELLATO / Nathan BARTHOLOMAY       | 175   | 16   |

This Worlds title is Aljona SAVCHENKO / Bruno MASSOT's for the taking after
their spectacular Olympic gold winning performance. Savchenko is looking for
her tenth World medal, and the pair is hoping to win their first World title as
a team. TARASOVA / MOROZOV are probably the only ones with a chance at stopping
them. YU / ZHANG were fourth at Worlds last year and are hoping to follow up a
disappointing free skate at the Olympics with a strong showing, and to place
well enough to ensure China's three pair spots next year despite the absence of
the top Chinese team, Sui and Han. JAMES / CIPRES have had potential all season
but haven't delivered in the big competitions. MARCHEI / HOTAREK are hoping to
follow up three spectacular Olympic performances with equal quality in front of
a home crowd. SCIMECA KNIERIM / KNIERIM are hoping to rise to the occasion with
a top-10 finish to secure USA's two pair spots for next year.

### Dance
| Skater                                  | Score | Rank |
|-----------------------------------------|-------|------| 
| Gabriella PAPADAKIS / Guillaume CIZERON | 207   | 1    |
| Madison HUBBELL / Zachary DONOHUE       | 190   | 2    |
| Anna CAPPELLINI / Luca LANOTTE          | 185   | 3    |
| Kaitlyn WEAVER / Andrew POJE            | 180   | 4    |
| Madison CHOCK / Evan BATES              | 180   | 5    |
| Alexandra STEPANOVA / Ivan BUKIN        | 175   | 6    |

It will take an absolute train wreck to stop PAPADAKIS / CIZERON from losing
their third World title after they lost the Olympic gold most likely due to a
costume malfunction. HUBELL / DONOHUE are looking to capitalize on their
potential after losing third-place short placements at the Olympics and at last
year's Worlds. CAPELLINI / LANOTTE, the 2014 World champions, are hoping to end
their career on a high note in front of a home crowd.