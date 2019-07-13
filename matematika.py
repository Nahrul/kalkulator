import os,sys
import datetime
import time
#selow mamang jan ngegas :v

def menu():
		print("menu pilihan")
		print
		print("1.perkalian")
		print("2.pertambahan")
		print("3.pembagian")
		print("4.pengambilan")
		
def perkalian():
	print("=======tools perkalian=======")

	print("hemmmm...")
	x = input("berapa? ")
	y = input("berapa? ")
	z = int(x) * int(y)
	print("hey salam kenal " + nama)
	print("hasilnya :")
	print(z)
	pilih = input("mulai lagi? y/n ")
	
	if pilih == "y":
		os.system('clear')
		return perkalian()
		
	else:
		print("good bye :*")
	
def pertambahan():
	print("======pertambahan======")
	
	print("hemmmmm...")
	x = input("berapa? ")
	y = input("berapa?")
	z = int(x) + int(y)
	print("hey salam kenal " + nama)
	print("hasilnya")
	print(z)
	pilih = input("mulai lagi? y/n ")
	
	if pilih == "y":
		os.system('clear')
		return pertambahan()
	else:
		print("good bye :*")
		
def pembagian():
	print("======Pembagian======")
	print("")
	print("hemmmmm...")
	print("hay, salam kenal " + nama)
	x = input("berapa? ")
	y = input("berapa? ")
	z = int(x) / int(y)
	print("hasilnya: ")
	print(z)
	pilih = input("mulai lagi? y/n ")
	
	if pilih == "y":
		os.system('clear')
		return pembagian()
		
	else:
		print("good bye :*")
		
def pengambilan():
	print("=======pengambilan======")
	print("")
	print("hemm....")
	print("hay salam kenal " + nama)
	x = input("berapa? ")
	y = input("berapa? ")
	z = int(x) - int(y)
	print("hasilnya: ")
	print(z)
	pilih = input("mulai lagi? y/n ")
	
	if pilih == "y":
		os.system('clear')
		return pengambilan()
		
	else:
		print("good bye:*")
		
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
mengetik('hallo ini script kalkulator\nmaap kalo masih banyak kekurangan ya :)\n		by: Nahrul Hayat')
time.sleep(2)
os.system('clear')
sekarang = datetime.datetime.now()
print(sekarang)
print("------------------------------------")
print("----hemm..hemm..-------")
print("ko nissa sabyan ya?:v")
print("kalkulator khusus matematika XD")
print("By: Nahrul Hayat :)")
print("-----------------------------------")
print("")
nama = input("nama kamu siapa? ")
time.sleep(2)
menu()
pilih = input("masukan pilihan: ")

if pilih == "1":
	perkalian()
	
elif pilih == "2":
	pertambahan()
	
elif pilih =="3":
	pembagian()
	
elif pilih == "4":
	pengambilan()
	
else:
	print("good bye:v")
	
def menu():
		print("menu pilihan")
		print
		print("1.perkalian")
		print("2.pertambahan")
		print("3.pembagian")
		print("4.pengambilan")