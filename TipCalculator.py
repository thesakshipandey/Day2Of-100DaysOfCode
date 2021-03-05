print("WELCOME TO THE TIP CALCULATOR")
total_bill = float(input("What was the total bill amount?\n"))
tip_input = int(input("What percentage tip would you like to give?\n"))
people = int(input("How many people would you like to split your bill with?\n"))
tip = 1 + (tip_input/100.0)
split = (total_bill/people)*tip
print(f"The final bill is {split}")
