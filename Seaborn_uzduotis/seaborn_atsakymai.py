import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


sns.set_theme()
mpg = sns.load_dataset('mpg')
print(mpg.to_string())
print(mpg.head(10))
print(mpg.shape)
#Reikšmės, kurios galbūt ne visai aiškios:
#mpg - miles per gallon
#displacement - variklio tūris kubiniais coliais.
# Jei norite pasisunkinti, galite perkaičiuoti stulpelius europietiškais standartais :)

# #1 Atspausdinkite histogramą, kurioje matytųsi, kiek automobilių turi kokią akseleraciją.
# # Šioje ir kitose užduotyse žaiskite su stiliais ir spalvomis, taip, kaip jums patinka.
sns.distplot(x=mpg['acceleration'],kde=True,bins=30,color="black")
plt.show()
print('\t1----'*10)
 #2 Atspausdinkite histogramą, kurioje matytųsi, kiek automobilių turi kokius variklio tūrius.
sns.distplot(mpg['displacement'], kde=False)
plt.show()
print('\t2----'*10)
#3.Atspausdinkite histogramą, kurioje matytųsi, kokie yra cilindrų skaičiaus variantai.
sns.countplot('cylinders', data=mpg)
sns.countplot(x=mpg["cylinders"])
plt.show()
print('\t3----'*10)
#
#4.Atspausdinkite histogramą, kurioje matytųsi, kiek yra pagaminimo metų variantų
sns.countplot(x=mpg['model_year'])
plt.show()
print('\t4----'*10)
#
#5.Atspausdinkite histogramą, kurioje matytųsi, kiek automobilių lentelėje kokia šalis pagamino.
sns.countplot(x=mpg['origin'])
plt.show()
print('\t5----'*10)
#
#6.Atspausdinkite histogramą, kurioje matytųsi, koks kurioje
# šalyje pagamintų automobilių variklio tūrio vidurkis.
sns.barplot(x=mpg['origin'], y=mpg['displacement'], data=mpg)
plt.show()
print('\t6----'*10)
#
#6 Atspausdinkite sklaidos diagramą,
# kurios x ašis būtų 'displacement',
# y - 'acceleration', taip pat kiekvienas
# taškas atspindėtų šalį gamintoją ir cilindrų skaičių
sns.scatterplot(x='displacement', y='acceleration', data=mpg, hue='origin', size='cylinders', palette="Set2")
plt.show()
print('\t6.1----'*10)
#
#7.Atspausdinkite visas įmanomas sklaidos diagramas lentelėje,
# kur pagal taško spalvą matytumėm šalį gamintoją.
# Kokias tendencijas galima aiškiai išskirti?
sns.pairplot(mpg, hue='origin')
plt.show()
print('\t7----'*10)
#
#8.Atspausdinkite stulpelinę diagramą, 'origin' x 'mpg'.
# Pabandykite interpretuoti rezultatą.
sns.boxplot('origin', 'mpg', data=mpg)
plt.show()
print('\t8----'*10)

#9.Sukurkite koreliacijų matricą.
# Jos pagrindu atspausdinkite mozaikinę diagramą.
cor = mpg.corr()
print(cor.to_string())
#
sns.heatmap(cor, annot=True, cmap='BrBG')
plt.show()
print('\t9----'*10)

#10.Atspausdinkite sklaidos diagramų rinkinį,
# kuriame kiekviena lentelė pagal šalį rodytų 'acceleration' ir 'mpg' sąntykį.
rink= sns.FacetGrid(data=mpg, col='origin')
rink.map(sns.scatterplot, 'acceleration', 'cylinders' )
plt.show()
print('\t9----'*10)

#jointplot¶ jointplot() allows you to basically match up two distplots for bivariate data. With your choice of what kind parameter to compare with:
# “scatter”
# “reg”
# “resid”
# “kde”
# “hex”
sns.jointplot(x='acceleration',y='horsepower',data=mpg,kind='scatter')
plt.show()
print('\t10----'*10)

#11.violinplot
column_list=[]
sns.violinplot(x=mpg['acceleration'])
plt.show()
print('\t11----'*10)

#output
  mpg  cylinders  displacement  horsepower  weight  acceleration  model_year  origin                                  name
