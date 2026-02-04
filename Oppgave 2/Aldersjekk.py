# Regler: 
# - under 13 = Barn
# - 13-17 = Ungdom
# - 18+ = Voksen

alder = int(input("Skriv inn alderen din: "))
if alder < 13:
    print("Du er et barn.")
elif alder >= 13 and alder <= 17:
    print("Du er en ungdom.")
else:
    print("Du er en voksen.")
