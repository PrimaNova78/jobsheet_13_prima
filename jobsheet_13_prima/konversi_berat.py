# sistem konversi berat
def konversi_berat():
    berat = int(input("Masukkan berat anda "))
    satuan = input("Dalam satuan apa berat yang anda masukkan ? (L untuk LBS, K untuk KG) ")


    if satuan.upper() == 'L':
        print(f"Berat anda {round(berat/2.2)}kg") 
    elif satuan.upper() == 'K':
        print(f"Berat anda {round(berat*2.2)}pon")