0    18.0          8         307.0       130.0    3504          12.0          70     usa             chevrolet chevelle malibu
1    15.0          8         350.0       165.0    3693          11.5          70     usa                     buick skylark 320
2    18.0          8         318.0       150.0    3436          11.0          70     usa                    plymouth satellite
3    16.0          8         304.0       150.0    3433          12.0          70     usa                         amc rebel sst
4    17.0          8         302.0       140.0    3449          10.5          70     usa                           ford torino
5    15.0          8         429.0       198.0    4341          10.0          70     usa                      ford galaxie 500
6    14.0          8         454.0       220.0    4354           9.0          70     usa                      chevrolet impala
7    14.0          8         440.0       215.0    4312           8.5          70     usa                     plymouth fury iii
8    14.0          8         455.0       225.0    4425          10.0          70     usa                      pontiac catalina
9    15.0          8         390.0       190.0    3850           8.5          70     usa                    amc ambassador dpl
10   15.0          8         383.0       170.0    3563          10.0          70     usa                   dodge challenger se
11   14.0          8         340.0       160.0    3609           8.0          70     usa                    plymouth 'cuda 340
12   15.0          8         400.0       150.0    3761           9.5          70     usa                 chevrolet monte carlo
13   14.0          8         455.0       225.0    3086          10.0          70     usa               buick estate wagon (sw)
14   24.0          4         113.0        95.0    2372          15.0          70   japan                 toyota corona mark ii
15   22.0          6         198.0        95.0    2833          15.5          70     usa                       plymouth duster
16   18.0          6         199.0        97.0    2774          15.5          70     usa                            amc hornet
17   21.0          6         200.0        85.0    2587          16.0          70     usa                         ford maverick
18   27.0          4          97.0        88.0    2130          14.5          70   japan                          datsun pl510
19   26.0          4          97.0        46.0    1835          20.5          70  europe          volkswagen 1131 deluxe sedan
20   25.0          4         110.0        87.0    2672          17.5          70  europe                           peugeot 504
21   24.0          4         107.0        90.0    2430          14.5          70  europe                           audi 100 ls
22   25.0          4         104.0        95.0    2375          17.5          70  europe                              saab 99e
23   26.0          4         121.0       113.0    2234          12.5          70  europe                              bmw 2002
24   21.0          6         199.0        90.0    2648          15.0          70     usa                           amc gremlin
25   10.0          8         360.0       215.0    4615          14.0          70     usa                             ford f250
26   10.0          8         307.0       200.0    4376          15.0          70     usa                             chevy c20
27   11.0          8         318.0       210.0    4382          13.5          70     usa                            dodge d200
28    9.0          8         304.0       193.0    4732          18.5          70     usa                              hi 1200d
29   27.0          4          97.0        88.0    2130          14.5          71   japan                          datsun pl510
30   28.0          4         140.0        90.0    2264          15.5          71     usa                   chevrolet vega 2300
31   25.0          4         113.0        95.0    2228          14.0          71   japan                         toyota corona
32   25.0          4          98.0         NaN    2046          19.0          71     usa                            ford pinto
33   19.0          6         232.0       100.0    2634          13.0          71     usa                           amc gremlin
34   16.0          6         225.0       105.0    3439          15.5          71     usa             plymouth satellite custom
35   17.0          6         250.0       100.0    3329          15.5          71     usa             chevrolet chevelle malibu
36   19.0          6         250.0        88.0    3302          15.5          71     usa                       ford torino 500
37   18.0          6         232.0       100.0    3288          15.5          71     usa                           amc matador
38   14.0          8         350.0       165.0    4209          12.0          71     usa                      chevrolet impala
39   14.0          8         400.0       175.0    4464          11.5          71     usa             pontiac catalina brougham
40   14.0          8         351.0       153.0    4154          13.5          71     usa                      ford galaxie 500
41   14.0          8         318.0       150.0    4096          13.0          71     usa                     plymouth fury iii
42   12.0          8         383.0       180.0    4955          11.5          71     usa                     dodge monaco (sw)
43   13.0          8         400.0       170.0    4746          12.0          71     usa              ford country squire (sw)
44   13.0          8         400.0       175.0    5140          12.0          71     usa                   pontiac safari (sw)
45   18.0          6         258.0       110.0    2962          13.5          71     usa            amc hornet sportabout (sw)
46   22.0          4         140.0        72.0    2408          19.0          71     usa                   chevrolet vega (sw)
47   19.0          6         250.0       100.0    3282          15.0          71     usa                      pontiac firebird
48   18.0          6         250.0        88.0    3139          14.5          71     usa                          ford mustang
49   23.0          4         122.0        86.0    2220          14.0          71     usa                    mercury capri 2000
50   28.0          4         116.0        90.0    2123          14.0          71  europe                             opel 1900
51   30.0          4          79.0        70.0    2074          19.5          71  europe                           peugeot 304
52   30.0          4          88.0        76.0    2065          14.5          71  europe                             fiat 124b
53   31.0          4          71.0        65.0    1773          19.0          71   japan                   toyota corolla 1200
54   35.0          4          72.0        69.0    1613          18.0          71   japan                           datsun 1200
55   27.0          4          97.0        60.0    1834          19.0          71  europe                  volkswagen model 111
56   26.0          4          91.0        70.0    1955          20.5          71     usa                      plymouth cricket
57   24.0          4         113.0        95.0    2278          15.5          72   japan                 toyota corona hardtop
58   25.0          4          97.5        80.0    2126          17.0          72     usa                    dodge colt hardtop
59   23.0          4          97.0        54.0    2254          23.5          72  europe                     volkswagen type 3
60   20.0          4         140.0        90.0    2408          19.5          72     usa                        chevrolet vega
61   21.0          4         122.0        86.0    2226          16.5          72     usa                   ford pinto runabout
62   13.0          8         350.0       165.0    4274          12.0          72     usa                      chevrolet impala
63   14.0          8         400.0       175.0    4385          12.0          72     usa                      pontiac catalina
64   15.0          8         318.0       150.0    4135          13.5          72     usa                     plymouth fury iii
65   14.0          8         351.0       153.0    4129          13.0          72     usa                      ford galaxie 500
66   17.0          8         304.0       150.0    3672          11.5          72     usa                    amc ambassador sst
67   11.0          8         429.0       208.0    4633          11.0          72     usa                       mercury marquis
68   13.0          8         350.0       155.0    4502          13.5          72     usa                  buick lesabre custom
69   12.0          8         350.0       160.0    4456          13.5          72     usa            oldsmobile delta 88 royale
70   13.0          8         400.0       190.0    4422          12.5          72     usa                chrysler newport royal
71   19.0          3          70.0        97.0    2330          13.5          72   japan                       mazda rx2 coupe
72   15.0          8         304.0       150.0    3892          12.5          72     usa                      amc matador (sw)
73   13.0          8         307.0       130.0    4098          14.0          72     usa      chevrolet chevelle concours (sw)
74   13.0          8         302.0       140.0    4294          16.0          72     usa                 ford gran torino (sw)
75   14.0          8         318.0       150.0    4077          14.0          72     usa        plymouth satellite custom (sw)
76   18.0          4         121.0       112.0    2933          14.5          72  europe                       volvo 145e (sw)
77   22.0          4         121.0        76.0    2511          18.0          72  europe                   volkswagen 411 (sw)
78   21.0          4         120.0        87.0    2979          19.5          72  europe                      peugeot 504 (sw)
79   26.0          4          96.0        69.0    2189          18.0          72  europe                       renault 12 (sw)
80   22.0          4         122.0        86.0    2395          16.0          72     usa                       ford pinto (sw)
81   28.0          4          97.0        92.0    2288          17.0          72   japan                       datsun 510 (sw)
82   23.0          4         120.0        97.0    2506          14.5          72   japan           toyouta corona mark ii (sw)
83   28.0          4          98.0        80.0    2164          15.0          72     usa                       dodge colt (sw)
84   27.0          4          97.0        88.0    2100          16.5          72   japan              toyota corolla 1600 (sw)
85   13.0          8         350.0       175.0    4100          13.0          73     usa                     buick century 350
86   14.0          8         304.0       150.0    3672          11.5          73     usa                           amc matador
87   13.0          8         350.0       145.0    3988          13.0          73     usa                      chevrolet malibu
88   14.0          8         302.0       137.0    4042          14.5          73     usa                      ford gran torino
89   15.0          8         318.0       150.0    3777          12.5          73     usa                  dodge coronet custom
90   12.0          8         429.0       198.0    4952          11.5          73     usa              mercury marquis brougham
91   13.0          8         400.0       150.0    4464          12.0          73     usa             chevrolet caprice classic
92   13.0          8         351.0       158.0    4363          13.0          73     usa                              ford ltd
93   14.0          8         318.0       150.0    4237          14.5          73     usa              plymouth fury gran sedan
94   13.0          8         440.0       215.0    4735          11.0          73     usa          chrysler new yorker brougham
95   12.0          8         455.0       225.0    4951          11.0          73     usa              buick electra 225 custom
96   13.0          8         360.0       175.0    3821          11.0          73     usa               amc ambassador brougham
97   18.0          6         225.0       105.0    3121          16.5          73     usa                      plymouth valiant
98   16.0          6         250.0       100.0    3278          18.0          73     usa                 chevrolet nova custom
99   18.0          6         232.0       100.0    2945          16.0          73     usa                            amc hornet
100  18.0          6         250.0        88.0    3021          16.5          73     usa                         ford maverick
101  23.0          6         198.0        95.0    2904          16.0          73     usa                       plymouth duster
102  26.0          4          97.0        46.0    1950          21.0          73  europe               volkswagen super beetle
103  11.0          8         400.0       150.0    4997          14.0          73     usa                      chevrolet impala
104  12.0          8         400.0       167.0    4906          12.5          73     usa                          ford country
105  13.0          8         360.0       170.0    4654          13.0          73     usa                plymouth custom suburb
106  12.0          8         350.0       180.0    4499          12.5          73     usa              oldsmobile vista cruiser
107  18.0          6         232.0       100.0    2789          15.0          73     usa                           amc gremlin
108  20.0          4          97.0        88.0    2279          19.0          73   japan                         toyota carina
109  21.0          4         140.0        72.0    2401          19.5          73     usa                        chevrolet vega
110  22.0          4         108.0        94.0    2379          16.5          73   japan                            datsun 610
111  18.0          3          70.0        90.0    2124          13.5          73   japan                             maxda rx3
112  19.0          4         122.0        85.0    2310          18.5          73     usa                            ford pinto
113  21.0          6         155.0       107.0    2472          14.0          73     usa                      mercury capri v6
114  26.0          4          98.0        90.0    2265          15.5          73  europe                  fiat 124 sport coupe
115  15.0          8         350.0       145.0    4082          13.0          73     usa               chevrolet monte carlo s
116  16.0          8         400.0       230.0    4278           9.5          73     usa                    pontiac grand prix
117  29.0          4          68.0        49.0    1867          19.5          73  europe                              fiat 128
118  24.0          4         116.0        75.0    2158          15.5          73  europe                            opel manta
119  20.0          4         114.0        91.0    2582          14.0          73  europe                            audi 100ls
120  19.0          4         121.0       112.0    2868          15.5          73  europe                           volvo 144ea
121  15.0          8         318.0       150.0    3399          11.0          73     usa                     dodge dart custom
122  24.0          4         121.0       110.0    2660          14.0          73  europe                             saab 99le
123  20.0          6         156.0       122.0    2807          13.5          73   japan                        toyota mark ii
124  11.0          8         350.0       180.0    3664          11.0          73     usa                      oldsmobile omega
125  20.0          6         198.0        95.0    3102          16.5          74     usa                       plymouth duster
126  21.0          6         200.0         NaN    2875          17.0          74     usa                         ford maverick
127  19.0          6         232.0       100.0    2901          16.0          74     usa                            amc hornet
128  15.0          6         250.0       100.0    3336          17.0          74     usa                        chevrolet nova
129  31.0          4          79.0        67.0    1950          19.0          74   japan                           datsun b210
130  26.0          4         122.0        80.0    2451          16.5          74     usa                            ford pinto
131  32.0          4          71.0        65.0    1836          21.0          74   japan                   toyota corolla 1200
132  25.0          4         140.0        75.0    2542          17.0          74     usa                        chevrolet vega
133  16.0          6         250.0       100.0    3781          17.0          74     usa     chevrolet chevelle malibu classic
134  16.0          6         258.0       110.0    3632          18.0          74     usa                           amc matador
135  18.0          6         225.0       105.0    3613          16.5          74     usa            plymouth satellite sebring
136  16.0          8         302.0       140.0    4141          14.0          74     usa                      ford gran torino
137  13.0          8         350.0       150.0    4699          14.5          74     usa              buick century luxus (sw)
138  14.0          8         318.0       150.0    4457          13.5          74     usa             dodge coronet custom (sw)
139  14.0          8         302.0       140.0    4638          16.0          74     usa                 ford gran torino (sw)
140  14.0          8         304.0       150.0    4257          15.5          74     usa                      amc matador (sw)
141  29.0          4          98.0        83.0    2219          16.5          74  europe                              audi fox
142  26.0          4          79.0        67.0    1963          15.5          74  europe                     volkswagen dasher
143  26.0          4          97.0        78.0    2300          14.5          74  europe                            opel manta
144  31.0          4          76.0        52.0    1649          16.5          74   japan                         toyota corona
145  32.0          4          83.0        61.0    2003          19.0          74   japan                            datsun 710
146  28.0          4          90.0        75.0    2125          14.5          74     usa                            dodge colt
147  24.0          4          90.0        75.0    2108          15.5          74  europe                              fiat 128
148  26.0          4         116.0        75.0    2246          14.0          74  europe                           fiat 124 tc
149  24.0          4         120.0        97.0    2489          15.0          74   japan                           honda civic
150  26.0          4         108.0        93.0    2391          15.5          74   japan                                subaru
151  31.0          4          79.0        67.0    2000          16.0          74  europe                             fiat x1.9
152  19.0          6         225.0        95.0    3264          16.0          75     usa               plymouth valiant custom
153  18.0          6         250.0       105.0    3459          16.0          75     usa                        chevrolet nova
154  15.0          6         250.0        72.0    3432          21.0          75     usa                       mercury monarch
155  15.0          6         250.0        72.0    3158          19.5          75     usa                         ford maverick
156  16.0          8         400.0       170.0    4668          11.5          75     usa                      pontiac catalina
157  15.0          8         350.0       145.0    4440          14.0          75     usa                     chevrolet bel air
158  16.0          8         318.0       150.0    4498          14.5          75     usa                   plymouth grand fury
159  14.0          8         351.0       148.0    4657          13.5          75     usa                              ford ltd
160  17.0          6         231.0       110.0    3907          21.0          75     usa                         buick century
161  16.0          6         250.0       105.0    3897          18.5          75     usa             chevroelt chevelle malibu
162  15.0          6         258.0       110.0    3730          19.0          75     usa                           amc matador
163  18.0          6         225.0        95.0    3785          19.0          75     usa                         plymouth fury
164  21.0          6         231.0       110.0    3039          15.0          75     usa                         buick skyhawk
165  20.0          8         262.0       110.0    3221          13.5          75     usa                   chevrolet monza 2+2
166  13.0          8         302.0       129.0    3169          12.0          75     usa                       ford mustang ii
167  29.0          4          97.0        75.0    2171          16.0          75   japan                        toyota corolla
168  23.0          4         140.0        83.0    2639          17.0          75     usa                            ford pinto
169  20.0          6         232.0       100.0    2914          16.0          75     usa                           amc gremlin
170  23.0          4         140.0        78.0    2592          18.5          75     usa                         pontiac astro
171  24.0          4         134.0        96.0    2702          13.5          75   japan                         toyota corona
172  25.0          4          90.0        71.0    2223          16.5          75  europe                     volkswagen dasher
173  24.0          4         119.0        97.0    2545          17.0          75   japan                            datsun 710
174  18.0          6         171.0        97.0    2984          14.5          75     usa                            ford pinto
175  29.0          4          90.0        70.0    1937          14.0          75  europe                     volkswagen rabbit
176  19.0          6         232.0        90.0    3211          17.0          75     usa                             amc pacer
177  23.0          4         115.0        95.0    2694          15.0          75  europe                            audi 100ls
178  23.0          4         120.0        88.0    2957          17.0          75  europe                           peugeot 504
179  22.0          4         121.0        98.0    2945          14.5          75  europe                           volvo 244dl
180  25.0          4         121.0       115.0    2671          13.5          75  europe                             saab 99le
181  33.0          4          91.0        53.0    1795          17.5          75   japan                      honda civic cvcc
182  28.0          4         107.0        86.0    2464          15.5          76  europe                              fiat 131
183  25.0          4         116.0        81.0    2220          16.9          76  europe                             opel 1900
184  25.0          4         140.0        92.0    2572          14.9          76     usa                              capri ii
185  26.0          4          98.0        79.0    2255          17.7          76     usa                            dodge colt
186  27.0          4         101.0        83.0    2202          15.3          76  europe                          renault 12tl
187  17.5          8         305.0       140.0    4215          13.0          76     usa     chevrolet chevelle malibu classic
188  16.0          8         318.0       150.0    4190          13.0          76     usa                dodge coronet brougham
189  15.5          8         304.0       120.0    3962          13.9          76     usa                           amc matador
190  14.5          8         351.0       152.0    4215          12.8          76     usa                      ford gran torino
191  22.0          6         225.0       100.0    3233          15.4          76     usa                      plymouth valiant
192  22.0          6         250.0       105.0    3353          14.5          76     usa                        chevrolet nova
193  24.0          6         200.0        81.0    3012          17.6          76     usa                         ford maverick
194  22.5          6         232.0        90.0    3085          17.6          76     usa                            amc hornet
195  29.0          4          85.0        52.0    2035          22.2          76     usa                    chevrolet chevette
196  24.5          4          98.0        60.0    2164          22.1          76     usa                       chevrolet woody
197  29.0          4          90.0        70.0    1937          14.2          76  europe                             vw rabbit
198  33.0          4          91.0        53.0    1795          17.4          76   japan                           honda civic
199  20.0          6         225.0       100.0    3651          17.7          76     usa                        dodge aspen se
200  18.0          6         250.0        78.0    3574          21.0          76     usa                     ford granada ghia
201  18.5          6         250.0       110.0    3645          16.2          76     usa                    pontiac ventura sj
202  17.5          6         258.0        95.0    3193          17.8          76     usa                         amc pacer d/l
203  29.5          4          97.0        71.0    1825          12.2          76  europe                     volkswagen rabbit
204  32.0          4          85.0        70.0    1990          17.0          76   japan                          datsun b-210
205  28.0          4          97.0        75.0    2155          16.4          76   japan                        toyota corolla
206  26.5          4         140.0        72.0    2565          13.6          76     usa                            ford pinto
207  20.0          4         130.0       102.0    3150          15.7          76  europe                             volvo 245
208  13.0          8         318.0       150.0    3940          13.2          76     usa            plymouth volare premier v8
209  19.0          4         120.0        88.0    3270          21.9          76  europe                           peugeot 504
210  19.0          6         156.0       108.0    2930          15.5          76   japan                        toyota mark ii
211  16.5          6         168.0       120.0    3820          16.7          76  europe                    mercedes-benz 280s
212  16.5          8         350.0       180.0    4380          12.1          76     usa                      cadillac seville
213  13.0          8         350.0       145.0    4055          12.0          76     usa                             chevy c10
214  13.0          8         302.0       130.0    3870          15.0          76     usa                             ford f108
215  13.0          8         318.0       150.0    3755          14.0          76     usa                            dodge d100
216  31.5          4          98.0        68.0    2045          18.5          77   japan                     honda accord cvcc
217  30.0          4         111.0        80.0    2155          14.8          77     usa               buick opel isuzu deluxe
218  36.0          4          79.0        58.0    1825          18.6          77  europe                         renault 5 gtl
219  25.5          4         122.0        96.0    2300          15.5          77     usa                     plymouth arrow gs
220  33.5          4          85.0        70.0    1945          16.8          77   japan                 datsun f-10 hatchback
221  17.5          8         305.0       145.0    3880          12.5          77     usa             chevrolet caprice classic
222  17.0          8         260.0       110.0    4060          19.0          77     usa            oldsmobile cutlass supreme
223  15.5          8         318.0       145.0    4140          13.7          77     usa                 dodge monaco brougham
224  15.0          8         302.0       130.0    4295          14.9          77     usa               mercury cougar brougham
225  17.5          6         250.0       110.0    3520          16.4          77     usa                    chevrolet concours
226  20.5          6         231.0       105.0    3425          16.9          77     usa                         buick skylark
227  19.0          6         225.0       100.0    3630          17.7          77     usa                plymouth volare custom
228  18.5          6         250.0        98.0    3525          19.0          77     usa                          ford granada
229  16.0          8         400.0       180.0    4220          11.1          77     usa                 pontiac grand prix lj
230  15.5          8         350.0       170.0    4165          11.4          77     usa          chevrolet monte carlo landau
231  15.5          8         400.0       190.0    4325          12.2          77     usa                      chrysler cordoba
232  16.0          8         351.0       149.0    4335          14.5          77     usa                      ford thunderbird
233  29.0          4          97.0        78.0    1940          14.5          77  europe              volkswagen rabbit custom
234  24.5          4         151.0        88.0    2740          16.0          77     usa                 pontiac sunbird coupe
235  26.0          4          97.0        75.0    2265          18.2          77   japan               toyota corolla liftback
236  25.5          4         140.0        89.0    2755          15.8          77     usa                   ford mustang ii 2+2
237  30.5          4          98.0        63.0    2051          17.0          77     usa                    chevrolet chevette
238  33.5          4          98.0        83.0    2075          15.9          77     usa                        dodge colt m/m
239  30.0          4          97.0        67.0    1985          16.4          77   japan                             subaru dl
240  30.5          4          97.0        78.0    2190          14.1          77  europe                     volkswagen dasher
241  22.0          6         146.0        97.0    2815          14.5          77   japan                            datsun 810
242  21.5          4         121.0       110.0    2600          12.8          77  europe                              bmw 320i
243  21.5          3          80.0       110.0    2720          13.5          77   japan                            mazda rx-4
244  43.1          4          90.0        48.0    1985          21.5          78  europe       volkswagen rabbit custom diesel
245  36.1          4          98.0        66.0    1800          14.4          78     usa                           ford fiesta
246  32.8          4          78.0        52.0    1985          19.4          78   japan                      mazda glc deluxe
247  39.4          4          85.0        70.0    2070          18.6          78   japan                        datsun b210 gx
248  36.1          4          91.0        60.0    1800          16.4          78   japan                      honda civic cvcc
249  19.9          8         260.0       110.0    3365          15.5          78     usa     oldsmobile cutlass salon brougham
250  19.4          8         318.0       140.0    3735          13.2          78     usa                        dodge diplomat
251  20.2          8         302.0       139.0    3570          12.8          78     usa                  mercury monarch ghia
252  19.2          6         231.0       105.0    3535          19.2          78     usa                    pontiac phoenix lj
253  20.5          6         200.0        95.0    3155          18.2          78     usa                      chevrolet malibu
254  20.2          6         200.0        85.0    2965          15.8          78     usa                  ford fairmont (auto)
255  25.1          4         140.0        88.0    2720          15.4          78     usa                   ford fairmont (man)
256  20.5          6         225.0       100.0    3430          17.2          78     usa                       plymouth volare
257  19.4          6         232.0        90.0    3210          17.2          78     usa                           amc concord
258  20.6          6         231.0       105.0    3380          15.8          78     usa                 buick century special
259  20.8          6         200.0        85.0    3070          16.7          78     usa                        mercury zephyr
260  18.6          6         225.0       110.0    3620          18.7          78     usa                           dodge aspen
261  18.1          6         258.0       120.0    3410          15.1          78     usa                       amc concord d/l
262  19.2          8         305.0       145.0    3425          13.2          78     usa          chevrolet monte carlo landau
263  17.7          6         231.0       165.0    3445          13.4          78     usa       buick regal sport coupe (turbo)
264  18.1          8         302.0       139.0    3205          11.2          78     usa                           ford futura
265  17.5          8         318.0       140.0    4080          13.7          78     usa                       dodge magnum xe
266  30.0          4          98.0        68.0    2155          16.5          78     usa                    chevrolet chevette
267  27.5          4         134.0        95.0    2560          14.2          78   japan                         toyota corona
268  27.2          4         119.0        97.0    2300          14.7          78   japan                            datsun 510
269  30.9          4         105.0        75.0    2230          14.5          78     usa                            dodge omni
270  21.1          4         134.0        95.0    2515          14.8          78   japan             toyota celica gt liftback
271  23.2          4         156.0       105.0    2745          16.7          78     usa                      plymouth sapporo
272  23.8          4         151.0        85.0    2855          17.6          78     usa                oldsmobile starfire sx
273  23.9          4         119.0        97.0    2405          14.9          78   japan                         datsun 200-sx
274  20.3          5         131.0       103.0    2830          15.9          78  europe                             audi 5000
275  17.0          6         163.0       125.0    3140          13.6          78  europe                           volvo 264gl
276  21.6          4         121.0       115.0    2795          15.7          78  europe                            saab 99gle
277  16.2          6         163.0       133.0    3410          15.8          78  europe                         peugeot 604sl
278  31.5          4          89.0        71.0    1990          14.9          78  europe                   volkswagen scirocco
279  29.5          4          98.0        68.0    2135          16.6          78   japan                       honda accord lx
280  21.5          6         231.0       115.0    3245          15.4          79     usa                     pontiac lemans v6
281  19.8          6         200.0        85.0    2990          18.2          79     usa                      mercury zephyr 6
282  22.3          4         140.0        88.0    2890          17.3          79     usa                       ford fairmont 4
283  20.2          6         232.0        90.0    3265          18.2          79     usa                      amc concord dl 6
284  20.6          6         225.0       110.0    3360          16.6          79     usa                         dodge aspen 6
285  17.0          8         305.0       130.0    3840          15.4          79     usa             chevrolet caprice classic
286  17.6          8         302.0       129.0    3725          13.4          79     usa                       ford ltd landau
287  16.5          8         351.0       138.0    3955          13.2          79     usa                 mercury grand marquis
288  18.2          8         318.0       135.0    3830          15.2          79     usa                       dodge st. regis
289  16.9          8         350.0       155.0    4360          14.9          79     usa               buick estate wagon (sw)
290  15.5          8         351.0       142.0    4054          14.3          79     usa              ford country squire (sw)
291  19.2          8         267.0       125.0    3605          15.0          79     usa         chevrolet malibu classic (sw)
292  18.5          8         360.0       150.0    3940          13.0          79     usa  chrysler lebaron town @ country (sw)
293  31.9          4          89.0        71.0    1925          14.0          79  europe                      vw rabbit custom
294  34.1          4          86.0        65.0    1975          15.2          79   japan                      maxda glc deluxe
295  35.7          4          98.0        80.0    1915          14.4          79     usa           dodge colt hatchback custom
296  27.4          4         121.0        80.0    2670          15.0          79     usa                         amc spirit dl
297  25.4          5         183.0        77.0    3530          20.1          79  europe                    mercedes benz 300d
298  23.0          8         350.0       125.0    3900          17.4          79     usa                     cadillac eldorado
299  27.2          4         141.0        71.0    3190          24.8          79  europe                           peugeot 504
300  23.9          8         260.0        90.0    3420          22.2          79     usa     oldsmobile cutlass salon brougham
301  34.2          4         105.0        70.0    2200          13.2          79     usa                      plymouth horizon
302  34.5          4         105.0        70.0    2150          14.9          79     usa                  plymouth horizon tc3
303  31.8          4          85.0        65.0    2020          19.2          79   japan                            datsun 210
304  37.3          4          91.0        69.0    2130          14.7          79  europe                    fiat strada custom
305  28.4          4         151.0        90.0    2670          16.0          79     usa                 buick skylark limited
306  28.8          6         173.0       115.0    2595          11.3          79     usa                    chevrolet citation
307  26.8          6         173.0       115.0    2700          12.9          79     usa             oldsmobile omega brougham
308  33.5          4         151.0        90.0    2556          13.2          79     usa                       pontiac phoenix
309  41.5          4          98.0        76.0    2144          14.7          80  europe                             vw rabbit
310  38.1          4          89.0        60.0    1968          18.8          80   japan                 toyota corolla tercel
311  32.1          4          98.0        70.0    2120          15.5          80     usa                    chevrolet chevette
312  37.2          4          86.0        65.0    2019          16.4          80   japan                            datsun 310
313  28.0          4         151.0        90.0    2678          16.5          80     usa                    chevrolet citation
314  26.4          4         140.0        88.0    2870          18.1          80     usa                         ford fairmont
315  24.3          4         151.0        90.0    3003          20.1          80     usa                           amc concord
316  19.1          6         225.0        90.0    3381          18.7          80     usa                           dodge aspen
317  34.3          4          97.0        78.0    2188          15.8          80  europe                             audi 4000
318  29.8          4         134.0        90.0    2711          15.5          80   japan                toyota corona liftback
319  31.3          4         120.0        75.0    2542          17.5          80   japan                             mazda 626
320  37.0          4         119.0        92.0    2434          15.0          80   japan                  datsun 510 hatchback
321  32.2          4         108.0        75.0    2265          15.2          80   japan                        toyota corolla
322  46.6          4          86.0        65.0    2110          17.9          80   japan                             mazda glc
323  27.9          4         156.0       105.0    2800          14.4          80     usa                            dodge colt
324  40.8          4          85.0        65.0    2110          19.2          80   japan                            datsun 210
325  44.3          4          90.0        48.0    2085          21.7          80  europe                  vw rabbit c (diesel)
326  43.4          4          90.0        48.0    2335          23.7          80  europe                    vw dasher (diesel)
327  36.4          5         121.0        67.0    2950          19.9          80  europe                   audi 5000s (diesel)
328  30.0          4         146.0        67.0    3250          21.8          80  europe                    mercedes-benz 240d
329  44.6          4          91.0        67.0    1850          13.8          80   japan                   honda civic 1500 gl
330  40.9          4          85.0         NaN    1835          17.3          80  europe                  renault lecar deluxe
331  33.8          4          97.0        67.0    2145          18.0          80   japan                             subaru dl
332  29.8          4          89.0        62.0    1845          15.3          80  europe                      vokswagen rabbit
333  32.7          6         168.0       132.0    2910          11.4          80   japan                         datsun 280-zx
334  23.7          3          70.0       100.0    2420          12.5          80   japan                         mazda rx-7 gs
335  35.0          4         122.0        88.0    2500          15.1          80  europe                     triumph tr7 coupe
336  23.6          4         140.0         NaN    2905          14.3          80     usa                    ford mustang cobra
337  32.4          4         107.0        72.0    2290          17.0          80   japan                          honda accord
338  27.2          4         135.0        84.0    2490          15.7          81     usa                      plymouth reliant
339  26.6          4         151.0        84.0    2635          16.4          81     usa                         buick skylark
340  25.8          4         156.0        92.0    2620          14.4          81     usa                dodge aries wagon (sw)
341  23.5          6         173.0       110.0    2725          12.6          81     usa                    chevrolet citation
342  30.0          4         135.0        84.0    2385          12.9          81     usa                      plymouth reliant
343  39.1          4          79.0        58.0    1755          16.9          81   japan                        toyota starlet
344  39.0          4          86.0        64.0    1875          16.4          81     usa                        plymouth champ
345  35.1          4          81.0        60.0    1760          16.1          81   japan                      honda civic 1300
346  32.3          4          97.0        67.0    2065          17.8          81   japan                                subaru
347  37.0          4          85.0        65.0    1975          19.4          81   japan                        datsun 210 mpg
348  37.7          4          89.0        62.0    2050          17.3          81   japan                         toyota tercel
349  34.1          4          91.0        68.0    1985          16.0          81   japan                           mazda glc 4
350  34.7          4         105.0        63.0    2215          14.9          81     usa                    plymouth horizon 4
351  34.4          4          98.0        65.0    2045          16.2          81     usa                        ford escort 4w
352  29.9          4          98.0        65.0    2380          20.7          81     usa                        ford escort 2h
353  33.0          4         105.0        74.0    2190          14.2          81  europe                      volkswagen jetta
354  34.5          4         100.0         NaN    2320          15.8          81  europe                           renault 18i
355  33.7          4         107.0        75.0    2210          14.4          81   japan                         honda prelude
356  32.4          4         108.0        75.0    2350          16.8          81   japan                        toyota corolla
357  32.9          4         119.0       100.0    2615          14.8          81   japan                          datsun 200sx
358  31.6          4         120.0        74.0    2635          18.3          81   japan                             mazda 626
359  28.1          4         141.0        80.0    3230          20.4          81  europe             peugeot 505s turbo diesel
360  30.7          6         145.0        76.0    3160          19.6          81  europe                          volvo diesel
361  25.4          6         168.0       116.0    2900          12.6          81   japan                       toyota cressida
362  24.2          6         146.0       120.0    2930          13.8          81   japan                     datsun 810 maxima
363  22.4          6         231.0       110.0    3415          15.8          81     usa                         buick century
364  26.6          8         350.0       105.0    3725          19.0          81     usa                 oldsmobile cutlass ls
365  20.2          6         200.0        88.0    3060          17.1          81     usa                       ford granada gl
366  17.6          6         225.0        85.0    3465          16.6          81     usa                chrysler lebaron salon
367  28.0          4         112.0        88.0    2605          19.6          82     usa                    chevrolet cavalier
368  27.0          4         112.0        88.0    2640          18.6          82     usa              chevrolet cavalier wagon
369  34.0          4         112.0        88.0    2395          18.0          82     usa             chevrolet cavalier 2-door
370  31.0          4         112.0        85.0    2575          16.2          82     usa            pontiac j2000 se hatchback
371  29.0          4         135.0        84.0    2525          16.0          82     usa                        dodge aries se
372  27.0          4         151.0        90.0    2735          18.0          82     usa                       pontiac phoenix
373  24.0          4         140.0        92.0    2865          16.4          82     usa                  ford fairmont futura
374  23.0          4         151.0         NaN    3035          20.5          82     usa                        amc concord dl
375  36.0          4         105.0        74.0    1980          15.3          82  europe                   volkswagen rabbit l
376  37.0          4          91.0        68.0    2025          18.2          82   japan                    mazda glc custom l
377  31.0          4          91.0        68.0    1970          17.6          82   japan                      mazda glc custom
378  38.0          4         105.0        63.0    2125          14.7          82     usa                plymouth horizon miser
379  36.0          4          98.0        70.0    2125          17.3          82     usa                        mercury lynx l
380  36.0          4         120.0        88.0    2160          14.5          82   japan                      nissan stanza xe
381  36.0          4         107.0        75.0    2205          14.5          82   japan                          honda accord
382  34.0          4         108.0        70.0    2245          16.9          82   japan                        toyota corolla
383  38.0          4          91.0        67.0    1965          15.0          82   japan                           honda civic
384  32.0          4          91.0        67.0    1965          15.7          82   japan                    honda civic (auto)
385  38.0          4          91.0        67.0    1995          16.2          82   japan                         datsun 310 gx
386  25.0          6         181.0       110.0    2945          16.4          82     usa                 buick century limited
387  38.0          6         262.0        85.0    3015          17.0          82     usa     oldsmobile cutlass ciera (diesel)
388  26.0          4         156.0        92.0    2585          14.5          82     usa            chrysler lebaron medallion
389  22.0          6         232.0       112.0    2835          14.7          82     usa                        ford granada l
390  32.0          4         144.0        96.0    2665          13.9          82   japan                      toyota celica gt
391  36.0          4         135.0        84.0    2370          13.0          82     usa                     dodge charger 2.2
392  27.0          4         151.0        90.0    2950          17.3          82     usa                      chevrolet camaro
393  27.0          4         140.0        86.0    2790          15.6          82     usa                       ford mustang gl
394  44.0          4          97.0        52.0    2130          24.6          82  europe                             vw pickup
395  32.0          4         135.0        84.0    2295          11.6          82     usa                         dodge rampage
396  28.0          4         120.0        79.0    2625          18.6          82     usa                           ford ranger
397  31.0          4         119.0        82.0    2720          19.4          82     usa                            chevy s-10

Process finished with exit code 0

