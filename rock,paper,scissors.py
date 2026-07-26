import random
choices = ["rock","paper","scissors"]
while True:
 user = input ("choose one (Rock , Paper , Scissors)\n").lower()   
 if user not in choices:
      print (f"invalid choice {user}. try again!")
      continue
 computer = random.choice(choices)  
 print(f"you choose: {user}")
 print (f"computer choose: {computer}")
 if user == computer:
  print ("match is tied")
 elif (user == "rock" and computer == "paper" ,
   user == "paper" and computer=="rock",
   user == "scissors" and computer=="paper"):
   print ("you won")
 else:
  print ("computer won")

 play_again = (input("Do you want to play again (Yes/No)\n")).lower()
 if play_again != "yes":
  print ("Thanks for playing")
  break
 
print ()
