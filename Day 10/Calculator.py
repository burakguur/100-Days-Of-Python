from art import logo

print(logo)

def toplama(x, y):
    return x + y

def cıkarma(x,y):
    return x - y

def carpma(x,y):
    return x * y

def bolme(x,y):
    return x / y

tekrar = False
while not tekrar == True:
    x = int(input("Birinci sayıyı giriniz: \n"))
    y = int(input("İkinci sayıyı giriniz: \n"))
    islem = input("İşlem seçiniz:\n1-Toplama için '+'\n2-Çıkarma için '-'\n3-Çarpma için '*'\n4-Bölme için '/'\n")

    def hesapla(x,y,islem):
        if islem == "+":
            print(f"Toplama işlemi sonucunuz = {toplama(x,y)}\n")
        elif islem == "-":
            print(f"Çıkarma işlemi sonucuzu = {cıkarma(x,y)}\n")
        elif islem == "*":
            print(f"Çarpma işlemi sonucunuz = {carpma(x,y)}\n")
        elif islem == "/":
            print(f"Bölme işlemi sonucunuz = {bolme(x,y)}\n")
    hesapla(x, y, islem)
    i = input("Başka bir işlem yapmak istiyor musunuz ? 'Y' - 'N'\n")

    if i == "y":
         continue
    elif i == "n":
        tekrar = True
        print("Bye!")

