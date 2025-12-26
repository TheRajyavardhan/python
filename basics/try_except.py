## First Function 
# num1 = int(input("Enter the Divisor: "))
# num2 = int(input("Enter the Dividend: "))
# try:
#     result = num2//num1
# except ValueError:
#     print("Invalid input")
# except ZeroDivisionError:
#     print("Divison by zero --invalid")
# else:
#     print("Ans is: ",result)
# finally:
#     print("Execution done")

## Second Function 

# def check_age(age):
#     if age<18:
#           raise ValueError("Age under 18")
#     else:
#         print("Age: ",age)

# age = int(input("Enter the age: "))
# try:
#     check_age(age)
# except ValueError as e:
#     print(e)


nums = {1:"one",2:"two",3:"three",4:"four"}
try:
    value = nums[5]
except :
    value = None

print(value)
