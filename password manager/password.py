master_pwd = input("What is the master password? ")

def view():
    with open("password.txt", 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("user:", user, "| Password:", passw)
            

def add():
    name = input("Account name: ")
    pwd = input("password: ")
    
    with open("password.txt", 'a') as f:
        f.write(name + "|" + pwd + "\n")
    
    print(name + " account added")
while True:
    mode = input("Would you like to add a new password or view existing ones (view, add)")
    if mode == "q":
        break
    
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue