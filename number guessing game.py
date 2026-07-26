import random
number = random.randint(0,10)
print ("Computer has given you a number now you have to guess the number between 0-10")
print ("YOU only get 3 chances")
for user in range (3): 
    user = int(input("guess the number\n"))
    if user == number:
        print ("You won")
        break
    elif user >= number:
        print ("Choose a smaller number")
    elif user <= number:
        print ("Choose a bigger number")