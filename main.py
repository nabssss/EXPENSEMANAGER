from logic import expense,fetchData
print("EXPENSE WALLET SYSTEM")
flaf = True
while True:
    print("press 'A' to add:\npress 'V' to view the status")
    userchoice = input("please enter your choice: ")
    if userchoice == 'A' or userchoice == 'a':
        data = expense()
    elif userchoice == 'V' or userchoice == 'v':
        newdata = fetchData()
        print(newdata)
    else:
        print("invalid key plz try again!!1..")
