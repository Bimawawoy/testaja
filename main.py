#coding: utf-8
# module
import os,sys,time,getpass,json
from tqdm import tqdm
import pathlib
import os.path
from signal import signal, SIGINT
from sys import exit

#Warna
red   = '\x1b[31m' # Merah
green = '\x1b[32m' # Hijau
yellow = '\x1b[33m' # Kuning
blue  = '\x1b[34m' # Biru
magenta = '\x1b[35m' # Ungu
cyan  = '\x1b[36m' # Biru Muda
white = '\x1b[37m' # Putih
reset = '\x1b[39m' # Reset Warna ( Kembali Ke Warna Awal )
brblack = '\x1b[90m' # Hitam Terang
R = '\x1b[91m' # Merah Terang
brgreen = '\x1b[92m' # Hijau Terang
k = '\x1b[93m' # Kuning Terang
brblue = '\x1b[94m' # Biru Terang
brmgnt = '\x1b[95m' # Ungu Terang
brcyan = '\x1b[96m' # Biru Muda Terang
G = '\x1b[97m' # Putih Terang# username
x = "bima"
# password
y = "bima"
ulang = 9999
jumlah = 1

  
def metu():
	os.system("clear")
	slamet=input("Yakin ingin keluar?[Y/N]")
	
#pek
def handler(signal_received, frame):
    # Handle any cleanup here
    sp("CTRL + C DETECTED!")
    sp("abort")
    exit(2)

if __name__ == '__main__':
    # Tell Python to run the handler() function when SIGINT is recieved
    signal(SIGINT, handler)

#path
def path():

  if os.path.isfile('user.txt'):
      print ("Username detected !")
      menu()
  else:
      print ("Username null")
      user()


# username
def user():
  os.system("clear")
  usr = input("Your name :")
  with open("user.txt", "w") as f:
    f.write("Your username is "+ usr)
    menu()
    if usr == "":
       sp ("Gaboleh kosong")
       time.sleep(2)
       user()

# down
def down():
  for i in tqdm(range(50)):
      print("Download..")
      time.sleep(0.2)


# spam
def spam():
  print ("\x1b[96m[\x1b[91m•\x1b[96m]Contoh Nomor \x1b[91m81xxxx")
  nomer = input("\x1b[96m[\x1b[91m•\x1b[96m]\x1b[96mNomor Target \x1b[91m: ")
# menu
def menu():
  os.system('clear')
sp ("\x1b[96m <=======================================>")
sp ("\x1b[92m [\x1b[91m•\x1b[92m] \x1b[33m Author \x1b[35m : \x1b[31m Bimaa Kun")
sp ("\x1b[92m [\x1b[91m•\x1b[92m] \x1b[33m Instagram \x1b[35m : \x1b[31m bimzgz.vfx")
sp ("\x1b[92m [\x1b[91m•\x1b[92m] \x1b[33m Facebook \x1b[35m : \x1b[31m Bimz Wibu")

with open("user.txt") as f:
    contents = f.read()
sp ("\x1b[92m [\x1b[91m•\x1b[92m] \x1b[33m Information \x1b[35m :" + contents)
sp ("\x1b[96m <=======================================>")
sp
sp ("\033[1;31m [1] Start brutal spam")
sp("\033[1;31m [2] Check update")
sp("\033[1;31m [3] Report bug (Whatsapp)")
sp("\033[1;31m [4] Download package(full)")
sp("\033[1;31m [5] Exit")
sp
 menu1 = input ("Choose>")  
  if menu1  =="1":
       os.system("clear")
       sp ("Loading...")
       time.sleep(3)
       spam()
  
  if menu1  =="2":
       os.system("clear")
       sp ("Tidak ada update yang tersedia...")
       time.sleep(3)
       menu()

  if menu1 =='':
       sp("ORANG GILA !")
       time.sleep(5)
       menu()

  if menu1 =="3":
       os.system("clear")
       sp ("Membuka whatsapp...")
       time.sleep(4)
       os.system("xdg-open https://wa.me/6281229259881")
       menu()

  if menu1 =="4":
       os.system("clear")
       sp ("Sedang mendownload package")
       down()
       time.sleep(10)
       menu()

  if menu1 =="5":
       keluar ()
  else:
      sp("Input salah")
      time.sleep(2)
