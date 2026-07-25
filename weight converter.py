weight = float(input("entre your weight\n"))
unit = input ("kg or gm\n")
if unit == "gm" :
    gm = weight / 1000
    print (f"your weight in kg is {gm} kg")
elif unit == "kg" :
    kg = weight * 1000
    print (f"your weigth in gm is {kg} gm")
else :
    print (f"{unit} was not valid") 