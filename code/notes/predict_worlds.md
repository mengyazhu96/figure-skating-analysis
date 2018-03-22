Predicting Worlds 2018
======================

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

### Men
| Skater               | Score         | Rank |
|----------------------|---------------|------|
| Nathan CHEN          | 308.329612471 | 1    |
| Shoma UNO            | 295.941618262 | 2    |
| Boyang JIN           | 286.315187217 | 3    |
| Mikhail KOLYADA      | 268.53158458  | 4    |
| Dmitri ALIEV         | 261.828645113 | 5    |
| Vincent ZHOU         | 261.690619329 | 6    |
| Keiji TANAKA         | 248.443267669 | 7    |
| Max AARON            | 248.30964074  | 8    |
| Deniss VASILJEVS     | 243.382928834 | 9    |
| Michal BREZINA       | 240.090284906 | 10   |
| Nam NGUYEN           | 238.36975195  | 11   |
| Misha GE             | 236.168272337 | 12   |
| Keegan MESSING       | 235.479919123 | 13   |
| Kazuki TOMONO        | 232.432894086 | 14   |
| Alexei BYCHENKO      | 231.434236077 | 15   |
| Daniel SAMOHIN       | 230.965171337 | 16   |
| Matteo RIZZO         | 223.736666331 | 17   |
| Morisi KVITELASHVILI | 216.526859536 | 18   |
| Alexander MAJOROV    | 215.240797842 | 19   |
| Jinseo KIM           | 213.719917743 | 20   |
| Paul FENTZ           | 212.610600358 | 21   |
| Brendan KERRY        | 211.548539912 | 22   |
| Phillip HARRIS       | 205.987983427 | 23   |
| Ivan PAVLOV          | 204.4983093   | 24   |
| will not qualify to free skate |     |      |
| Julian Zhi Jie YEE   | 68.6231040033 | 25   |
| Romain PONSART       | 67.7166628218 | 26   |
| Javier RAYA          | 65.4491351326 | 27   |
| Chih-I TSAO          | 64.8792132226 | 28   |
| Stephane WALKER      | 63.0057256776 | 29   |
| Abzal RAKIMGALIEV    | 62.1378852652 | 30   |
| Donovan CARRILLO     | 61.4543528237 | 31   |
| Slavik HAYRAPETYAN   | 61.26536953   | 32   |
| Igor REZNICHENKO     | 61.1912089769 | 33   |
| Burak DEMIRBOGA      | 60.870223578  | 34   |
| Valtter VIRTANEN     | 60.0418329298 | 35   |
| Nicholas VRDOLJAK    | 58.070185633  | 36   |
| Larry LOUPOLOVER     | 53.5339335834 | 37   |


### Ladies
| Skater                   | Score         | Rank |
|--------------------------|---------------|------|
| Alina ZAGITOVA           | 230.825205165 | 1    |
| Satoko MIYAHARA          | 206.265386641 | 2    |
| Maria SOTSKOVA           | 203.103828227 | 3    |
| Kaetlyn OSMOND           | 200.439766982 | 4    |
| Wakaba HIGUCHI           | 196.463820478 | 5    |
| Carolina KOSTNER         | 193.299537077 | 6    |
| Bradie TENNELL           | 192.787906709 | 7    |
| Gabrielle DALEMAN        | 187.532783242 | 8    |
| Elizabet TURSYNBAEVA     | 185.37737229  | 9    |
| Dabin CHOI               | 180.908651567 | 10   |
| Stanislava KONSTANTINOVA | 180.0 (\*)    | 11   |
| Mariah BELL              | 179.856237816 | 12   |
| Loena HENDRICKX          | 173.364787174 | 13   |
| Hanul KIM                | 171.343619802 | 14   |
| Mirai NAGASU             | 170.159229748 | 15   |
| Nicole SCHOTT            | 168.712004757 | 16   |
| Nicole RAJICOVA          | 168.57445622  | 17   |
| Xiangning LI             | 166.112131768 | 18   |
| Laurine LECAVELIER       | 166.038388125 | 19   |
| Ivett TOTH               | 164.870737828 | 20   |
| Angelina KUCHVALSKA      | 158.956934717 | 21   |
| Alexia PAGANINI          | 156.267529728 | 22   |
| Kailani CRAINE           | 153.394327217 | 23   |
| Viveca LINDFORS          | 146.413403884 | 24   |
| will not qualify to free |               |      |
| Amy LIN                  | 50.8819927345 | 25   |
| Larkyn AUSTMAN           | 50.7873847864 | 26   |
| Elisabetta LECCARDI      | 50.0 (\*)     | 27   |
| Eliska BREZINOVA         | 49.8856735074 | 28   |
| Natasha MCKAY            | 49.6192116942 | 29   |
| Isadora WILLIAMS         | 48.6379782079 | 30   |
| Dasa GRM                 | 48.5127749989 | 31   |
| Anne Line GJERSEM        | 47.8517943366 | 32   |
| Anita OSTLUND            | 47.7570082056 | 33   |
| Gerli LIINAMAE           | 46.2253304724 | 34   |
| Elzbieta KROPA           | 45.9984975213 | 35   |
| Antonina DUBININA        | 40.8578141883 | 36   |
| Alisa STOMAKHINA         | 40.0 (\*)     | 37   |

