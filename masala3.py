zaxira = 12

while zaxira > 0:
    sotildi = int(input("Sotildi: "))
    
    if sotildi > zaxira:
        print(f"Xato! Omborda atigi {zaxira} ta daftar qolgan.")
        continue
        
    zaxira -= sotildi
    print(f"Qoldi: {zaxira}")

print("Ombor bo'sh")