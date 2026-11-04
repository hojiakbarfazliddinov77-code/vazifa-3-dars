A = (3, 7)
B = (8, 2)

yigindi_A = sum(A)
yigindi_B = sum(B)

print(f"A yig'indisi: {yigindi_A}")
print(f"B yig'indisi: {yigindi_B}")

if yigindi_A > yigindi_B:
    print("A yigindisi katta", {yigindi_A})
elif yigindi_B > yigindi_A:
    print("B yigindisi katta", {yigindi_B})
else:
    print("Yig'indilar teng")