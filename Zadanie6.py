droga = float(input("podaj dlugosc trasy: "))
spalanie = float(input("podaj spalanie l/100 km: "))
cena = 6.5

zuzycie = droga*spalanie/100
koszt = zuzycie*cena

print("zuzycie paliwa:", round(zuzycie, 2), "l")
print("koszt podrozy:", round(koszt, 2), "zl")
