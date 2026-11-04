jami = 0
sanoq = 0

while True:
    xarajat = int(input())
    
    if xarajat == 0:
        break
        
    jami += xarajat
    sanoq += 1

ortacha = jami / sanoq

if sanoq > 0:
    print(f"Jami: {jami}")
    print(f"Kiritilgan xarajatlar soni: {sanoq}")
    print(f"O'rtacha: {ortacha:.2f}")
else:
    print("Xarajatlar kiritilmadi.")