nums = [4,5,6,7,8,9,10]

cube = list(map(lambda x:x*x*x,nums))
print(cube)

multipleof3 = list(filter(lambda x: x%3==0,nums))
print(multipleof3)

from functools import reduce 
Totalproduct = reduce(lambda a,b: a*b, nums)
print(Totalproduct)

strList = ["Devansh","Mohit","Sonu","Sid","Prarambh","Vaibhav"]
result = list(filter(lambda x: len(x)>4, strList))
print(result)