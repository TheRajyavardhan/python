import function # user made module
print(function.factorial(5))

import math  # inbuilt module
print(math.sqrt(16))

from math import sqrt, pi # importing specific file
print(sqrt(25),pi)

import math as m # making file alias for use
print(m.factorial(4))

import random 
print(random.randint(1,10))
print(random.choice([1,2,3]))

from datetime import datetime
print(datetime.now())

