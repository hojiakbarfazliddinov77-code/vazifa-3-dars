shaharlar = {"Toshkent": 3000000, "Farg‘ona": 300000, "Samarqand": 600000}

katta = [shahar for shahar, aholi in shaharlar.items() if aholi > 500000]
eng_kop = max(shaharlar, key=shaharlar.get)

print("500 000 dan ko'p:", ", ".join(katta))
print("Eng ko'p aholi:", eng_kop)