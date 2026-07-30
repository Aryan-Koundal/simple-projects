def add_sprinkles(func):
    def wrapper ():
        print ("YOU ADDED SPRINKLES")
        func()
    return wrapper

@add_sprinkles
def get_ice_cream ():
    print ("HERE IS YOUR ICE CREAM")

get_ice_cream()