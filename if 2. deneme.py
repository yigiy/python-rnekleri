print("Not Hesaplama")
sınav1 = int(input("1.sınav notunuzu giriniz: "))
sınav2 = int(input("2.sınav notunuzu giriniz: "))
ortalama = (sınav1 + sınav2)/2
if (sınav1 > 100 or sınav1<0) or (sınav2 > 100 or sınav2<0):
    print("notlar 0 ile 100 arasında olur")
else:#sınav notlarında hata yoksa aşağıdakiler çalışacak.
        if ortalama >=90: print ("harikasın AA aldın")
        elif ortalama >= 70 : print ("notun fen değil BB aldın")
        elif ortalama >= 50 : print ("geçtin işte",ortalama)
        else:
            print("malesef kaldın")