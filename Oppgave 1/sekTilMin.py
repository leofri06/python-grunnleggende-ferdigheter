sekunder = int(input("Skriv inn antall sekunder: "))
minutter = sekunder // 60
resterendeSekunder = sekunder % 60

print(f"{sekunder} sekunder er {minutter} minutter og {resterendeSekunder} sekunder.")