def fuzzy_membership(x, a, b, c, d):
    if x <= a:
        return 0
    elif a < x <= b:
        return (x - a) / (b - a)
    elif b < x <= c:
        return 1
    elif c < x < d:
        return (d - x) / (d - c)
    else:
        return 0

def fuzzy_bahu_naik(x,a,b):
    if x<=a:
        return 0
    elif a < x <= b:
        return (x-a) / (b - a)
    else :
        return 1

def fuzzy_bahu_turun(x,a,b):
    if x<=a:
        return 1
    elif a < x <= b:
        return (b-x) / (b - a)
    else :
        return 0


def main():
    pilihan = input("Apa yang ingin Anda pilih? (air/teh): ") 

    if pilihan == "air":
        print(" Kategori suhu")
        print(" Air Biasa: 0°C - 10°C")
        print(" Dingin: 5°C - 20°C")
        print(" Hangat: 15°C - 35°C")
        print(" Panas: 30°C - 45°C")
        suhu = float(input("Masukkan suhu air (0-45): "))

        dingin = fuzzy_bahu_turun(suhu, 5, 15)
        air_biasa = fuzzy_membership(suhu, 15, 20, 25, 30)
        hangat = fuzzy_membership(suhu, 25, 30, 35, 40)
        panas = fuzzy_bahu_naik(suhu, 40, 45)  

        # print(f"Keanggotaan Air_Biasa: {air_biasa}")
        # print(f"Keanggotaan Air Dingin: {dingin}")
        # print(f"Keanggotaan Air Hangat: {hangat}")
        # print(f"Keanggotaan Air Panas: {panas}")

        if panas > hangat and panas > dingin and panas > air_biasa:
            air_status = "Panas"
        elif hangat > panas and hangat > dingin and hangat > air_biasa:
            air_status = "Hangat"
        elif dingin > panas and dingin > hangat and dingin > air_biasa:
            air_status = "Dingin"
        else:
            air_status = "Air Biasa"

        print(f"Anda mengambil air: {air_status}")

    elif pilihan == "teh":
        suhu = float(input("Masukkan suhu air (0-40): "))
        gula = float(input("Masukkan jumlah gula (0-14 sendok teh): "))
        teh = float(input("Masukkan jumlah teh (0-6 sendok teh): "))

        dingin = fuzzy_membership(suhu, 5, 15, 20, 25)
        air_biasa = fuzzy_membership(suhu, 20, 25, 30, 35)
        hangat = fuzzy_membership(suhu, 30, 35, 40, 45)

        sedikit_gula = fuzzy_membership(gula, 0, 2, 4, 6)
        cukup_gula = fuzzy_membership(gula, 4, 6, 8, 10)
        manis = fuzzy_membership(gula, 8, 10, 12, 14)

        sedikit_teh = fuzzy_membership(teh, 0, 1, 2, 3)
        cukup_teh = fuzzy_membership(teh, 3, 4, 5, 6)

        # print(f"Keanggotaan Air Dingin: {dingin}")
        # print(f"Keanggotaan Air Hangat: {hangat}")
        # print(f"Keanggotaan Air Biasa: {air_biasa}")

        # print(f"Keanggotaan Gula Sedikit: {sedikit_gula}")
        # print(f"Keanggotaan Gula Cukup: {cukup_gula}")
        # print(f"Keanggotaan Gula Manis: {manis}")
        # print(f"Keanggotaan Teh Sedikit: {sedikit_teh}")
        # print(f"Keanggotaan Teh Cukup: {cukup_teh}")

        
        if hangat > dingin and hangat > air_biasa:
            air_status = "Hangat"
        elif dingin > air_biasa:
            air_status = "Dingin"
        else:
            air_status = "Air Biasa"

        if sedikit_gula > cukup_gula and sedikit_gula > manis:
            gula_status = "Sedikit Gula"
        elif cukup_gula > manis:
            gula_status = "Cukup Gula"
        else:
            gula_status = "Manis"

        if sedikit_teh > cukup_teh:
            teh_status = "Sedikit Teh"
        else:
            teh_status = "Cukup Teh"

        print(f"Air: {air_status}, Gula: {gula_status}, Teh: {teh_status}")
        print(f"Buat Teh {air_status}, {gula_status}, {teh_status}")

    else:
        print("Pilihan tidak valid. Silakan pilih 'air' atau 'teh'.")

if __name__ == "__main__":
    main()
