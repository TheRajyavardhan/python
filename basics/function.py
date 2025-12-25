def factorial(num):
    if num == 0: return 1
    i = num
    fact = 1
    while i != 0:
        fact *= i
        i -= 1
    return fact 
 

def listFunction(arr):
    total = 0
    minNum = float('inf')
    maxNum = -float('inf')
    for i in arr:
        total += i
        minNum = min(i,minNum)
        maxNum = max(i,maxNum)
    return total, minNum, maxNum


def primeCheck(num):
    if num <= 1: return False
    for i in range(2,(num*0.5) + 1):
        if num%i == 0:
           return False
    return True


def countVowels(string,count=0):
    for i in string:
        if i in "aeiou":
            count+=1
    return count       

print(factorial(5))
total,minNum,maxNum = listFunction([1,2,3,5,6,8,9])
print("Total: ",total,"\nMinimum: ",minNum,"\nMaxmum: ",maxNum)
print(primeCheck(21))
name = "Mohit"
print(countVowels(name))