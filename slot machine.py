print ("*******************************")
print ("Welcome to Slot Machine")
print ("Numbers : 1 , 2 , 3 ")
print("********************************")
print ("--------Rules--------")
print ("IF you get 3 same numbers you Won and gets double money")
print ("IF you get 2 same numbers you almost Won and get half money back ")
print ("IF you get non same number YOU LOST ")
print ("First deposit some Balance to play")

Balance = 0
def show_balance (balance):
    print (f"Current Balance : {balance}")

def deposit (balance):
    dep = int(input("Entre the amount you want to Deposit"))
    balance += dep
    return balance

def withdraw (balance):
    draw = int(input("Entre the amount you want to Withdraw"))
    if draw > balance:
       print ("Not enough Balance")
       return balance
    balance -= draw
    return balance

while True :
    print ("1. Show Balance")
    print ("2. Deposit Amount")
    print ("3. Withdraw Amount")
    print ("4. Play")
    choice = int (input("Entre your choice 1-4\n"))
    if choice == 1 :
        show_balance(Balance)
    elif choice == 2 :
        Balance =deposit(Balance)

    elif choice == 3 :
       Balance = withdraw(Balance)

    elif choice == 4 :
        print ("Now the real game starts")

    elif choice == 5 :
       print ("You have quit the game")
       break
    else:
        print ("choose between 1-4")


    if Balance < 10 :
     print ("Insufficient Balance")
     exit()
    a = input("Betting amount is $10 , type Yes to play and No to quit :\n").lower()
    if a == "yes":
     print ("Continuing")
 
    elif a == "no":
      print("U had quit the game.")
      exit()
    else :
      print ("Invalid input.")
   
    
    print ("spinning")

    import random 
    x = random.randint(1,3)
    y = random.randint(1,3)
    z = random.randint(1,3)
    if Balance < 10 :
     print ("insufficient Balance, Deposit some Balance")
     exit()
    else :
      if x == y == z :
       print ("You Won")
       Balance +=20
      elif x == y or y == z or z == x :
          print ("You almost won")
          Balance += 5
      else :
          print ("YOU Lost")
          Balance -=10
      print (f"{x}-{y}-{z}")
      print (f"Your new balance : {Balance}")
      