(\*) no previous data in our dataset

### Pairs
| Skater                                     | Score         | Rank |
|--------------------------------------------|---------------|------|
| Aljona SAVCHENKO / Bruno MASSOT            | 227.913246342 | 1    |
| Evgenia TARASOVA / Vladimir MOROZOV        | 218.577713066 | 2    |
| Xiaoyu YU / Hao ZHANG                      | 215.604590892 | 3    |
| Natalia ZABIIAKO / Alexander ENBERT        | 205.592658883 | 4    |
| Julianne SEGUIN / Charlie BILODEAU         | 200.758895787 | 5    |
| Vanessa JAMES / Morgan CIPRES              | 199.653991286 | 6    |
| Alexa SCIMECA KNIERIM / Chris KNIERIM      | 197.780931915 | 7    |
| Valentina MARCHEI / Ondrej HOTAREK         | 196.890093487 | 8    |
| Cheng PENG / Yang JIN                      | 195.805681989 | 9    |
| Kristina ASTAKHOVA / Alexei ROGONOV        | 192.280210342 | 10   |
| Kirsten MOORE-TOWERS / Michael MARINARO    | 191.480342482 | 11   |
| Tae Ok RYOM / Ju Sik KIM                   | 187.903752736 | 12   |
| Anna DUSKOVA / Martin BIDAR                | 187.720123389 | 13   |
| Nicole DELLA MONICA / Matteo GUARISE       | 180.790483731 | 14   |
| Ekaterina ALEXANDROVSKAYA / Harley WINDSOR | 180.053941767 | 15   |
| Deanna STELLATO / Nathan BARTHOLOMAY       | 176.341104902 | 16   |
| will not qualify to free skate             |               |      |
| Annika HOCKE / Ruben BLOMMAERT             | 61.3267983666 | 17   |
| Paige CONNERS / Evgeni KRASNOPOLSKI        | 60.2644669575 | 18   |
| Camille RUEST / Andrew WOLFE               | 58.3213381418 | 19   |
| Miriam ZIEGLER / Severin KIEFER            | 57.9267749709 | 20   |
| Laura BARQUERO / Aritz MAESTU              | 55.6106417869 | 21   |
| Miu SUZAKI / Ryuichi KIHARA                | 54.8458350015 | 22   |
| Lola ESBRAT / Andrei NOVOSELOV             | 54.8452236821 | 23   |
| Lana PETRANOVIC / Antonio SOUZA-KORDEIRU   | 52.4751755678 | 24   |
| Zoe JONES / Christopher BOYADJI            | 50.3267272469 | 25   |
| Kyueun KIM / Alex Kang Chan KAM            | 49.9500611005 | 26   |
| Ioulia CHTCHETININA / Mikhail AKULOV       | 49.7213528547 | 27   |
| Elizaveta KASHITSYNA / Mark MAGYAR         | 45.0 (\*)     | 28   |


