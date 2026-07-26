
def show_balance ():
    print (f"Current Balance ${Balance}")

def deposit (balance):
    dep = int (input("Entre the amount you want to Deposit\n$"))
    balance += dep
    print (f"Now your Balance is {balance}") 
    return balance

def withdraw (balance):
    draw = int (input ("Entre the amount you want to Withdraw\n$"))
    if draw > balance:
        print (f"Not enough balance!")
        return balance
    balance -= draw
    print (f"Your remaining Balance is ${balance}")
    return balance

Balance = 0

while True :
    print ("-------Banking System--------")
    print ("1. Show Balance ")
    print ("2. Deposit Amount")
    print ("3. Withdraw Amount")
    print ("4. Exit")
    choice = int (input("Entre your choice 1-4\n"))
    if choice == 1 :
        show_balance()

    elif choice == 2 :
        Balance =deposit(Balance)

    elif choice == 3 :
       Balance = withdraw(Balance)

    elif choice == 4 :
        print ("Thank you for using Banking System")
        break

    else :
        print ("invalid choice , please entre a number between 1-4")
        