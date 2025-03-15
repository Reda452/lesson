#class creation
class myClass:

    # private variable
    __privatevar = 27

    # private method
    def privMeth(self):
        print("I'm inside class myClass")

    # Function to print value of private variable
    def hello(self):
        print("Private Variable value: ",myClass.__privatevar)

# object creation and method call
foo = myClass()
foo.hello()
foo.__privMeth()