### Dance
| Skater                                  | Score           | Rank |
|-----------------------------------------|-----------------|------| 
| Gabriella PAPADAKIS / Guillaume CIZERON | 198.01247271798 | 1    |
| Madison CHOCK / Evan BATES              | 184.67276013933 | 2    |
| Kaitlyn WEAVER / Andrew POJE            | 181.84384088922 | 3    |
| Anna CAPPELLINI / Luca LANOTTE          | 180.60769664168 | 4    |
| Madison HUBBELL / Zachary DONOHUE       | 177.41845731714 | 5    |
| Alexandra STEPANOVA / Ivan BUKIN        | 175.35504537063 | 6    |
| Piper GILLES / Paul POIRIER             | 172.98419848149 | 7    |
| Kaitlin HAWAYEK / Jean-Luc BAKER        | 168.61260151518 | 8    |
| Tiffani ZAGORSKI / Jonathan GUERREIRO   | 164.55935969541 | 9    |
| Charlene GUIGNARD / Marco FABBRI        | 164.13068315669 | 10   |
| Carolane SOUCISSE / Shane FIRUS         | 163.22345380286 | 11   |
| Olivia SMART / Adria DIAZ               | 157.58983115959 | 12   |
| Kana MURAMOTO / Chris REED              | 156.39932541898 | 13   |
| Natalia KALISZEK / Maksym SPODYRIEV     | 156.14926842667 | 14   |
| Marie-Jade LAURIAULT / Romain LE GAC    | 153.73575220013 | 15   |
| Alexandra NAZAROVA / Maxim NIKITIN      | 152.89439863967 | 16   |
| Shiyue WANG / Xinyu LIU                 | 148.08234766872 | 17   |
| Kavita LORENZ / Joti POLIZOAKIS         | 148.04349524915 | 18   |
| Yura MIN / Alexander GAMELIN            | 148.0076596851  | 19   |
| Anna YANOVSKAYA / Adam LUKACS           | 147.52476250586 | 20   |
| will not qualify to free                |                 |      |
| Alisa AGAFONOVA / Alper UCAR            | 58.972156639650 | 21   |
| Allison REED / Saulius AMBRULEVICIUS    | 58.0 (\*)       | 22   |
| Cecilia TORN / Jussiville PARTANEN      | 57.01582313054  | 23   |
| Lilah FEAR / Lewis GIBSON               | 56.18967644145  | 24   |
| Lucie MYSLIVECKOVA / Lukas CSOLLEY      | 56.035596867770 | 25   |
| Cortney MANSOUROVA / Michal CESKA       | 55.94544055401  | 26   |
| Tina GARABEDIAN / Simon PROULX-SENECAL  | 52.6278683932   | 27   |
| Viktoria KAVALIOVA / Yurii BIELIAIEV    | 50.556778466120 | 28   |
| Chantelle KERRY / Andrew DODDS          | 48.251011438400 | 29   |
| Adel TANKOVA / Ronald ZILBERBERG        | 45.720083833630 | 30   |
| Teodora MARKOVA / Simon DAZE            | 45.558398006680 | 31   |

(\*) no previous data in our dataset

## Predicting the PB Total Score
For missing data, do the same guesses as in Model 3.

### Men
| Skater               | Score  | Rank |
|----------------------|--------|------|
| Shoma UNO            | 319.31 | 1    |
| Nathan CHEN          | 307.46 | 2    |
| Boyang JIN           | 303.58 | 3    |
| Mikhail KOLYADA      | 282.00 | 4    |
| Vincent ZHOU         | 276.69 | 5    |
| Dmitri ALIEV         | 274.06 | 6    |
| Keiji TANAKA         | 260.31 | 7    |
| Max AARON            | 259.69 | 8    |
| Misha GE             | 258.34 | 9    |
| Alexei BYCHENKO      | 257.01 | 10   |
| Keegan MESSING       | 255.43 | 11   |
| Daniel SAMOHIN       | 251.44 | 12   |
| Michal BREZINA       | 246.07 | 13   |
| Deniss VASILJEVS     | 243.52 | 14   |
| Nam NGUYEN           | 242.59 | 15   |
| Brendan KERRY        | 236.24 | 16   |
| Matteo RIZZO         | 232.41 | 17   |
| Kazuki TOMONO        | 231.93 | 18   |
| Alexander MAJOROV    | 225.86 | 19   |
| Paul FENTZ           | 225.85 | 20   |
| Julian Zhi Jie YEE   | 213.99 | 21   |
| Morisi KVITELASHVILI | 204.57 | 22   |
| Jinseo KIM           | 202.80 | 23   |
| Chih-I TSAO          | 195.21 | 24   |
| will not qualify for free |   |      |
| Slavik HAYRAPETYAN   | 69.49  | 25   |
| Ivan PAVLOV          | 69.26  | 26   |
| Phillip HARRIS       | 68.53  | 27   |
| Javier RAYA          | 66.88  | 28   |
| Stephane WALKER      | 65.96  | 29   |
| Abzal RAKIMGALIEV    | 64.18  | 30   |
| Igor REZNICHENKO     | 63.96  | 31   |
| Romain PONSART       | 63.81  | 32   |
| Burak DEMIRBOGA      | 61.27  | 33   |
| Valtter VIRTANEN     | 60.23  | 34   |
| Donovan CARRILLO     | 59.07  | 35   |
| Nicholas VRDOLJAK    | 59.02  | 36   |
| Larry LOUPOLOVER     | 52.44  | 37   |

