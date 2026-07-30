try:
    number = int(input("Entre 1st Number:"))
    numb = int(input ("Entre 2nd Number"))
    print (number/numb)
except ZeroDivisionError:
    print ("You cannot divide by zero")
except ValueError:
    print ("Entre only numbers")
except Exception:
    print ("Something went wrong")