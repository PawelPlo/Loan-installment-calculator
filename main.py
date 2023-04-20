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

#Wyliczenia dla pierwszego miesiąca

inf_1=1.592824484
inf_1=float(inf_1)
kapitał_1=(1+(inf_1 + oprocentowanie_kredytu)/1200)*kwota_kredytu-wysokość_raty
pomniejszenie_kapitału=kwota_kredytu-kapitał_1
print(f"Po pierwszym miesiącu Twoja pozostała kwota kredytu to {kapitał_1} PLN,\n to o {pomniejszenie_kapitału} PLN mniej niż w poprzednim miesiącu")
