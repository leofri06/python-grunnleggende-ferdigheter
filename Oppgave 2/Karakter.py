# Siden vi har gjort den, tok jeg koden fra forrige gang, og gikk over for å se etter forbedringer.

# Regler:
# - under 35 = 1
# - 35-49 = 2
# - 50-64 = 3
# - 65-79 = 4
# - 80-90 = 5
# - 91-100 = 6

while True:    
    poengsum = int(input("Skriv inn poengsummen din (0-100):\n").strip())

    if poengsum < 0 or poengsum > 100:
        print("\nIkke gyldig inndata, prøv igjen")
    elif poengsum >= 91:
        print("\nDu fikk karakter 6.")
        break
    elif poengsum >= 80 and poengsum <= 90:
        print("\nDu fikk karakter 5.")
        break
    elif poengsum >= 65 and poengsum <= 79:
        print("\nDu fikk karakter 4.")
        break
    elif poengsum >= 50 and poengsum <= 64:
        print("\nDu fikk karakter 3.")
        break
    elif poengsum >= 35 and poengsum <= 49:
        print("\nDu fikk karakter 2.")
        break
    else: # under 35
        print("\nDu fikk karakter 1.")
        break
