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