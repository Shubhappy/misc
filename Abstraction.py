#Program for abstraction, Function created for calculation
def calculation():
    def add():
        print(x+y)
    def substraction():
        print(x-y)
    def multiplication():
        print(x*y)
    def division():
        print(x/y)
    if sign=="+":
        add()
    elif sign=="-":
        substraction()
    elif sign=="*":
        multiplication()
    else:
        division()
x=int(input("Enter the first no.: ")) #End User can only see the message and input the data here
y=int(input("Enter the first no.: ")) #End User can only see the message and input the data here
sign = (input("Please press + for addition, - for substraction, * for multiplication and / for division: ")) #End User can only see the message and input the data here
calculation()