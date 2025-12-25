student = {"dev":34, "mohit":78, "rohit":67, "gargi":65, "ganesh":93}
print("Keys : ")
for i in student.keys():
         print(i)
print("Values: ")
for i in student.values():
         print(i)
maxMark = 0
topper = ""
for k,v in student.items():
    if maxMark<v:
        maxMark = v
        topper = k
print("topper is: ",topper)  
s = "Hindustan"
freq = {}
for i in s:
    if i in freq.keys():
         freq[i]+=1
    else:
          freq[i] = 1
print("frequency of character: ",freq)

arr = [1,5,5,6,8,4,7,9,2,3,3,]
test_set = set(arr)
print("test_set: ",test_set)
test_set2 = {10,11,12,13,14,15,1}
print("union of 2 set: ",test_set | test_set2)
print("Intersection of 2 set: ",test_set & test_set2)
print("Difference of 2 set: ",test_set - test_set2)

