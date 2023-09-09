konu ="HESAP MAKİNESİ"
print("\033[1;33;40m")#renkli yazmak için yazdık
print("╔"+"═"*(len(konu)+2)+"╗")
print("║ \033[1;31;40m"+konu+"\033[1;33;40m ║")
print("╚"+"═"*(len(konu)+2)+"╝")
print("\033[1;37;40m")
print("1-TOPLAMA")
print("2-ÇIKARMA")
print("3-ÇARPMA")
print("4-BÖLME")
print("5-ÇIKIŞ")

sayi1 = int(input("1.sayıyı giriniz"))
sayi2 = int(input("2.sayıyı giriniz"))

secim = input("SEÇİMİNİZ ?")


if secim =="1":print("toplamı:",sayi1+sayi2)


if sayi2>sayi1:
    gecici = sayi2
    sayi2 = sayi1
    sayi1 = gecici


if secim =="2":print("farkı:",sayi1-sayi2)
if secim =="3":print("çarpımı:",sayi1*sayi2)
if secim =="4":print("bölümü:",sayi1/sayi2)
if secim =="5":exit()
