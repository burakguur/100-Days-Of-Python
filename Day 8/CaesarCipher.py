alfabe = ['a', 'b', 'c','ç', 'd', 'e', 'f', 'g','ğ', 'h','ı', 'i', 'j', 'k', 'l', 'm',
            'n', 'o','ö', 'p', 'q', 'r', 's','ş', 't', 'u','ü', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c','ç', 'd', 'e', 'f', 'g','ğ', 'h','ı', 'i', 'j', 'k', 'l', 'm',
            'n', 'o','ö', 'p', 'q', 'r', 's','ş', 't', 'u','ü', 'v', 'w', 'x', 'y', 'z']

from art import logo



def sıfre(ilk_yazı, kaydırma_num,sifreleme):
    son_yazı = ""
    if secim == "decode":
        kaydırma_num *= -1
    for harf in ilk_yazı:
        if harf in alfabe:
            yer = alfabe.index(harf)
            yeni_yer = yer + kaydırma_num
            son_yazı += alfabe[yeni_yer]
        else:
            son_yazı += harf
    print(f"Şifrelenmiş yazınız: {son_yazı}")

print(logo)

bitis = False
while not bitis:
    secim = input("Encode - Decode seçiminiz : \n")
    yazı = input("Mesajınızı giriniz : \n")
    kaydırma = int(input("Kaydırma miktarını giriniz: \n"))

    sıfre(ilk_yazı=yazı, kaydırma_num=kaydırma,sifreleme=secim)

    tekrarla = input("Tekrar denemek istiyor musunuz ? 'Evet' / 'Hayır'\n").lower()
    if tekrarla == "hayır":
        bitis = True
        print("Byee!")

