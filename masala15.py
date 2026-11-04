birinchi = {"Ali", "Madina", "Jasur", "Aziza"}
ikkinchi = {"Jasur", "Sardor", "Aziza", "Bekzod"}

faqat_birinchi = birinchi - ikkinchi
faqat_ikkinchi = ikkinchi - birinchi
ikkalasida = birinchi & ikkinchi

print("Faqat birinchi:", ", ".join(sorted(faqat_birinchi)))
print("Faqat ikkinchi:", ", ".join(sorted(faqat_ikkinchi)))
print("Ikkalasida:", ", ".join(sorted(ikkalasida)))