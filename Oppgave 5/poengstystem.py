poeng = 0

while True:
    valg = input("\nVelkommen!\n"
                "1: Legg til poeng\n"
                "2: Vis poeng\n"
                "3: Avslutt\n"
                "Ditt valg: ").strip()
    if valg == "1":
        poeng += int(input("Hvor mange poeng vil du legge til? "))
    elif valg == "2":
        print(f"Dine poeng: {poeng}")
    elif valg == "3":
        print("Avslutter programmet.")
        break
    else:
        print("Ugyldig valg, prøv igjen.")