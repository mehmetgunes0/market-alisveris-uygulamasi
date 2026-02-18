"""
Kullanıcıdan ürün ve fiyat bilgilerini alarak bir alışveriş sepeti oluşturmak, ardından bakiye kontrolü yapıp, yeterli değilse sepetten ürün silmek.

Görev Tanımı:
1. Ürün ve fiyat bilgilerini kullanıcıdan alın (örneğin: “Ekmek – 10 TL”, “Süt – 25 TL”).
• Kullanıcı “X” yazana kadar ürün ve fiyat almaya devam edin.
• Ürün adlarını urunler listesinde, fiyatları fiyatlar listesinde saklayın.
2. Kullanıcıdan bakiye bilgisini isteyin.
3. for döngüsüyle sepeti ekrana yazdırın ve toplam fiyatı hesaplayın.
4. if yapısı ile kontrol edin:
• Eğer bakiye yeterliyse
• Eğer bakiye yetmiyorsa:
5. Bakiyesi yetmeyen kullanıcıya while döngüsüyle ürün silme seçeneği verin.
• Ürün silindikçe toplam fiyatı yeniden hesaplayın.
• Bakiye yeterli olunca siparişi onaylayın.
"""

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
            