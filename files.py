register_you = input("Please register yourself:")
with open("register.txt", "a") as file:  
    file.write(register_you)
    


with open("register.txt", "r") as file:
    content = file.read()
print(content)     