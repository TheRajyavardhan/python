#Dictionary
student = {
    "name" : "Mohit",
    "age" : 21,
    "course" : "BCA"
}
# #name, age, course, city are keys.

# print(student["name"])
# student["age"] = 22
# student["city"] = "Delhi"
# print(student.get("marks","Not found"))

# for key in student:
#     print(key, student[key])

# for key, value in student.items():
#     print(key, value)

# for i in student.keys():
#     print(i)
# for i in student.values():
#     print(i)
# student.items()
# student.pop("age")
# for key, value in student.items():
#     print(key, value)

# s = "programming"
# freq = {}

# for ch in s:
#     if ch in freq:
#         freq[ch]+=1
#     else:
#         freq[ch] = 1
# print(freq)

a = {1,2,3}
b = {3,4,5}

print(a | b) #union
print(a & b) #intersection
print(a - b) #difference 