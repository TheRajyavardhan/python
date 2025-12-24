x = int(input("Enter the number: "))
if x > 0:
    print("positive number")
elif x < 0:
    print("negative number")
else: 
    print("Zero")

marks = int(input("Enter your marks: "))
if marks<40: 
    print("fail")
else: 
    print("pass")


year = int(input("Enter the current year: "))
if year%4==0 and year%100!=0 or (year%400 == 0) :
    print("it is leap year.")
else:
    print("it is not leap year.")