storst = 0
for x in range(2):
    tall = int(input(f"Skriv inn tall nummer {x + 1}: "))
    if tall > storst:
        storst = tall
print(f"Det største tallet er: {storst}")