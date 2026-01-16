user=str(input("Enter username: "))
Password=int(input("Enter password: "))

if user == "Admin" and Password == 1234:
   print("Login Successful")
elif user =="Admin" and Password != 1234:
   print("Incorrect Password")  
elif user !="Admin" and Password == 1234:
   print("Incorrect Username")     
else:
    print("Login Failed") 