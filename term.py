import subprocess
import platform
import os 
import socket
import time
from tkinter.constants import COMMAND
from turtle import Home

path = 'c:/'

print("Welcome to Terminal [Version: 1.0, Development Branch]")
print("use CTRL+C at anytime to escape this terminal")

print("""
[0] Exit Terminal 
""")

# ping command
while True:
    usr_input = input("/Terminal~# ")
    host = input("Enter a URL or IP to ping: ")
    number = input("How many times do you want to ping this URL/IP? ")

    if usr_input == 'date':
        print("The Local Date Is: " + time.strftime("%m/%d/%Y"))
    def ping(host):
        param = '-n' if platform.system().lower() == 'windows' 
    else '-c'
        command = ['ping', param, number, host]
        return subprocess.call(command)
    print(ping(host))
    
    if usr_input == 0:
        os.startfile("Home.py")
