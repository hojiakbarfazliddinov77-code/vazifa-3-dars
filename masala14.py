ruxsat = {"matematika", "ingliz", "informatika", "fizika"}
tanlangan = {"ingliz", "informatika", "tarix"}

ruxsat_etilgan = tanlangan & ruxsat
ruxsat_etilmagan = tanlangan - ruxsat

print("Ruxsat etilgan:", ", ".join(sorted(ruxsat_etilgan)))
print("Ruxsat etilmagan:", ", ".join(sorted(ruxsat_etilmagan)))