import time 
import os 
import socket
import colorama
from colorama import Fore, Back, Style
from colorama.initialise import reset_all
colorama.init(autoreset=True)


login_name = open("data/password.pass")
login_pas = open("data/username.pass")
l_p = login_pas.read()
l_n = login_name.read()

print("""
.d8888.  .d8b.  db    db db    db  .d8b.     .d88b.  .d8888. 
88'  YP d8' `8b 88    88 88    88 d8' `8b   .8P  Y8. 88'  YP 
`8bo.   88ooo88 Y8    8P Y8    8P 88ooo88   88    88 `8bo.   
  `Y8b. 88~~~88 `8b  d8' `8b  d8' 88~~~88   88    88   `Y8b. 
db   8D 88   88  `8bd8'   `8bd8'  88   88   `8b  d8' db   8D 
`8888Y' YP   YP    YP       YP    YP   YP    `Y88P'  `8888Y' 
""")

print("Welcome back " + l_n)
print(Fore.YELLOW + "The Current Date is: " + time.strftime("%m/%d/%y"))

time.sleep(0.7)
print("""
[1] To open search engine
[2] To open Text Editor
[3] To open File Explorer
[4] To Configure or open BIOS
[5] Terminal 
[6] Games
[7] Exit \n""")

# controls select options above
select = input("/~# ")
if select == '1':
    os.startfile('Browser.py')

if select == '2':
    os.startfile('Editor.py')

if select == '3':
    os.startfile('fileExpl.py')

# Yes I know This is a mess
if select == '4':
      while True:
        b_login = input(str("Please Enter the Password To " + l_n + " To open BIOS: ")) 
        
        # user opens BIOS when prompted 
        if b_login == l_p:
          print(Fore.CYAN + "Opening BIOS...")
          host_name = socket.gethostbyname()
          host_ip = socket.gethostbyname(host_name)
          print("[1] USER NAME: " + l_n)
          print("HOST NAME: ", host_name)
          print("LOCAL IPS: " + host_ip)
          edit_b = input("Enter [?] To change settings: ")

        # change username prompt
        if edit_b == '1':
            edit_n = input("Please Enter a new username: ")
            with open("username.pass", 'w') as f:
              f.writelines(edit_n)
              print("Username changed to " + edit_n)
              input(Fore.RED + "Press Enter to close this prmopt\n") 

        # change password prompt
        if edit_b == '2':
            edit_p = input("Enter a new Password: ")
            with open("Password.pass", 'w') as f: 
              f.writelines(edit_p)
              print(Fore.GREEN + "Password changed Successfully")
        else:
              print(Fore.RED + "Wrong password to " + l_n)


if select == '5':
  print(Fore.GREEN + "Opening Terminal...")
  time.sleep(0.8)
  print(Fore.RED + "This Terminal is for Testing purposes **ONLY** and is in active development")
  os.startfile('term.py')

if select == '6':
      print(Fore.GREEN + "[+] Opening Games...")
      time.sleep(0.6)
      os.startfile('games.py')
      input()

if select == '7':
      print(Fore.RED + "[-] Exiting Home screen...")
      time.sleep(0.9)
      print(Fore.RED + "[-] Logging out...\n")
      print(Fore.GREEN + "Goodbye :)")
      quit()
