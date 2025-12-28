# file = open("data.txt","w")
# file.write("Hello Python\n")
# file.write("File handling started\n")
# file.close() #not close file != no file save

# file = open("data.txt","r")
# for line in file: ## file reading line by line
#     print(line.strip())
# file.close()
# content = file.read() ## reading as whole
# print(content)
# file.close()

# with open("data.txt","w") as file: ## professional way
#     file.write("Safe writing\n")

# with open("data.txt","a") as file:
#     file.write("New line added\n") ## won't erase earlier data stored in file "data.txt"

try:
    with open("data.txt","r") as file:
        print(file.read())
except FileNotFoundError:
    print("file does not exist")
    
    