### Ladies
| Skater                   | Score  | Rank |
|--------------------------|--------|------|
| Alina ZAGITOVA           | 239.57 | 1    |
| Kaetlyn OSMOND           | 231.02 | 2    |
| Satoko MIYAHARA          | 222.38 | 3    |
| Carolina KOSTNER         | 216.73 | 4    |
| Maria SOTSKOVA           | 216.28 | 5    |
| Gabrielle DALEMAN        | 213.52 | 6    |
| Wakaba HIGUCHI           | 212.52 | 7    |
| Bradie TENNELL           | 204.10 | 8    |
| Elizabet TURSYNBAEVA     | 200.98 | 9    |
| Dabin CHOI               | 199.26 | 10   |
| Mirai NAGASU             | 194.95 | 11   |
| Mariah BELL              | 191.59 | 12   |
| Laurine LECAVELIER       | 188.10 | 13   |
| Stanislava KONSTANTINOVA | 180.00 | 14   |
| Nicole RAJICOVA          | 179.70 | 15   |
| Angelina KUCHVALSKA      | 176.99 | 16   |
| Loena HENDRICKX          | 176.91 | 17   |
| Hanul KIM                | 175.71 | 18   |
| Xiangning LI             | 175.37 | 19   |
| Ivett TOTH               | 172.65 | 20   |
| Nicole SCHOTT            | 172.39 | 21   |
| Kailani CRAINE           | 168.61 | 22   |
| Amy LIN                  | 155.61 | 23   |
| Anita OSTLUND            | 145.14 | 24   |
| will not qualify for free |       |      |
| Isadora WILLIAMS         | 55.74  | 25   |
| Alexia PAGANINI          | 55.26  | 26   |
| Viveca LINDFORS          | 53.92  | 27   |
| Eliska BREZINOVA         | 52.06  | 28   |
| Larkyn AUSTMAN           | 51.42  | 29   |
| Natasha MCKAY            | 50.10  | 30   |
| Elisabetta LECCARDI      | 50.00  | 31   |
| Anne Line GJERSEM        | 49.80  | 32   |
| Dasa GRM                 | 47.40  | 33   |
| Elzbieta KROPA           | 46.06  | 34   |
| Gerli LIINAMAE           | 44.46  | 35   |
| Antonina DUBININA        | 41.05  | 36   |
| Alisa STOMAKHINA         | 40.00  | 37   |

### Pairs
| Skater                                     | Score  | Rank |
|--------------------------------------------|--------|------|
| Aljona SAVCHENKO / Bruno MASSOT            | 236.68 | 1    |
| Evgenia TARASOVA / Vladimir MOROZOV        | 227.58 | 2    |
| Vanessa JAMES / Morgan CIPRES              | 220.02 | 3    |
| Xiaoyu YU / Hao ZHANG                      | 219.20 | 4    |
| Valentina MARCHEI / Ondrej HOTAREK         | 216.59 | 5    |
| Natalia ZABIIAKO / Alexander ENBERT        | 212.88 | 6    |
| Alexa SCIMECA KNIERIM / Chris KNIERIM      | 207.96 | 7    |
| Julianne SEGUIN / Charlie BILODEAU         | 204.02 | 8    |
| Kristina ASTAKHOVA / Alexei ROGONOV        | 203.64 | 9    |
| Cheng PENG / Yang JIN                      | 202.92 | 10   |
| Nicole DELLA MONICA / Matteo GUARISE       | 202.74 | 11   |
| Kirsten MOORE-TOWERS / Michael MARINARO    | 198.11 | 12   |
| Tae Ok RYOM / Ju Sik KIM                   | 193.63 | 13   |
| Anna DUSKOVA / Martin BIDAR                | 189.09 | 14   |
| Miriam ZIEGLER / Severin KIEFER            | 181.75 | 15   |
| Ekaterina ALEXANDROVSKAYA / Harley WINDSOR | 178.10 | 16   |
| will not qualify for free                  |        |      |
| Annika HOCKE / Ruben BLOMMAERT             | 63.04  | 17   |
| Deanna STELLATO / Nathan BARTHOLOMAY       | 60.93  | 18   |
| Paige CONNERS / Evgeni KRASNOPOLSKI        | 60.35  | 19   |
| Camille RUEST / Andrew WOLFE               | 60.09  | 20   |
| Miu SUZAKI / Ryuichi KIHARA                | 57.74  | 21   |
| Lola ESBRAT / Andrei NOVOSELOV             | 57.48  | 22   |
| Lana PETRANOVIC / Antonio SOUZA-KORDEIRU   | 52.83  | 23   |
| Zoe JONES / Christopher BOYADJI            | 52.32  | 24   |
| Laura BARQUERO / Aritz MAESTU              | 51.46  | 25   |
| Ioulia CHTCHETININA / Mikhail AKULOV       | 46.57  | 26   |
| Elizaveta KASHITSYNA / Mark MAGYAR         | 45.00  | 27   |
| Kyueun KIM / Alex Kang Chan KAM            | 42.93  | 28   |

