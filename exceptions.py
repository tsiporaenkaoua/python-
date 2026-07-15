try:
    x = int(input("Nombre : "))
    print(10 / x)

except ValueError:
    print("Tu dois entrer un nombre")

except ZeroDivisionError:
    print("Division par zéro impossible")