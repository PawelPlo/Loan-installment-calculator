#Loan installment calculator

kwota_kredytu = input("Wpisz wysokość kredytu w PLN:   ")
kwota_kredytu = float(kwota_kredytu)
print(f"Wysokość kredytu to {kwota_kredytu} PLN")

oprocentowanie_kredytu = input("Wpisz wysokość oprocentowania:   ")
oprocentowanie_kredytu = float(oprocentowanie_kredytu)
print(f"Wysokość oprocentowania wynosi {oprocentowanie_kredytu} %")

wysokość_raty = input("Wpisz proponowaną wysokość raty w PLN:     ")
wysokość_raty= float(wysokość_raty)
print(f"Proponowana przez Ciebie wysokość raty to {wysokość_raty} PLN")

#Month nr 1

inf_1=1.592824484
inf_1=float(inf_1)
kapitał_1=(1+(inf_1 + oprocentowanie_kredytu)/1200)*kwota_kredytu-wysokość_raty
pomniejszenie_kapitału_1=kwota_kredytu-kapitał_1
print(f"Po pierwszym miesiącu Twoja pozostała kwota kredytu do spłaty to {kapitał_1} PLN,\nto o {pomniejszenie_kapitału_1} PLN mniej niż w poprzednim miesiącu")
print()

#Month nr 2

inf_2=-0.453509101198007
inf_2=float(inf_2)
kapitał_2=(1+(inf_2 + oprocentowanie_kredytu)/1200)*kapitał_1-wysokość_raty
pomniejszenie_kapitału_2=kapitał_1-kapitał_2
print(f"Po drugim miesiącu Twoja pozostała kwota kredytu do spłaty to {kapitał_2} PLN,\nto o {pomniejszenie_kapitału_2} PLN mniej niż w poprzednim miesiącu")
print()

#Month nr 3

inf_3=2.32467171712441
inf_3=float(inf_3)
kapitał_3=(1+(inf_3 + oprocentowanie_kredytu)/1200)*kapitał_2-wysokość_raty
pomniejszenie_kapitału_3=kapitał_2-kapitał_3
print(f"Po trzecim miesiącu Twoja pozostała kwota kredytu do spłaty to {kapitał_3} PLN,\nto o {pomniejszenie_kapitału_3} PLN mniej niż w poprzednim miesiącu")
print()

#Month nr 4

inf_4=1.26125440724877
inf_4=float(inf_4)
kapitał_4=(1+(inf_4 + oprocentowanie_kredytu)/1200)*kapitał_3-wysokość_raty
pomniejszenie_kapitału_4=kapitał_3-kapitał_4
print(f"Po czwartym miesiącu Twoja pozostała kwota kredytu do spłaty to {kapitał_4} PLN,\nto o {pomniejszenie_kapitału_4} PLN mniej niż w poprzednim miesiącu")
print()

#Month nr 5

inf_5=1.78252628571251
inf_5=float(inf_5)
kapitał_5=(1+(inf_5 + oprocentowanie_kredytu)/1200)*kapitał_4-wysokość_raty
pomniejszenie_kapitału_5=kapitał_4-kapitał_5
print(f"Po piątym miesiącu Twoja pozostała kwota kredytu do spłaty to {kapitał_5} PLN,\nto o {pomniejszenie_kapitału_5} PLN mniej niż w poprzednim miesiącu")
print()

#Month nr 6

inf_6=2.32938454145522
inf_6=float(inf_6)
kapitał_6=(1+(inf_6 + oprocentowanie_kredytu)/1200)*kapitał_5-wysokość_raty
pomniejszenie_kapitału_6=kapitał_5-kapitał_6
print(f"Po szóstym miesiącu Twoja pozostała kwota kredytu do spłaty to {kapitał_6} PLN,\nto o {pomniejszenie_kapitału_6} PLN mniej niż w poprzednim miesiącu")
print()

#Month nr 7

inf_7=1.50222984223283
inf_7=float(inf_7)
kapitał_7=(1+(inf_7 + oprocentowanie_kredytu)/1200)*kapitał_6-wysokość_raty
pomniejszenie_kapitału_7=kapitał_6-kapitał_7
print(f"Po siódmym miesiącu Twoja pozostała kwota kredytu do spłaty to {kapitał_7} PLN,\nto o {pomniejszenie_kapitału_7} PLN mniej niż w poprzednim miesiącu")
print()

#Month nr 8

