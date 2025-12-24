for i in range(1,11):
    print(i);

for i in range(2,21,2):
    print(i);

n = int(input("Enter the number: "))
total = 0;
for i in range(1,n+1):
    total+=i;
print("Total: ",total)
m = int(input("Enter the table number: "))
for i in range(1,11):
    print(m," x ",i," = ",m*i);
    

