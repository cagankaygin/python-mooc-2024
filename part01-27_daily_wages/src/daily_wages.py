wage = float(input("Hourly wage"))
hour = int(input("Hours worked"))
day = input("Day of the week")
dw = hour * wage
if day == "Sunday":
    dw *= 2
print(f"Daily wages: {dw} euros")