inf_8=1.78252628571251
inf_8=float(inf_8)
kapitał_8=(1+(inf_8 + oprocentowanie_kredytu)/1200)*kapitał_7-wysokość_raty
pomniejszenie_kapitału_8=kapitał_7-kapitał_8
print(f"Po ósmym miesiącu Twoja pozostała kwota kredytu do spłaty to {kapitał_8} PLN,\nto o {pomniejszenie_kapitału_8} PLN mniej niż w poprzednim miesiącu")
print()

#Month nr 9

inf_9=2.32884899407637
inf_9=float(inf_9)
kapitał_9=(1+(inf_9 + oprocentowanie_kredytu)/1200)*kapitał_8-wysokość_raty
pomniejszenie_kapitału_9=kapitał_8-kapitał_9
print(f"Po dziewiątym miesiącu Twoja pozostała kwota kredytu do spłaty to {kapitał_9} PLN,\nto o {pomniejszenie_kapitału_9} PLN mniej niż w poprzednim miesiącu")
print()

#Month nr 10

inf_10=0.616921348207244
inf_10=float(inf_10)
kapitał_10=(1+(inf_10 + oprocentowanie_kredytu)/1200)*kapitał_9-wysokość_raty
pomniejszenie_kapitału_10=kapitał_9-kapitał_10
print(f"Po dziesiątym miesiącu Twoja pozostała kwota kredytu do spłaty to {kapitał_10} PLN,\nto o {pomniejszenie_kapitału_10} PLN mniej niż w poprzednim miesiącu")
print()

#Month nr 11

inf_11=2.35229588637833
inf_11=float(inf_11)
kapitał_11=(1+(inf_11 + oprocentowanie_kredytu)/1200)*kapitał_10-wysokość_raty
pomniejszenie_kapitału_11=kapitał_10-kapitał_11
print(f"Po jedenastym miesiącu Twoja pozostała kwota kredytu do spłaty to {kapitał_11} PLN,\nto o {pomniejszenie_kapitału_11} PLN mniej niż w poprzednim miesiącu")
print()

#Month nr 12

inf_12=0.337779545187098
inf_12=float(inf_12)
kapitał_12=(1+(inf_12 + oprocentowanie_kredytu)/1200)*kapitał_11-wysokość_raty
pomniejszenie_kapitału_12=kapitał_11-kapitał_12
print(f"Po dwunastym miesiącu Twoja pozostała kwota kredytu do spłaty to {kapitał_12} PLN,\nto o {pomniejszenie_kapitału_12} PLN mniej niż w poprzednim miesiącu")
print()

#Month nr 13

inf_13=1.57703524727525
inf_13=float(inf_13)
kapitał_13=(1+(inf_13 + oprocentowanie_kredytu)/1200)*kapitał_12-wysokość_raty
pomniejszenie_kapitału_13=kapitał_12-kapitał_13
print(f"Po trzynastym miesiącu Twoja pozostała kwota kredytu do spłaty to {kapitał_13} PLN,\nto o {pomniejszenie_kapitału_13} PLN mniej niż w poprzednim miesiącu")
print()

#Month nr 14

inf_14=-0.292781442607648
inf_14=float(inf_14)
kapitał_14=(1+(inf_14 + oprocentowanie_kredytu)/1200)*kapitał_13-wysokość_raty
pomniejszenie_kapitału_14=kapitał_13-kapitał_14
print(f"Po czternastym miesiącu Twoja pozostała kwota kredytu do spłaty to {kapitał_14} PLN,\nto o {pomniejszenie_kapitału_14} PLN mniej niż w poprzednim miesiącu")
print()

#Month nr 15

inf_15=2.48619659017508
inf_15=float(inf_15)
kapitał_15=(1+(inf_15 + oprocentowanie_kredytu)/1200)*kapitał_14-wysokość_raty
pomniejszenie_kapitału_15=kapitał_14-kapitał_15
print(f"Po piętnastym miesiącu Twoja pozostała kwota kredytu do spłaty to {kapitał_15} PLN,\nto o {pomniejszenie_kapitału_15} PLN mniej niż w poprzednim miesiącu")
print()

#Month nr 16

inf_16=0.267110317834564
inf_16=float(inf_16)
kapitał_16=(1+(inf_16 + oprocentowanie_kredytu)/1200)*kapitał_15-wysokość_raty
pomniejszenie_kapitału_16=kapitał_15-kapitał_16
print(f"Po szesnastym miesiącu Twoja pozostała kwota kredytu do spłaty to {kapitał_16} PLN,\nto o {pomniejszenie_kapitału_16} PLN mniej niż w poprzednim miesiącu")
print()

