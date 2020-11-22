import random
import os

ekraniTemizle = lambda: os.system('cls')


tarlaUzunluk = 8
tarlaGenislik = 8
mayinSayisi = 16
tarla = []

mayinIndeksleri = []
alanSayisi = tarlaUzunluk * tarlaGenislik


i = 0
while(i < mayinSayisi):
	mayinAraniyor = True
	
	while(mayinAraniyor):
		indeks = random.randint(0,alanSayisi)
		
		if(not(indeks in mayinIndeksleri)):
			mayinIndeksleri.append(indeks)
			mayinAraniyor = False
			i = i + 1



i = 0
while(i < alanSayisi):
	tarla.append("x ")
	i = i + 1

def IndeksinEtrafindaKacMayinVar(indeks):
	etrafindakiMayinSayisi = 0
	i = 0
	
	while(i < 3):
		geriKontrolAlanIndeksi = indeks - (tarlaGenislik + 1) + i
		if(geriKontrolAlanIndeksi >= 0):
			alanGecerlimi = True
			
			if(i == 0 and geriKontrolAlanIndeksi % tarlaGenislik == tarlaGenislik -1):
				alanGecerlimi = False
			
			elif(i == 2 and geriKontrolAlanIndeksi % tarlaGenislik == 0):
				alanGecerlimi = False
			
			if(alanGecerlimi and geriKontrolAlanIndeksi in mayinIndeksleri):
				etrafindakiMayinSayisi = etrafindakiMayinSayisi + 1
		ileriKontrolAlanIndeksi = indeks + (tarlaGenislik - 1) + i
		if(ileriKontrolAlanIndeksi < alanSayisi):
			alanGecerlimi = True
			if(i == 0 and ileriKontrolAlanIndeksi % tarlaGenislik == tarlaGenislik -1):
				alanGecerlimi = False
			elif(i == 2 and ileriKontrolAlanIndeksi % tarlaGenislik == 0):
				alanGecerlimi = False
			if(alanGecerlimi and ileriKontrolAlanIndeksi in mayinIndeksleri):
				etrafindakiMayinSayisi = etrafindakiMayinSayisi + 1
		i = i + 1
	
	if(indeks - 1 >= 0 and (indeks-1) % tarlaGenislik != tarlaGenislik - 1):
		if(indeks-1 in mayinIndeksleri):
			etrafindakiMayinSayisi = etrafindakiMayinSayisi + 1
	
	if(indeks + 1 < alanSayisi and (indeks+1) % tarlaGenislik != 0):
		if(indeks+1 in mayinIndeksleri):
			etrafindakiMayinSayisi = etrafindakiMayinSayisi + 1
	return etrafindakiMayinSayisi


def EkraniCizdir():
	
	ekraniTemizle()
	i = 0
	print("   ", end="")
	
	while(i < tarlaGenislik):
		print(str(i) + " ", end="")
		i = i +1
	i = 0
	while(i < alanSayisi):
		if(i % tarlaGenislik == 0):
			print('')
			print(str(int(i/tarlaGenislik)) + ': ', end = "") 
		print(tarla[i], end="") 
		i = i + 1
		
oyunDevamEdiyor = True
kazandi = False
EkraniCizdir()
acilanAlanSayisi = 0

while(oyunDevamEdiyor):
	print("")
	
	sutun = int(input("Sütun >>>"))
	
	while(sutun < 0 or sutun >= tarlaGenislik):
		sutun = int(input("Gecerli Sütun gir >>>"))
	
	satir = int(input("Satir >>>"))
	while(satir < 0 or satir >= tarlaUzunluk):
		satir = int(input("Gecerli Satir gir >>>"))
	
	inputIndex = satir * tarlaGenislik + sutun
	
	if(inputIndex in mayinIndeksleri):
		oyunDevamEdiyor = False
		tarla[inputIndex] = "m "
	else: 
		
		tarla[inputIndex] = str(IndeksinEtrafindaKacMayinVar(inputIndex)) + " "
		acilanAlanSayisi = acilanAlanSayisi + 1
		
		if(alanSayisi - acilanAlanSayisi == mayinSayisi):
			kazandi = True
			oyunDevamEdiyor = False
	EkraniCizdir()

print("")
if(kazandi):
	print("Kazandi!")
else:
	print("Kaybetti!")