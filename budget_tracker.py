import json
import datetime
from pathlib import Path
print("----------------------------------")
print("Welcome in the Budget Tracker 1.0")
print("----------------------------------\n")



def addIncome():
    global userAccountBalance
    income = float(input("Provide income to add: "))
    userAccountBalance = userAccountBalance + income
    print("| Your current account balance is: {:.2f} |".format(userAccountBalance))
    print("\nChoose which operation would you like to perform (type option number and click Enter):")
    incomes.append("+" + str(income))

def subExpense():
    global userAccountBalance
    expense = float(input("Provide expense to subtract: "))
    userAccountBalance = userAccountBalance - expense
    print("| Your current account balance is: {:.2f} |".format(userAccountBalance))
    print("\nChoose which operation would you like to perform (type option number and click Enter):")
    expenses.append("-" + str(expense))
    
def showBalance():
    print("| Your current account balance is: {:.2f} |".format(userAccountBalance))
    print("\nChoose which operation would you like to perform (type option number and click Enter):")


def exitProgram():
    global userAccountBalance
    time = datetime.datetime.now()
    save = {"Date": str(time.strftime("%Y-%m-%d %X")),
             "Start Balance": startBalance,
             "End Balance": userAccountBalance,
             "Account Balance": userAccountBalance,
             "Operations": {"Incomes":incomes, "Expenses":expenses}
            }
    with open("budget_tracker.json", "r") as file:
        jsonList = json.load(file)
        jsonList.append(save)
    with open("budget_tracker.json", "w") as file:
        json.dump(jsonList, file, indent=4)
    exit()

def convert(string):
    numericString = ""
    for character in string:
        if character.isnumeric():
            numericString += character
        elif character == ",":
            numericString += "."
        elif character == ".":
            numericString += character
    numericString = "{:.2f}".format(float(numericString))
    return float(numericString)

options = {
    1:("Add income", addIncome),
    2:("Subtract expense", subExpense),
    3:("Show account balance", showBalance),
    4:("Exit", exitProgram)
}

incomes = []
expenses = []

file_path = Path('budget_tracker.json')

if file_path.exists():
    with open('budget_tracker.json', 'r') as file:
        jsonList = json.load(file)
        userAccountBalance = float(jsonList[-1]["Account Balance"])
        startBalance = userAccountBalance

else:
    startBalance = 0
    userAccountBalance = convert(input("At first, please provide your account balance: "))
    with open("budget_tracker.json", "w") as file:
        json.dump([], file)


print("| Your account balance is currently: {} |".format(userAccountBalance))

print("\nChoose which operation would you like to perform (type option number and click Enter):")

while True:
    print("1.Add income \n" + "2.Add expense \n" + "3.Show account balance \n" + "4.Exit")

    userChoice = input("-> ")
    if userChoice.isnumeric():
        userChoice = int(userChoice)
        if userChoice in options:
            print("\nYou chose option number {} -> {}".format(userChoice, options[userChoice][0]))
            options[userChoice][1]()
        else:
            print("\nYou chose option that doesn't exist. Please choose a correct option:")
    else:
        print("\nIncorrect input. Type number of option without any additional symbols.")