Tuple = list (map (int, input("Enter the nos.").split()))
print (Tuple)
total = 0
for ele in range (0, len (Tuple)):
    total = total + Tuple [ele]
        
print ("Sum: ", total)
