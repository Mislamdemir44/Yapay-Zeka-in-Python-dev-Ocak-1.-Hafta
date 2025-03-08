# Kullanıcıdan ad, yaş ve doğum yılı alma
ad = input("Adınızı girin: ")
yas = int(input("Yaşınızı girin: "))
dogum_yili = 2024 - yas  # Güncel yıla göre doğum yılını hesapla

print(f"Merhaba {ad}! {yas} yaşındasın ve {dogum_yili} yılında doğmuşsun.")

# Kullanıcıdan iki sayı alma
sayi1 = float(input("Birinci sayıyı girin: "))
sayi2 = float(input("İkinci sayıyı girin: "))

# Dört işlem hesaplamaları
toplam = sayi1 + sayi2
fark = sayi1 - sayi2
carpim = sayi1 * sayi2
if sayi2 != 0:
    bolum = sayi1 / sayi2
else:
    bolum = "Tanımsız (sıfıra bölme hatası)"

# Sonuçları ekrana yazdırma
print(f"Toplam: {toplam}")
print(f"Fark: {fark}")
print(f"Çarpım: {carpim}")
print(f"Bölüm: {bolum}")
