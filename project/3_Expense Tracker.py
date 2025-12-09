# ------------------------------------------------
# Expense Tracker
# ------------------------------------------------
import json
Expenses =[]
print("Welcome to Expense Tracker :")


while True:
    print("\n============Menu=========")
    print("1.Add Expense")
    print("2.View all Expense ")
    print("3.View total Spending")
    print("View spending by Category")
    print("5.Exit")
    print("=============================")
    
    choice = input("Enter your choice (1-5):")
    
    # 1 Add Expense
    if (choice=='1'):
        date =input("Enter date  (DD-MM-YYYY): ")
        category =input("Enter Category (food ,Travel ,shopping ,etc): ")
        description =input("Enter short desciption :")
        Amount =float(input("enter amount : "))


        Expense ={
            "date":date,
            "category":category,
            "description":description,
            "Amount":Amount
        }
        Expenses.append(Expense)
        print("\n Expense added Succesfully !")

    # View all expense
    elif    choice=="2":
        if len(Expenses) == 0:
            print("\n No expense recorded yet.")
        else :
            print("\n ---- All Expense -----")
            i =1
            for e in Expenses:
                print(f"{i}.{e["date"]} | {e["category"]} |{e["description"]} | {e["Amount"]}")
                i+=1
                print("-----------------------------------------------")


    #3. View Total Spending 
    elif choice == "3":
        total =0
        for e in Expenses:
            total += e["Amount"]
        print(f"\n Total Spending = {total}")
    
    # 4. Spending by Category 
    elif choice == "4":
        if len(Expenses) == 0:
            print("\n No Expenses recorded yet .")
        else:
            summary ={}
            for e in Expenses:
                cat = e["category"]
                if( cat in summary):
                    summary[cat] += e["Amount"]
                else :
                    summary[cat] = e["Amount"]
            print("\n Spending by Category :")
            for cat ,amt in summary.items():
                print(f"{cat}:{amt}")
            
            
    # 5Exit
    elif choice == "5":
        print("\n  Thanks for using Expense Tracker ! Bye !")
        break
    else:
        print("\n Invalid choice . Please try again .")    




# Save
with open("expenses.png", "w") as f:
    json.dump(Expenses, f)

# Load
with open("expenses.png", "r") as f:
    Expenses = json.load(f)