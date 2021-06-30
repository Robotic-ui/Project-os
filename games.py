import time 
import os
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

print(Fore.LIGHTCYAN_EX + "What game would you like to play?")
print("""
[1] Snake
[2] Pong
[3] Tetris
[4] Go back to Home
""")

select = input("/Games~# ")

if select == '1':
    os.startfile('Games/Snake.py')

if select == '2':
    os.startfile('Games/Pong.py')

if select == '3':
    os.startfile('Games/Tetris.py')

if select == '4':
    os.startfile('Home.py')
    time.sleep(2)
    quit()
