def tebak_angka():
    angka_rahasia = 9
    tebakan = 0 
    batas = 3

    while tebakan < batas:
        user = int(input("Masukkan angka > "))
        if user == angka_rahasia:
            print("Selamat Anda Berhasil menemukan angkanya")
            break
        else:
            print("Salah!")
            tebakan += 1

    else :
        print(f"Anda gagal menemukan angkanya, angka rahasianya adalah {angka_rahasia}")