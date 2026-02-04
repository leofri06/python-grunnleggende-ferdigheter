x = 0
totalSum = 0

print("Skriv inn karakterene dine (eller 'stopp' for å avslutte): ")
while True:
    tall = input(": ").strip()
    if tall.lower() == 'stopp':
        break
    elif int(tall) < 0 or int(tall) > 6:
        print("Karakteren må være mellom 0 og 6, prøv igjen.")
        continue
    x += 1
    totalSum += int(tall)
    snitt = totalSum / x
print(f"Snittet ditt er {snitt}")