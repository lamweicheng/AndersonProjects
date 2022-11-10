import secrets, string

letters, digits, specialChars= string.ascii_letters, string.digits, string.punctuation

#Combinations of the password can be letters, digits, characters
alphabet = letters + digits + specialChars 


#Set the length limit of the password as 12
password_length = 12 

#Empty Password String
password = ""


#Simple Password Generator without any constraints 
# for i in range (password_length):
#     password += " ". join(secrets.choice(alphabet))




#Password Generator with Constraints 
# while True:
  
#     for i in range (password_length):
#         password += "". join(secrets.choice(alphabet))
    
#     if (any(char in specialChars for char in password) and (sum(char in digits for char in password) >= 2)):
#         break


# while len(password) <= password_length:
#     password += "". join(secrets.choice(alphabet))


passwordlist = []

while True:

    for i in range (0, 12):
        password += "".join(secrets.choice(alphabet))
    
    passwordlist.append(password)

    if len(passwordlist) == 3:
        break    

print(passwordlist)