### Dance
| Skater                                  | Score  | Rank |
|-----------------------------------------|--------|------|
| Gabriella PAPADAKIS / Guillaume CIZERON | 205.28 | 1    |
| Kaitlyn WEAVER / Andrew POJE            | 190.01 | 2    |
| Madison HUBBELL / Zachary DONOHUE       | 189.43 | 3    |
| Madison CHOCK / Evan BATES              | 188.24 | 4    |
| Anna CAPPELLINI / Luca LANOTTE          | 186.64 | 5    |
| Alexandra STEPANOVA / Ivan BUKIN        | 184.86 | 6    |
| Piper GILLES / Paul POIRIER             | 182.57 | 7    |
| Charlene GUIGNARD / Marco FABBRI        | 177.75 | 8    |
| Kaitlin HAWAYEK / Jean-Luc BAKER        | 174.29 | 9    |
| Tiffani ZAGORSKI / Jonathan GUERREIRO   | 168.45 | 10   |
| Carolane SOUCISSE / Shane FIRUS         | 164.96 | 11   |
| Natalia KALISZEK / Maksym SPODYRIEV     | 164.48 | 12   |
| Kana MURAMOTO / Chris REED              | 163.86 | 13   |
| Alexandra NAZAROVA / Maxim NIKITIN      | 160.88 | 14   |
| Shiyue WANG / Xinyu LIU                 | 158.21 | 15   |
| Marie-Jade LAURIAULT / Romain LE GAC    | 157.62 | 16   |
| Olivia SMART / Adria DIAZ               | 154.81 | 17   |
| Alisa AGAFONOVA / Alper UCAR            | 153.68 | 18   |
| Yura MIN / Alexander GAMELIN            | 151.38 | 19   |
| Kavita LORENZ / Joti POLIZOAKIS         | 150.49 | 20   |
| will not qualify to free                |        |      |
| Lucie MYSLIVECKOVA / Lukas CSOLLEY      | 59.75  | 21   |
| Anna YANOVSKAYA / Adam LUKACS           | 59.13  | 22   |
| Allison REED / Saulius AMBRULEVICIUS    | 58.00  | 23   |
| Cecilia TORN / Jussiville PARTANEN      | 57.73  | 24   |
| Lilah FEAR / Lewis GIBSON               | 54.82  | 25   |
| Viktoria KAVALIOVA / Yurii BIELIAIEV    | 54.64  | 26   |
| Cortney MANSOUROVA / Michal CESKA       | 53.53  | 27   |
| Tina GARABEDIAN / Simon PROULX-SENECAL  | 53.00  | 28   |
| Adel TANKOVA / Ronald ZILBERBERG        | 46.66  | 29   |
| Chantelle KERRY / Andrew DODDS          | 45.42  | 30   |
| Teodora MARKOVA / Simon DAZE            | 41.99  | 31   |  


## OLS

