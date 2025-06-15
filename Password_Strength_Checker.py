
'''
Build a tool that assesses the strength of a password based on criteria such as length, presence of uppercase and
lowercase letters, numbers, and special characters. Provide feedback to users on the password's strength.
'''

import string

password = input("Enter the password : ")

# print(string.ascii_uppercase)
# print(string.ascii_lowercase)
# print(string.punctuation)
# print(string.digits)

upper_Case = any( [1 if i in string.ascii_uppercase else 0 for i in password] )  # 1 indicate Upper-Case Letter , 0 indicate Lower-Case Letter
# print(upper_Case)
lower_Case = any( [1 if i in string.ascii_lowercase else 0 for i in password] )
# print(lower_Case)
special_Characters = any( [1 if i in string.punctuation else 0 for i in password] )
# print(special_Characters)
digital_Characters = any( [1 if i in string.digits else 0 for i in password] )
# print(digital_Characters)

symbols = [ upper_Case , lower_Case , special_Characters , digital_Characters ]

password_Length = len(password)
score = 0

with open("common_password.txt" , "r") as file:
    common_Passwords = file.read().splitlines()

if password in common_Passwords:
    print("Password was found in common password list. Score : 0 / 7")
    exit()

if password_Length > 8:
    score += 1

if password_Length > 12:
    score += 1

if password_Length > 17:
    score += 1

if password_Length > 20:
    score += 1

if password_Length > 24:
    score += 1

if password_Length > 28:
    score += 1

if password_Length > 32:
    score += 1

print(f"Password length is {str( password_Length )}, adding {str(score)} points!")

if sum(symbols) > 1:
    score += 1
if sum(symbols) > 2:
    score += 1
if sum(symbols) > 3:
    score += 1

print(f"Password has {str(sum(symbols))} different symbols types, adding {str(sum(symbols)-1)} points!")

if score < 4:
    print(f"The password is quite weak! Score : {str(score)} / 7")
elif score == 4:
    print(f"The password is ok! Score : {str(score)} / 7")
elif score > 4 and score < 6:
    print(f"The password is pretty good! Score : {str(score)} / 7")
elif score > 6:
    print(f"The password is strong! Score : {str(score)} / 7")
