import os,sys
import datetime
import time
#selow mamang jan ngegas :v

def menu():
		print(red,"-----------•menu pilihan•--------")
		print
		print(yellow,"|======> [1]•perkalian   <======|")
		print(green,"|======> [2]•pertambahan <======|")
		print(blue,"|======> [3]•pembagian   <======|")
		print(purple,"|======> [4]•pengambilan <======|")
		print(cyan,"|======> [0]•exit        <======|")
		
def utama():
	sekarang = datetime.datetime.now()
	print("|-----------------------------------|")
	print("| ",sekarang,"      |")
	print("|  kalkulator khusus matematika XD  |")
	print("|     By: Nahrul Hayat :)           |")
	print("|-----------------------------------|\n")
#	nama = input("nama kamu siapa? ")
	time.sleep(0.5)
	menu()
	pilih = input("\033[1;30m\nmasukan pilihan: ")
	
	if pilih == "1":
		perkalian()
		
	elif pilih == "2":
		pertambahan()
		
	elif pilih =="3":
		pembagian()
		
	elif pilih == "4":
		pengambilan()
	
	elif pilih == "0":
		print(cyan,"see you next time :)")
		exit()
		
	else:
		print("pilihan yang anda masukan salah +_-")
		time.sleep(1)
		os.system('clear')
		utama()
	
def perkalian():
	print("\033[1;33m=======tools perkalian=======")
	print
	x = input("berapa? ")
	y = input("berapa? ")
	z = int(x) * int(y)
	print("hasilnya :")
	print(x,"×",y,"=",z)
	pilih = input("mulai lagi? y/n ")
	if pilih == "y":
		os.system('clear')
		utama()
		
	else:
		print("×_- sampai jumpa lagi nanti '_'")
	
def pertambahan():
	print("\033[1;32m======pertambahan======")
	print
	x = input("berapa? ")
	y = input("berapa?")
	z = int(x) + int(y)
	print("hasilnya")
	print(x,"+",y,"=",z)
	pilih = input("mulai lagi? y/n ")
	
	if pilih == "y":
		os.system('clear')
		utama()
	else:
		print("×_- sampai jumpa lagi nanti '_'")
		
def pembagian():
	print("\033[1;34m======Pembagian======")
	print
	x = input("berapa? ")
	y = input("berapa? ")
	z = int(x) / int(y)
	print("hasilnya: ")
	print(x,":",y,"=",z)
	pilih = input("mulai lagi? y/n ")
	
	if pilih == "y":
		os.system('clear')
		utama()
		
	else:
		print("×_- sampai jumpa lagi nanti '_'")
		
def pengambilan():
	print("\033[1;35m=======pengambilan======")
	print
	x = input("berapa? ")
	y = input("berapa? ")
	z = int(x) - int(y)
	print("hasilnya: ")
	print(x,"-",y,"=",z)
	pilih = input("mulai lagi? y/n ")
	
	if pilih == "y":
		os.system('clear')
		utama()
		
	else:
		print("×_- sampai jumpa lagi nanti '_'")
		
#program
import random
import sys
import time

os.system('clear')
def mengetik(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.1)
mengetik('\033[1;36mhallo ini script kalkulator\nmaap kalo masih banyak kekurangan ya :)\n		by: Nahrul Hayat')
time.sleep(2)
os.system('clear')
red = '\033[1;31m'
yellow = '\033[1;33m'
green = '\033[1;32m'
blue = '\033[1;34m'
purple = '\033[1;35m'
cyan = '\033[1;36m'
grey = '\033[1;30m'

utama()
	