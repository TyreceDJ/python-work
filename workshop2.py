csx = {
    "mp1": "hardware",
    "mp2": "skinny pi",
    "mp3": "python basics",
    "mp4": "advance OOP"
}

while_num = 10

for i in csx:
    print(f"{i} {csx[i]}")

while while_num > 0:
    print(while_num)
    while_num = while_num - 1
    
revenue = int(input("How much did your product make? "))

is_yes = True
while is_yes:
    response = input("HOw much did your roduct earn in revenue?: ")
    if (reponse = input("Does yur business have any expenses to add?(Y/N): ")
    if (response == "Y"):
        new_expense = int(input("Enter expense: "))
        expenses = expenses + new_expense
    else:
        is_yes = False

profit = revenue - expenses
print(f"Your product had ${revenue:.2f} in revenue, ${expenses:.2f} in total expenses, and a profit of ${profit:.2f}")