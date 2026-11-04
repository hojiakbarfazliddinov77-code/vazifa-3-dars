harorat = (18, 20, 17, 23, 25, 21, 19)

yuqori_haroratlar = []
kunlar_soni = 0

for h in harorat:
    if h > 20:
        yuqori_haroratlar.append(h)
        kunlar_soni += 1

harorat_str = ", ".join(map(str, yuqori_haroratlar))

print(f"Haroratlar: {harorat_str}")
print(f"Kunlar soni: {kunlar_soni}")