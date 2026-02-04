antall = int(input("Hvor mange tall vil du summere? "))
totalSum = 0

for x in range(antall):
    tall = int(input(f"Skriv inn tall nummer {x + 1}: "))
    totalSum += tall
print(f"Summen av tallene er: {totalSum}")