#Month nr 17

inf_17=1.41795267229799
inf_17=float(inf_17)
kapitał_17=(1+(inf_17 + oprocentowanie_kredytu)/1200)*kapitał_16-wysokość_raty
pomniejszenie_kapitału_17=kapitał_16-kapitał_17
print(f"Po siedemnastym miesiącu Twoja pozostała kwota kredytu do spłaty to {kapitał_17} PLN,\nto o {pomniejszenie_kapitału_17} PLN mniej niż w poprzednim miesiącu")
print()

#Month nr 18

inf_18=1.05424326726375
inf_18=float(inf_18)
kapitał_18=(1+(inf_18 + oprocentowanie_kredytu)/1200)*kapitał_17-wysokość_raty
pomniejszenie_kapitału_18=kapitał_17-kapitał_18
print(f"Po osiemnastym miesiącu Twoja pozostała kwota kredytu do spłaty to {kapitał_18} PLN,\nto o {pomniejszenie_kapitału_18} PLN mniej niż w poprzednim miesiącu")
print()

#Month nr 19

inf_19=1.4805201044812
inf_19=float(inf_19)
kapitał_19=(1+(inf_19 + oprocentowanie_kredytu)/1200)*kapitał_18-wysokość_raty
pomniejszenie_kapitału_19=kapitał_18-kapitał_19
print(f"Po dziewiętnastym miesiącu Twoja pozostała kwota kredytu do spłaty to {kapitał_19} PLN,\nto o {pomniejszenie_kapitału_19} PLN mniej niż w poprzednim miesiącu")
print()

#Month nr 20

inf_20=1.57703524727525
inf_20=float(inf_20)
kapitał_20=(1+(inf_20 + oprocentowanie_kredytu)/1200)*kapitał_19-wysokość_raty
pomniejszenie_kapitału_20=kapitał_19-kapitał_20
print(f"Po dwudziestym miesiącu Twoja pozostała kwota kredytu do spłaty to {kapitał_20} PLN,\nto o {pomniejszenie_kapitału_20} PLN mniej niż w poprzednim miesiącu")
print()

#Month nr 21

inf_21=-0.0774206903147018
inf_21=float(inf_21)
kapitał_21=(1+(inf_21 + oprocentowanie_kredytu)/1200)*kapitał_20-wysokość_raty
pomniejszenie_kapitału_21=kapitał_20-kapitał_21
print(f"Po dwudziestym pierwszym miesiącu Twoja pozostała kwota kredytu do spłaty to {kapitał_21} PLN,\nto o {pomniejszenie_kapitału_21} PLN mniej niż w poprzednim miesiącu")
print()

#Month nr 22

inf_22=1.16573339872354
inf_22=float(inf_22)
kapitał_22=(1+(inf_22 + oprocentowanie_kredytu)/1200)*kapitał_21-wysokość_raty
pomniejszenie_kapitału_22=kapitał_21-kapitał_22
print(f"Po dwudziestym drugim miesiącu Twoja pozostała kwota kredytu do spłaty to {kapitał_22} PLN,\nto o {pomniejszenie_kapitału_22} PLN mniej niż w poprzednim miesiącu")
print()

#Month nr 23

inf_23=-0.404186717638335
inf_23=float(inf_23)
kapitał_23=(1+(inf_23 + oprocentowanie_kredytu)/1200)*kapitał_22-wysokość_raty
pomniejszenie_kapitału_23=kapitał_22-kapitał_23
print(f"Po dwudziestym trzecim miesiącu Twoja pozostała kwota kredytu do spłaty to {kapitał_23} PLN,\nto o {pomniejszenie_kapitału_23} PLN mniej niż w poprzednim miesiącu")
print()

#Month nr 24

inf_24=1.49970852083123
inf_24=float(inf_24)
kapitał_24=(1+(inf_24 + oprocentowanie_kredytu)/1200)*kapitał_23-wysokość_raty
pomniejszenie_kapitału_24=kapitał_23-kapitał_24
print(f"Po dwudziestym czwartym miesiącu Twoja pozostała kwota kredytu do spłaty to {kapitał_24} PLN,\nto o {pomniejszenie_kapitału_24} PLN mniej niż w poprzednim miesiącu")
print()