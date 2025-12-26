nums = [1,2,3,4]

square = list(map(lambda x: x*x,nums))
print(square)

evens = list(filter(lambda x: x%2 == 0, nums))
print(evens)

from functools import reduce 
total = reduce(lambda a,b: a+b, nums)
print(total)

result = list(map(lambda x:x*x,filter(lambda x:x%2 == 0,nums)))
print(result)