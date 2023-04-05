from random import randint
from art import logo

#Haklar
kolay = 10
zor = 5

#Cevabı kontrol fonksiyonu
def kontrol(tahmin,cevap, hata):
    if tahmin > cevap:
        print("Cevabınız büyük")
        return hata - 1
    elif tahmin < cevap:
        print("Cevabınız düşük")
        return hata - 1
    else:
        print(f"Doğru cevap. Cevap: {cevap}")

#Zorluk fonksiyonu
def zorluk():
    seviye = input("Zorluk seviyenizi seçiniz. Kolay - Zor\n").lower()
    if seviye == "kolay":
        return kolay
    else:
        return zor

def oyun():
    print(logo)
    print("Sayı tahmin oyununa hoşgeldin! \n1-100 arasında bir sayı tuttum bakalım bilecek misin ?? :))")
    cevap = randint(1,100)

    hata = zorluk()

    tahmin = 0
    while tahmin != cevap:
        print(f"{hata} hakkınız kaldı.")

        tahmin = int(input("Tahmin et: "))

        hata = kontrol(tahmin,cevap,hata)
        if hata == 0:
            print("Tahmin hakkın bitti, kaybettin.")
            return
        elif tahmin != cevap:
            print("Tekrar tahmin et")

oyun()






