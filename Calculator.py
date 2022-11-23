#Addition, substraction & multiplication for multiple inputs
numbers= list (map (int, input("Enter the nos.").split()))
summation = 0
substraction = 0
multiplication = 0
#i = 0
print ("")

#Basic functions of calculator for multiple inputs
for ele in range (0, len (numbers)):
    summation = summation + numbers [ele]
    substraction = substraction - numbers [ele]
    multiplication = multiplication * numbers [ele]
#    division = division
print ("Sum is: ", summation)
print ("Substraction is: ", substraction)
print ("Multiplication is: ", multiplication)
#print ("Division is: ", i/j)
