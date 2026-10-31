import random
droga = random.randint(1, 1000)
spalanie = float(input("podaj spalanie l/100 km: "))
cena = float(input("podaj cene paliwa za litr: "))

zuzycie = round(droga * spalanie / 100,2)
koszt = round(zuzycie * cena,2)

print(f"dlugosc trasy: {droga} km")
print(f"zuzycie paliwa: {zuzycie} l")
print(f"koszt podrozy: {koszt} zl")