try:
    sayi = int(input("Lütfen 1 ile 100 arasında bir sayı girin: "))

    # Sayı aralık dışındaysa uyarı ver
    if sayi < 1 or sayi > 100:
        print("yanlış sayı! Lütfen 1 ile 100 arasında bir sayı girin.")
    else:
        # Girilen sayıdan 100'e kadar olan çift sayıları listele
        cift_sayilar = [i for i in range(sayi, 101) if i % 2 == 0]
        print(f"{sayi} sayısından 100'e kadar olan çift sayılar:", cift_sayilar)

except ValueError:
    print("Lütfen geçerli bir tam sayı girin!")