import datetime

def getexpense():
    choice = 'y'
    totalexpense = []
    while True:
        if choice == 'n':
            break
        elif choice == 'y':
            amount = input(">>>Enter Expense Amount: ")
            remark = input(">>>Enter Expense Remark: ")
            totalexpense.extend([amount, remark])
            choice = input(">>>Do you want to enter more expense(y/n):")
    return totalexpense


def pushdata(id, value):  # if we store it in list it could be[['2020', '02', '21'], ['hghj', '766', 'hjghjg', '877']]
    list_of_expense = {

    }
    dictdata = {id[0]: {id[1]: {id[2]: [value]}}}  # we use this to want our list in this format
    list_of_expense.update(dictdata)  # {'2020': {'02': {'21': ['tinda', '67']}}}
    saveData(list_of_expense)


def saveData(listofExpense):  # this is to append and write our data
    fopen = open('expense.txt', 'a')
    fopen.write(str(listofExpense) + '\n')
    fopen.close()


def expense():
    dummydata = getexpense()
    # print(dummydata)
    date = str(datetime.date.today())
    key = date.split('-')
    data = [key, dummydata]
    saveData = pushdata(key,dummydata)
    return saveData


def fetchData():  # this is used when we need to read the data
    fopen = open('expense.txt', 'r')
    data = fopen.read()
    fopen.close()
    return data
