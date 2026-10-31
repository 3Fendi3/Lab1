import random
droga = random.randint(1, 1000)
spalanie = float(input("podaj spalanie l/100 km: "))
cena = float(input("podaj cene paliwa za litr: "))

zuzycie = droga * spalanie / 100
koszt = zuzycie * cena

print("dlugosc trasy:", droga, "km")
print("zuzycie paliwa:", round(zuzycie, 2), "l")
print("koszt podrozy:", round(koszt, 2), "zl")