s = "malayalam"
print(s[0])
print(s[-1])
print(len(s))

st = ""
n = len(s)
for ch in range(n):
    st += s[n-ch-1]
print(st)

count = 0
for ch in s:
    if ch in "aeiou":
        count += 1
print(count)

n = len(s)
flag = True
for i in range(n//2):
    if s[i] != s[n-i-1]:
        print("it is not palindrome.")
        flag = False
        break
        
if flag : print("it is palindrome.")
