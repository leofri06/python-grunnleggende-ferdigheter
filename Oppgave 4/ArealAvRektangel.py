def Areal(lengde, bredde):
    return lengde * bredde

lengde = int(input("Skriv inn lengden på rektangelet: "))
bredde = int(input("Skriv inn bredden på rektangelet: "))
print(f"Arealet av rektangelet er {Areal(lengde, bredde)}")
