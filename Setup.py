import time 
import os
import sys
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

print("""
.d8888.  .d8b.  db    db db    db  .d8b.     .d88b.  .d8888. 
88'  YP d8' `8b 88    88 88    88 d8' `8b   .8P  Y8. 88'  YP 
`8bo.   88ooo88 Y8    8P Y8    8P 88ooo88   88    88 `8bo.   
  `Y8b. 88~~~88 `8b  d8' `8b  d8' 88~~~88   88    88   `Y8b. 
db   8D 88   88  `8bd8'   `8bd8'  88   88   `8b  d8' db   8D 
`8888Y' YP   YP    YP       YP    YP   YP    `Y88P'  `8888Y' 
""")

print(Fore.GREEN + "Welcome new user, Please go through the Setup Page to get Started \n or if you already have a accout you can Continue to Login as normal!")

# setup 
print("""
[1] Continue with Setup
[2] I Have already done the Setup 
""")

# ON EXECUTE (When debug ran) some minor errors with l_p and l_n (**name l_p and l_n are not defined**) <-- option 2

# option 1 
setup = input("/Setup#> ")
if setup =='1':
    name = input(str("Please Enter your display name: "))   # When picking option 2 error says "name is not defined"
    pas = input(str("Please Enter your new Password to Login: ")) 
with open('data/username.pass', 'w') as f:
    f.writelines(name)

with open('data/password.pass', 'w') as f:
    f.writelines(pas)
    print("Setup Complete!")
    print(Fore.RED + "Username and Password changed successfully!\n")
    input(Fore.RED + "Press the Enter key to close this prompt!")
    
# option 2 (reads and checks data folder for correct login info)
if setup == '2':
    login_name = open('data/password.pass')
    login_pas = open('data/username.pass')
    l_p = login_pas.read()
    l_n = login_name.read()

# Login system for option 2
while True:
    login = input(str("Please Enter the Password To" + l_n + ": "))
    if login == l_p:
        os.startfile("Home.py")
        break
    else:
        print("Wrong Password!")