menu()
    

# mengetik otomatis cepat
def sp(a):
  for e in a + "\n":
    sys.stdout.write(e)
    sys.stdout.flush()
    time.sleep(0.001)


# login
def login():
  os.system("clear")
  sp("\033[1;96m       ╔╗   ╔═══╗╔═══╗╔══╗╔═╗ ╔╗")
  sp("       ║║   ║╔═╗║║╔═╗║╚╣─╝║║╚╗║║")
  sp("       ║║   ║║ ║║║║ ╚╝ ║║ ║╔╗╚╝║")
  sp("       ║║ ╔╗║║ ║║║║╔═╗ ║║ ║║╚╗║║")
  sp("       ║╚═╝║║╚═╝║║╚╩═║╔╣─╗║║ ║║║")
  sp("       ╚═══╝╚═══╝╚═══╝╚══╝╚╝ ╚═╝")
  sp("\033[1;96m+\033[1;90m========================================\033[1;96m+")
  sp(" \033[1;97m{\033[1;95m•\033[1;97m} \033[1;93mAuthor   \033[1;91m: \033[1;95mBimz Senpai")
  sp(" \033[1;97m{\033[1;95m•\033[1;97m} \033[1;93mFacebook \033[1;91m: \033[1;95mBimz wibu")
  sp("\033[1;96m+\033[1;90m========================================\033[1;96m+")
  username = input(" \033[1;97m{\033[1;93m+\033[1;97m} \033[1;96mUsername:\033[1;92m ")
  password = getpass.getp#coding: utf-8
# module
import os,sys,time,getpass,json
from tqdm import tqdm
import pathlib
import os.path
from signal import signal, SIGINT
from sys import exit

#Warna
red   = '\x1b[31m' # Merah
green = '\x1b[32m' # Hijau
yellow = '\x1b[33m' # Kuning
blue  = '\x1b[34m' # Biru
magenta = '\x1b[35m' # Ungu
cyan  = '\x1b[36m' # Biru Muda
white = '\x1b[37m' # Putih
reset = '\x1b[39m' # Reset Warna ( Kembali Ke Warna Awal )
brblack = '\x1b[90m' # Hitam Terang
R = '\x1b[91m' # Merah Terang
brgreen = '\x1b[92m' # Hijau Terang
k = '\x1b[93m' # Kuning Terang
brblue = '\x1b[94m' # Biru Terang
brmgnt = '\x1b[95m' # Ungu Terang
brcyan = '\x1b[96m' # Biru Muda Terang
G = '\x1b[97m' # Putih Terang# username
x = "bima"
# password
y = "bima"
ulang = 9999
jumlah = 1


def keluar():
  os.system("clear")

  elp = input ("Yakin ingin keluar? [Y/N]:")

  if elp =="Y":
       sp ("Byee byee :)")
       exit()

  if elp =="N":
       menu()
  else:
     sp("Input salah")
     time.sleep(2)
     menu()
  

#pek
def handler(signal_received, frame):
    # Handle any cleanup here
    sp("CTRL + C DETECTED!")
    sp("abort")
    exit(2)

if __name__ == '__main__':
    # Tell Python to run the handler() function when SIGINT is recieved
    signal(SIGINT, handler)

#path
def path():

  if os.path.isfile('user.txt'):
      print ("Username detected !")
      menu()
  else:
      print ("Username null")
      user()


# username
def user():
  os.system("clear")
  usr = input("Your name :")
  with open("user.txt", "w") as f:
    f.write("Your username is "+ usr)
    menu()
    if usr == "":
       sp ("Gaboleh kosong")
       time.sleep(2)
       user()

# down
def down():
  for i in tqdm(range(50)):
      print("Download..")
      time.sleep(0.2)


# spam
def spam():
  print ("\x1b[96m[\x1b[91m•\x1b[96m]Contoh Nomor \x1b[91m81xxxx")
  nomer = input("\x1b[96m[\x1b[91m•\x1b[96m]\x1b[96mNomor Target \x1b[91m: ")
