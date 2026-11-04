ovozlar = {"Ali": "Python", "Vali": "JavaScript", "Madina": "Python",
           "Jasur": "C++", "Aziza": "Python", "Sardor": "JavaScript"}

hisob = {}
for til in ovozlar.values():
    hisob[til] = hisob.get(til, 0) + 1

for til, soni in hisob.items():
    print(f"{til}: {soni} ta ovoz")

golib = max(hisob, key=hisob.get)
print("G'olib:", golib)