def factorial(num):
    if num<=1: return 1
    return num*factorial(num-1)

def printNum(num):
    if num == 0: return 
    print(num)
    printNum(num-1)
    return 

def sumOfdigit(num):
    if num == 0: return 0
    n = sumOfdigit(num//10)
    return num%10+n

def is_palindrome(s):
    if len(s) <= 1: return True
    s = "".join(s.split())
    if s[0]!=s[-1]: return False
    return is_palindrome(s[1:-1])
print(is_palindrome("nurses run"))
