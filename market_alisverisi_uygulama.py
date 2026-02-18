
ürün = []
fiyat = []


while True:
    ürünAdi = input("Ürün Adını Girin: ")
    if ürünAdi == "x":
        break
    ürünFiyati =int(input("Ürün Fiyatını Girin: "))
    ürün.append(ürünAdi)
    fiyat.append(ürünFiyati)

toplam = sum(fiyat)

bakiye = int(input("Bakiye Bilgisini Girin: "))

for i in ürün:
    print("\n---> SEPETİNİZ <--- \n",ürün," == ",fiyat,"\n Toplam Sepet Tutarınız: ",toplam)
    if bakiye>= toplam:
        print("\nSiparişiniz Onaylandı!")
        break
    elif bakiye<toplam:
        print("\nDevam Etmek İçin Lütfen Ürün Çıkarın!\n")
        while True:
            ürünAdi = input("Çıkarmak İstediğiniz Ürünün Adını Girin: ")
            if ürünAdi == "x":
             break
            ürünFiyati = int(input("Çıkarmak İstediğiniz Ürünün Fiyatını Girin: "))
            ürün.remove(ürünAdi)
            fiyat.remove(ürünFiyati)
            toplam = sum(fiyat)
            