### Men
[Short Start Order](http://www.isuresults.com/results/season1718/wc2018/wc2018_Men_SP_TimeSchedule.pdf)

### Ladies
[Free Start Order](http://www.isuresults.com/results/season1718/wc2018/wc2018_Ladies_FS_TimeSchedule.pdf)

| Predicted Final Rank | Skater | Predicted Free Score | Predicted Free Rank | Predicted Total Score | Start Order | PB Free Score | Short Score | Normalized Start Order |
|----|--------------------------|--------|----|--------|----|--------|-------|------|
| 1  | Alina ZAGITOVA           | 144.17 | 1  | 223.68 | 23 | 157.97 | 79.51 | 0.96 |
| 2  | Carolina KOSTNER         | 141.16 | 2  | 221.44 | 24 | 142.61 | 80.27 | 1.0  |
| 3  | Satoko MIYAHARA          | 139.25 | 3  | 213.61 | 22 | 146.44 | 74.36 | 0.92 |
| 4  | Kaetlyn OSMOND           | 136.36 | 4  | 209.09 | 19 | 152.15 | 72.73 | 0.79 |
| 5  | Gabrielle DALEMAN        | 136.22 | 5  | 207.83 | 21 | 141.33 | 71.61 | 0.88 |
| 6  | Maria SOTSKOVA           | 134.97 | 6  | 206.77 | 20 | 142.28 | 71.80 | 0.83 |
| 7  | Wakaba HIGUCHI           | 131.84 | 7  | 197.73 | 18 | 141.99 | 65.89 | 0.75 |
| 8  | Bradie TENNELL           | 127.35 | 9  | 196.11 | 16 | 137.09 | 68.76 | 0.67 |
| 9  | Mirai NAGASU             | 127.39 | 8  | 192.60 | 17 | 132.04 | 65.21 | 0.71 |
| 10 | Elizabet TURSYNBAEVA     | 124.77 | 10 | 187.15 | 14 | 138.69 | 62.38 | 0.58 |
| 11 | Loena HENDRICKX          | 118.27 | 12 | 182.34 | 13 | 121.78 | 64.07 | 0.54 |
| 12 | Nicole SCHOTT            | 119.87 | 11 | 181.71 | 15 | 116.85 | 61.84 | 0.63 |
| 13 | Hanul KIM                | 113.58 | 13 | 173.72 | 10 | 121.38 | 60.14 | 0.42 |
| 14 | Viveca LINDFORS          | 111.14 | 16 | 171.32 | 12 | 102.75 | 60.18 | 0.5  |
| 15 | Laurine LECAVELIER       | 111.39 | 15 | 171.18 | 8  | 124.29 | 59.79 | 0.33 |
| 16 | Mariah BELL              | 111.75 | 14 | 170.90 | 7  | 130.67 | 59.15 | 0.29 |
| 17 | Stanislava KONSTANTINOVA | 106.72 | 18 | 165.91 | 11 | 92.89  | 59.19 | 0.46 |
| 18 | Dabin CHOI               | 108.94 | 17 | 164.24 | 5  | 131.49 | 55.30 | 0.21 |
| 19 | Eliska BREZINOVA         | 105.06 | 19 | 163.43 | 9  | 97.63  | 58.37 | 0.38 |
| 20 | Kailani CRAINE           | 100.11 | 21 | 157.01 | 3  | 111.84 | 56.90 | 0.13 |
| 21 | Alexia PAGANINI          | 95.54  | 23 | 153.40 | 1  | 106.67 | 57.86 | 0.04 |
| 22 | Ivett TOTH               | 101.43 | 20 | 152.06 | 4  | 111.16 | 50.63 | 0.17 |
| 23 | Dasa GRM                 | 99.08  | 22 | 151.51 | 6  | 92.84  | 52.43 | 0.25 |
| 24 | Elisabetta LECCARDI      | 93.00  | 24 | 144.13 | 2  | 92.89  | 51.13 | 0.08 |
| 25 | Larkyn AUSTMAN           | DNQ    |    | 50.17  |    |        | 50.17 |      |
| 26 | Xiangning LI             | DNQ    |    | 50.06  |    |        | 50.06 |      |
| 27 | Nicole RAJICOVA          | DNQ    |    | 49.87  |    |        | 49.87 |      |
| 28 | Amy LIN                  | DNQ    |    | 49.31  |    |        | 49.31 |      |
| 29 | Anita OSTLUND            | DNQ    |    | 48.99  |    |        | 48.99 |      |
| 30 | Alisa STOMAKHINA         | DNQ    |    | 48.71  |    |        | 48.71 |      |
| 31 | Elzbieta KROPA           | DNQ    |    | 46.53  |    |        | 46.53 |      |
| 32 | Natasha MCKAY            | DNQ    |    | 45.89  |    |        | 45.89 |      |
| 33 | Anne Line GJERSEM        | DNQ    |    | 45.25  |    |        | 45.25 |      |
| 34 | Gerli LIINAMAE           | DNQ    |    | 45.14  |    |        | 45.14 |      |
| 35 | Isadora WILLIAMS         | DNQ    |    | 42.16  |    |        | 42.16 |      |
| 36 | Antonina DUBININA        | DNQ    |    | 41.40  |    |        | 41.40 |      |
| 37 | Angelina KUCHVALSKA      | DNQ    |    | 35.78  |    |        | 35.78 |      |


[Short Start Order](www.isuresults.com/results/season1718/wc2018/wc2018_Ladies_SP_TimeSchedule.pdf)

| PB Short | Skater | Normalized Start Order | Predicted Score | Predicted Rank | Start |
|-------|--------------------------|------|--------|----|----|
| 82.92 | Alina ZAGITOVA           | 0.92 | 73.94  | 1  | 34 |
| 78.87 | Kaetlyn OSMOND           | 0.97 | 72.70  | 2  | 36 |
| 75.94 | Satoko MIYAHARA          | 1.0  | 71.66  | 3  | 37 |
| 78.30 | Carolina KOSTNER         | 0.89 | 71.52  | 4  | 33 |
| 74.00 | Maria SOTSKOVA           | 0.95 | 70.16  | 5  | 35 |
| 73.26 | Wakaba HIGUCHI           | 0.86 | 68.90  | 6  | 32 |
| 70.40 | Mirai NAGASU             | 0.81 | 66.98  | 7  | 30 |
| 72.70 | Gabrielle DALEMAN        | 0.70 | 66.81  | 8  | 26 |
| 67.77 | Dabin CHOI               | 0.76 | 65.16  | 9  | 28 |
| 66.87 | Elizabet TURSYNBAEVA     | 0.78 | 65.06  | 10 | 29 |
| 63.85 | Mariah BELL              | 0.84 | 64.28  | 11 | 31 |
| 66.61 | Laurine LECAVELIER       | 0.57 | 62.48  | 12 | 21 |
| 67.01 | Bradie TENNELL           | 0.54 | 62.36  | 13 | 20 |
| 61.01 | Nicole RAJICOVA          | 0.73 | 61.76  | 14 | 27 |
| 61.49 | Ivett TOTH               | 0.68 | 61.37  | 15 | 25 |
| 59.20 | Nicole SCHOTT            | 0.59 | 59.40  | 16 | 22 |
| 57.54 | Loena HENDRICKX          | 0.62 | 58.94  | 17 | 23 |
| 56.04 | Anita OSTLUND            | 0.51 | 57.03  | 18 | 19 |
| 56.97 | Kailani CRAINE           | 0.43 | 56.54  | 19 | 16 |
| 55.26 | Alexia PAGANINI          | 0.49 | 56.37  | 20 | 18 |
| 57.50 | Amy LIN                  | 0.38 | 56.17  | 21 | 14 |
| 58.99 | Angelina KUCHVALSKA      | 0.19 | 54.70  | 22 | 7  |
| 52.06 | Eliska BREZINOVA         | 0.46 | 54.59  | 23 | 17 |
| 61.15 | Hanul KIM                | 0.05 | 54.16  | 24 | 2  |
| 55.74 | Isadora WILLIAMS         | 0.27 | 54.13  | 25 | 10 |
| 46.18 | Stanislava KONSTANTINOVA | 0.65 | 54.05  | 26 | 24 |
| 59.20 | Xiangning LI             | 0.08 | 53.57  | 27 | 3  |
| 53.92 | Viveca LINDFORS          | 0.16 | 52.07  | 28 | 6  |
| 49.80 | Anne Line GJERSEM        | 0.32 | 52.03  | 29 | 12 |
| 51.42 | Larkyn AUSTMAN           | 0.24 | 51.85  | 30 | 9  |
| 46.06 | Elzbieta KROPA           | 0.41 | 51.23  | 31 | 15 |
| 50.10 | Natasha MCKAY            | 0.11 | 49.71  | 32 | 4  |
| 44.46 | Gerli LIINAMAE           | 0.30 | 49.27  | 33 | 11 |
| 46.18 | Alisa STOMAKHINA         | 0.22 | 49.14  | 34 | 8  |
| 41.05 | Antonina DUBININA        | 0.35 | 48.32  | 35 | 13 |
| 46.18 | Elisabetta LECCARDI      | 0.14 | 48.22  | 36 | 5  |
| 47.40 | Dasa GRM                 | 0.03 | 47.56  | 37 | 1  |



### Pairs
[Free Start Order](http://www.isuresults.com/results/season1718/wc2018/wc2018_Pairs_FS_TimeSchedule.pdf)


[Short Start Order](http://www.isuresults.com/results/season1718/wc2018/wc2018_Pairs_SP_TimeSchedule.pdf)

| PB Short | Skater | Normalized Start Order | Predicted Score | Predicted Rank | Start |
|-------|--------------------------------------------|------|-------|----|----|
| 81.68 | Evgenia TARASOVA / Vladimir MOROZOV        | 0.68 | 75.23 | 1  | 19 |
| 79.84 | Aljona SAVCHENKO / Bruno MASSOT            | 0.70 | 74.28 | 2  | 20 |
| 75.52 | Vanessa JAMES / Morgan CIPRES              | 0.76 | 72.00 | 3  | 21 |
| 74.35 | Natalia ZABIIAKO / Alexander ENBERT        | 0.73 | 71.03 | 4  | 20 |
| 75.58 | Xiaoyu YU / Hao ZHANG                      | 0.62 | 70.89 | 5  | 17 |
| 74.00 | Nicole DELLA MONICA / Matteo GUARISE       | 0.65 | 70.12 | 6  | 18 |
| 74.50 | Valentina MARCHEI / Ondrej HOTAREK         | 0.57 | 69.75 | 7  | 16 |
| 73.33 | Cheng PENG / Yang JIN                      | 0.43 | 67.87 | 8  | 12 |
| 71.16 | Julianne SEGUIN / Charlie BILODEAU         | 0.59 | 67.86 | 9  | 17 |
| 72.17 | Alexa SCIMECA KNIERIM / Chris KNIERIM      | 0.49 | 67.59 | 10 | 14 |
| 70.89 | Kirsten MOORE-TOWERS / Michael MARINARO    | 0.51 | 67.00 | 11 | 14 |
| 70.52 | Kristina ASTAKHOVA / Alexei ROGONOV        | 0.41 | 65.86 | 12 | 11 |
| 66.45 | Ekaterina ALEXANDROVSKAYA / Harley WINDSOR | 0.46 | 63.73 | 13 | 13 |
| 69.40 | Tae Ok RYOM / Ju Sik KIM                   | 0.19 | 63.32 | 14 | 5  |
| 63.94 | Miriam ZIEGLER / Severin KIEFER            | 0.54 | 62.82 | 15 | 15 |
| 65.90 | Anna DUSKOVA / Martin BIDAR                | 0.14 | 60.64 | 16 | 4  |
| 63.04 | Annika HOCKE / Ruben BLOMMAERT             | 0.11 | 58.59 | 17 | 3  |
| 60.09 | Camille RUEST / Andrew WOLFE               | 0.27 | 58.09 | 18 | 8  |
| 60.93 | Deanna STELLATO / Nathan BARTHOLOMAY       | 0.08 | 57.03 | 19 | 2  |
| 57.74 | Miu SUZAKI / Ryuichi KIHARA                | 0.30 | 56.82 | 20 | 8  |
| 60.35 | Paige CONNERS / Evgeni KRASNOPOLSKI        | 0.05 | 56.43 | 21 | 2  |
| 57.48 | Lola ESBRAT / Andrei NOVOSELOV             | 0.24 | 56.20 | 22 | 7  |
| 52.83 | Lana PETRANOVIC / Antonio SOUZA-KORDEIRU   | 0.32 | 53.93 | 23 | 9  |
| 51.46 | Laura BARQUERO / Aritz MAESTU              | 0.35 | 53.29 | 24 | 10 |
| 52.32 | Zoe JONES / Christopher BOYADJI            | 0.22 | 52.70 | 25 | 6  |
| 51.76 | Elizaveta KASHITSYNA / Mark MAGYAR         | 0.03 | 50.74 | 26 | 1  |
| 46.57 | Ioulia CHTCHETININA / Mikhail AKULOV       | 0.16 | 48.59 | 27 | 5  |
| 42.93 | Kyueun KIM / Alex Kang Chan KAM            | 0.38 | 48.10 | 28 | 11 |




## My Tweaks on Model 3

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

### Dance
| Skater                                  | Score | Rank |
|-----------------------------------------|-------|------| 
| Gabriella PAPADAKIS / Guillaume CIZERON | 207   | 1    |
| Madison HUBBELL / Zachary DONOHUE       | 190   | 2    |
| Anna CAPPELLINI / Luca LANOTTE          | 185   | 3    |
| Kaitlyn WEAVER / Andrew POJE            | 180   | 4    |
| Madison CHOCK / Evan BATES              | 180   | 5    |
| Alexandra STEPANOVA / Ivan BUKIN        | 175   | 6    |