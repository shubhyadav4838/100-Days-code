# Working of *args in python (Positinal Arguments)
def add(*args): # *args is a tuple of arguments passed to the function
    sum = 0
    for num in args:
        sum += num
    return sum

# print(add(1,2,4,5,6,7,8,9,5,4,3,5,6,7))

def calculate(n,**kwargs): # keywords arguments
    print(kwargs)
    n+= kwargs["add"]
    n*= kwargs["multiply"]
    print(n)
    
calculate(3,add=5, multiply=6 )

class Car: # By using the .get() fuction if the value does not exist it will return None, will not give the error
    def __init__(self,**kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
my_car = Car(make="Toyota")
print(my_car.model)