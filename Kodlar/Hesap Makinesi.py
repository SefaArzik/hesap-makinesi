print("""

Toplama işlemi için 1'e basınız.
Çıkarma işlemi içim 2'ye basınız.
çarpma işlemi için 3'e basınız.
Bölme işlemi için 4'e basınız.
Çıkış yapmak için Q yada q'e basınız 



""")    
    
while True:   
    işlem1 = str(input("Ne yapmak istiyorsunuz : "))   
    if işlem1 == "1":
        sayi1 = int(input("sayi1 giriniz : "))
        sayi2 = int(input("sayi2 giriniz : "))
        print("Sonuç: ", sayi1 + sayi2 )

    elif işlem1 == "2":
        sayi1 = int(input("sayi1 giriniz : "))
        sayi2 = int(input("sayi2 giriniz : "))
        print("Sonuç: " , sayi1 - sayi2 )
    elif işlem1 == "3":
        sayi1 = int(input("sayi1 giriniz : "))
        sayi2 = int(input("sayi2 giriniz : "))
        print("Sonuç: " , sayi1 * sayi2 )
    elif işlem1 == "4":
        sayi1 = int(input("sayi1 giriniz : "))
        sayi2 = int(input("sayi2 giriniz : "))
        print("Sonuç: ", sayi1 / sayi2)
    elif işlem1 == "q" or "Q":
        print("Çıkış yapılıyor")
        break   
    else:
        print("Geçersiz işlem girdiniz")
        break