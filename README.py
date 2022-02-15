s1=int(input("enter 1st mark:"))
s2=int(input("enter 2nd mark:"))
s3=int(input("enter 3rd mark:"))
s4=int(input("enter 4th mark:"))
s5=int(input("enter 5th mark:"))


print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
print( ) 
print("Student Mark Stament")
Details=["Name:Siva", "Std:10","Age:18","Section:B"]

for a in Details:
    print(a)


total=s1+s2+s3+s4+s5

average=total/5

print("The Total Mark:",total)
print("The Average:",average)

"""
450~500 - A Grade

400~449 - B Grade

350~399 - C Grade

300~349 - D Grade

below 300 - Fail

"""

if total>=450 and total<=500:
    print ("Grade: A")
    print("Best Keep Going")
elif total<=449 and total>=400:
    print("Grade:B")
    print("Good")
elif total<=399 and total>=350:
    print("Grade: C")
    print("Good but Need Attention")
    
elif total<=349 and total>=300:
    print("Grade:D")
    
else:
    print("Fail")
