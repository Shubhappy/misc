In_no = [1,8,5,20,12]
#Author: Shubham Gupta
# Convert list into tuple and then vice-versa to maintain the same input for ascending/descending order
Tup = tuple (In_no)
Ascend = list (Tup)

# code for descending order
i= 0
j=0
print ("Descending order of nos.")
while j<len (In_no):
    for i in In_no:
        print (max (In_no))
        In_no.remove( max (In_no))

# code for Ascending order
k=0
l=0
print ("")
print ("Ascending order of nos.")
while l<len (Ascend):
    for k in Ascend:
        print (min (Ascend))
        Ascend.remove( min (Ascend))