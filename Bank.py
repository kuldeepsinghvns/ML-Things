import pandas as pd


def readfromexcel():
    df = pd.read_excel("sbi.xlsx", index_col=0)
    return df


def GetBalance(accno):
    try:
        df = readfromexcel()
        x = df[['balance']]

        return x.loc[accno][0]

    except:
        return None


def deposit(accno, newBalance):
    try:
        currentBalance = GetBalance(accno)
        balance = currentBalance+newBalance
        ChangeBalance(accno, balance)
        df = readfromexcel()
        SaveToExcel(df)
        return True
    except:
        return False


def CloseAccount(accno):
    try:
        df = readfromexcel()
        df = df.drop(accno)
        print(df)
        SaveToExcel(df)
        return True
    except:
        return False


def NewAccount(accno, name, balance):
    try:
        newdata = {

            'balance': balance,
            "name": name
        }
        df = readfromexcel()
        print(newdata)
        df.loc[accno] = newdata
        print('df', df)
        SaveToExcel(df)
        return True
    except:
        return False


def ChangeBalance(accno, newbalance):
    try:
        newdata = {'accno': [accno],

                   'balance': [newbalance]
                   }
        newdata = pd.DataFrame(newdata, index=newdata["accno"])
        print(newdata)
        df = readfromexcel()
        df.update(newdata)

        SaveToExcel(df)
        return True
    except:
        return False
    
def searchaccount(accno):
    try:
        df=readfromexcel()
        x=df[['name']]
        name=x.loc[accno][0]
        balance=GetBalance(accno)
        return accno,name,balance
    except:
        return None




def SaveToExcel(df):
    df.to_excel("sbi.xlsx")


deposit = deposit(1, 500)
print(deposit)


while True:
    print("0-Exit,1-New Account,2-Deposit Balance,3-Withdrawl Account,4-Close Account,5-Search Account")
    select = int(input("Enter Number"))
    if select == 0:
        break
    elif select == 1:
        print("New Account")
        accno = int(input("Inter Account Number"))
        name = (input("Inter Your Name"))
        balance = int(input("Inter Your balance"))
        NewAccount(accno, name, balance)

        continue
        # NewAccount()
    elif select == 2:
        print("Deposit Balance")
        accno = int(input("Inter Your Account Number"))
        amount = int(input("Inter Your Amount"))
        currentbalance = GetBalance(accno)
        newbalance = amount+currentbalance
        ChangeBalance(accno, newbalance)

        continue
        # ChangeBalance()
    elif select == 3:
        print("Withdrawl Account")
        accno = int(input("Inter Your Account Number"))
        amount = int(input("Inter Your Amount"))
        currentbalance = GetBalance(accno)
        newbalance = currentbalance-amount
        ChangeBalance(accno, newbalance)
        if amount > currentbalance:
            print("Error")
        continue
        # CloseAccount()
    elif select == 4:
        print("Close Account")
        accno=int(input("Inter Your Account Number"))
        CloseAccount(accno)  
        continue
        # GetBalance()
    elif select==5:
        print("Search Account")
        accno=int(input("Inter Your Account Number"))
        
        details=searchaccount(accno)
        print(details)
        continue
    else:
        print("Invalid Number")

"""
0-Exit, 1-New Account,2-Deposit,3-Withdraw, 4-Close Account
"""

# df=readfromexcel()
# print(df)
# NewAccount(4,"Popat",500)
# CloseAccount(4)
# balance=GetBalance(4)
# print(balance)
# ChangeBalance(4, 600)
# balance=GetBalance(4)
# print(balance)
# balance=balance+500
# ChangeBalance(4,balance)
# balance=GetBalance(4)
# print(balance)


"""

x=GetBalance(3)
print(x)
x=NewAccount(4,"Champak",300)
print(x)
"""
