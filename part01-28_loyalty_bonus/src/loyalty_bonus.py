points = int(input("How many points are on your card? "))
bonus = "15 %"
katsayi = 1.15

if points < 100:
    bonus = "10 %"
    katsayi = 1.1

puan = points * katsayi

print(f"Your bonus is {bonus}")
print(f"You now have {puan} points")