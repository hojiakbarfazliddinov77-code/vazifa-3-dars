baholar = {"Ali": 85, "Vali": 72, "Madina": 96, "Jasur": 68}

yuqori = [f"{ism} — {ball}" for ism, ball in baholar.items() if ball >= 90]
ortacha = sum(baholar.values()) / len(baholar)

print("Yuqori ball olganlar:", ", ".join(yuqori))
print("O‘rtacha ball:", ortacha)