#*args 
def add (*args):
    total = 0
    for arg in args :
        total += arg
    return total
print (add(1,2,3,4,5))

#**kwargs
def aryan (**kwargs):
    for key , value in kwargs.items():
        print (f"{key} : {value}")
aryan(street ="123 Fake street",
      city = "Kangra",
      state = "HP")


#
def kaku (*args,**kwargs):
    for arg in args:
        print (arg,end = " ")
    print()
    for key , value in kwargs.items():
            print (f"{key} : {value}")

kaku("Dr.","Spongebob","squarepants",
     street ="123 Fake street",
      city = "Kangra",
      state = "HP")


#
def kaku(*args, **kwargs):
    print(" ".join(args))

    for key, value in kwargs.items():
        print(f"{key} : {value}")
kaku("Dr.","Spongebob","squarepants",
     street ="123 Fake street",
      city = "Kangra",
      state = "HP")    

if __name__=="__main__":
    kaku("Dr.","Spongebob","squarepants",
     street ="123 Fake street",
      city = "Kangra",
      state = "HP") 