nums = [1,2,3,4,5]
total = 0
minNum = float('inf')
maxNum = -float('inf')
for i in nums:
    print(i)
    total += i
    minNum = min(i,minNum)
    maxNum = max(i,maxNum)
print("Total sum of nums: ", total)
print("Minimum of nums: ",minNum)
print("Maximum of nums: ",maxNum) 
newNum = int(input("Enter your Number: "))
nums.append(newNum)
print("Modified list: ",nums)
rev = []
for i in range(len(nums)-1,-1,-1):
    rev.append(nums[i])
print("reverse list: ",rev)

t = tuple(nums)
print(t)