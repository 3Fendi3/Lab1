print("Kalkulator")
operator = input("podaj operator (wpisz + - * / **): ")
a = float(input("podaj a: "))
b = float(input("podaj b: "))

if operator == "+":
    print(a + b)
elif operator == "-":
    print(a - b)
elif operator == "*":
    print(a * b)
elif operator == "/":
    if b == 0 or a == 0:
        print("nie mozna dzielic przez 0")
        exit()
    print(a / b)
elif operator == "**":
    print(a ** b)
