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
username = "bima"
password = "bima"


#tambah
def tambah():
  os.system("clear")
  sp ("Masukan nomor dengan awalan +62")
  nomort = input(">")
  with open("target.txt", "a+") as a:
      a.write(nomort)
      a.write('\n')
      a. close()
  sp ("Ingin menambahkan nomor lagi? [Y/N]")
  tmbah = input("[Y/N]")
  if tmbah == "Y":
     tambah()
  if tmbah == "N":
     menu()
  else:
     sp ("Input salah")
     time.sleep(2)
     menu()


# mengetik otomatis cepat
def sp(a):
  for e in a + "\n":
    sys.stdout.write(e)
    sys.stdout.flush()
    time.sleep(0.005)

#pek
def handler(signal_received, frame):
    # Handle any cleanup here
    sp("\x1b[91m[!]CTRL + C DETECTED!")
    sp("[!]Program Terminated!")
    sp("Exit...")
    exit(2)

if __name__ == '__main__':
    # Tell Python to run the handler() function when SIGINT is recieved
    signal(SIGINT, handler)

#path
def path():

  if os.path.isfile('user.txt'):
      sp ("Username detected !")
      menu()
  else:
      sp ("Username null")
      user()


# username
def user():
  os.system("clear")
  usr = input("Your name :")
  with open("user.txt", "w") as f:
    f.write("Your username is "+ usr)
    f. close()
    menu()
    if usr == "":
       sp ("Gaboleh kosong")
       time.sleep(2)
       user()

#Main menu
def menu():
  os.system("reset")
  os.system("clear")
  sp ("\x1b[36m______________________________________________________")
  sp ("\x1b[92m [\x1b[91m•\x1b[92m] \x1b[33m Author \x1b[35m      : Bimz")
  sp ("\x1b[92m [\x1b[91m•\x1b[92m] \x1b[33m Instagram \x1b[35m   : bimzgz.vfx")
  sp ("\x1b[92m [\x1b[91m•\x1b[92m] \x1b[33m Github \x1b[35m      : https://github.com/Bimzgzx")
  with open('user.txt') as f:
    contents = f.read()
  sp ("\x1b[92m [\x1b[91m•\x1b[92m] \x1b[33m Information \x1b[35m : " + contents)
  sp ("\x1b[36m______________________________________________________")
  sp ("\x1b[32m                      MENU                                    ")
  sp ("\x1b[91m")
  sp ("    [1]Start Spam                          ")
  sp ("    [2]Start Spam(MASSIVE)                 ")
  sp ("    [3]Setting file nomor                  ")
  sp ("    [4]List file nomor                     ")
  sp ("    [5]Reset Nomor                         ")
  sp ("    [6]Exit                                ")
  sp ("\x1b[36m______________________________________________________")
  menupilih = input(">")
  if menupilih =="1":
       os.system("clear")
       sp ("Tidak tersedia!")
       time.sleep(1)
       menu()

  if menupilih == "2":
       os.system("clear")
       sp ("Tidak tersedia!")
       time.sleep(1)
       menu()

  if menupilih == "3":
      tambah()

  if menupilih == "4":
      if os.path.isfile('target.txt'):
        sp ("File detected !")
        with open('target.txt') as a:
          contents = a.read()
          sp (contents)
          time.sleep(5)
        menu()
      else:
        sp("Kamu belum menambahkan nomor!")
        time.sleep(3)
        menu()
  
  if menupilih == "5":
      if os.path.isfile('target.txt'):
        sp ("File detected !")
        sp ("Reset succesfull!")
        os.system("rm target.txt")
        time.sleep(4)
        menu()
      else:
        sp("target.txt not found!")
        time.sleep(3)
        menu()
        
       
  if menupilih == "6":
      sp ("Exit...")
      sp ("Goodbyee :)")
      exit()

  else:
    sp("Input error!")
    time.sleep(3)
    menu()

path()