# menu
def menu():
  os.system('clear')
  sp("\x1b[96m <=======================================>")
  sp("\x1b[92m [\x1b[91m•\x1b[92m] \x1b[33m Author \x1b[35m : \x1b[31m Bimaa Kun")
  sp("\x1b[92m [\x1b[91m•\x1b[92m] \x1b[33m Instagram \x1b[35m : \x1b[31m bimzgz.vfx")
  sp("\x1b[92m [\x1b[91m•\x1b[92m] \x1b[33m Facebook \x1b[35m : \x1b[31m Bimz Wibu")
  with open('user.txt') as f:
    contents = f.read()
  sp("\x1b[92m [\x1b[91m•\x1b[92m] \x1b[33m Information \x1b[35m :" + contents)
  sp("\x1b[96m <=======================================>")
  sp
  sp
  sp("\033[1;31m [1] Start brutal spam")
  sp("\033[1;31m [2] Check update")
  sp("\033[1;31m [3] Report bug (Whatsapp)")
  sp("\033[1;31m [4] Download package(full)")
  sp("\033[1;31m [5] Exit")
  sp
  menu1 = input ("Choose>")  
  if menu1  =="1":
       os.system("clear")
       sp ("Loading...")
       time.sleep(3)
       spam()
  
  if menu1  =="2":
       os.system("clear")
       sp ("Tidak ada update yang tersedia...")
       time.sleep(3)
       menu()

  if menu1 =='':
       sp("ORANG GILA !")
       time.sleep(5)
       menu()

  if menu1 =="3":
       os.system("clear")
       sp ("Membuka whatsapp...")
       time.sleep(4)
       os.system("xdg-open https://wa.me/6281229259881")
       menu()

  if menu1 =="4":
       os.system("clear")
       sp ("Sedang mendownload package")
       down()
       time.sleep(10)
       menu()

  if menu1 =="5":
       keluar ()
  else:
       sp("Input salah")
       time.sleep(2)
       menu()
    

# mengetik otomatis cepat
def sp(a):
  for e in a + "\n":
    sys.stdout.write(e)
    sys.stdout.flush()
    time.sleep(0.001)


# login
def login():
  os.system("clear")
  sp("\033[1;96m       ╔╗   ╔═══╗╔═══╗╔══╗╔═╗ ╔╗")
  sp("       ║║   ║╔═╗║║╔═╗║╚╣─╝║║╚╗║║")
  sp("       ║║   ║║ ║║║║ ╚╝ ║║ ║╔╗╚╝║")
  sp("       ║║ ╔╗║║ ║║║║╔═╗ ║║ ║║╚╗║║")
  sp("       ║╚═╝║║╚═╝║║╚╩═║╔╣─╗║║ ║║║")
  sp("       ╚═══╝╚═══╝╚═══╝╚══╝╚╝ ╚═╝")
  sp("\033[1;96m+\033[1;90m========================================\033[1;96m+")
  sp(" \033[1;97m{\033[1;95m•\033[1;97m} \033[1;93mAuthor   \033[1;91m: \033[1;95mBimz Senpai")
  sp(" \033[1;97m{\033[1;95m•\033[1;97m} \033[1;93mFacebook \033[1;91m: \033[1;95mBimz wibu")
  sp("\033[1;96m+\033[1;90m========================================\033[1;96m+")
  username = input(" \033[1;97m{\033[1;93m+\033[1;97m} \033[1;96mUsername:\033[1;92m ")
  password = getpass.getpass(" \033[1;97m{\033[1;93m+\033[1;97m} \033[1;96mPassword: ")
  if username == x and password == y:
    print(" \033[1;92mAccess Granted !")
    time.sleep(1)
    path()
  else:
    for i in range(ulang):
        sp("\x1b[31m Access Denied !")

login()
ass(" \033[1;97m{\033[1;93m+\033[1;97m} \033[1;96mPassword: ")
if username == x and password == y:
    print(" \033[1;92mAccess Granted !")
    time.sleep(1)
    path()
else:
    for i in range(ulang):
        sp("\x1b[31m Access Denied !")

login()