cafe = int(input("How many times a week do you eat at the student cafeteria?"))
lunch = float(input("The price of a typical student lunch?"))
gros = float(input("How much money do you spend on groceries in a week?"))
cunch = cafe * lunch 
print(f"Average food expenditure:")
print(f"Daily: {(cunch + gros) / 7} euros" )
print(f"Weekly: {cunch + gros} euros")