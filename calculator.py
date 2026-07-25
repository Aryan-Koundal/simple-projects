number1 = float(input("entre an number"))
operator= input("entre an operator ( + - * / )")
number2 = float(input("entre an number"))
if operator == "+" :
 print (number1 + number2)
elif operator == "-":
 print (number1-number2)
elif operator == "*":
 print (number1*number2)
elif operator == "/":
 if number2 !=0 :
  print (number1/number2)
else :
 print ("invalid operator !")