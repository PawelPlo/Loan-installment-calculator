#Loan installment calculator

kwota_kredytu = input("Wpisz wysokość kredytu w PLN:   ")
kwota_kredytu = int(kwota_kredytu)
print(f"Wysokość kredytu to {kwota_kredytu} PLN")

oprocentowanie_kredytu = input("Wpisz wysokość oprocentowania:   ")
oprocentowanie_kredytu = int(oprocentowanie_kredytu)
print(f"Wysokość oprocentowania wynosi {oprocentowanie_kredytu} %")

wysokość_raty = input("Wpisz proponowaną wysokość raty w PLN:     ")
wysokość_raty= int(wysokość_raty)
print(f"Proponowana przez Ciebie wysokość raty to {wysokość_raty} PLN")




inf_1=1.592824484
inf_1=float(inf_1)
kapitał_1=(1+(inf_1 + oprocentowanie_kredytu)/1200)*kwota_kredytu-wysokość_raty
print(kapitał_1)