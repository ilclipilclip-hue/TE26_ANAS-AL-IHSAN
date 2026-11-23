TEGANGAN = 220.0  # Tegangan suplai tetap (Volt)

# 15 data inti tetap (Arus dalam Ampere)
data_inti = [0.8, 1.5, 2.4, 3.18, 3.2, 3.8, 4.2, 4.54, 4.55, 5.1, 1.1, 2.9, 3.5, 4.8, 6.0]

# 5 data tambahan realistis (beban rendah, mendekati ambang batas, dan beban tinggi)
data_tambahan = [0.5, 2.0, 3.1, 4.5, 5.5]

semua_arus = data_inti + data_tambahan


def hitung_daya(arus, tegangan=220.0):
    """Menghitung daya listrik P = V * I (Watt) tanpa pembulatan dini."""
    return tegangan * arus


def tentukan_status(daya):
    """Mengklasifikasikan status beban berdasarkan satu nilai daya P (Watt)."""
    if daya <= 700.0:
        return "AMAN"
    elif daya <= 1000.0:
        return "WASPADA"
    else:
        return "BEBAN TINGGI"


def hitung_statistik(daftar_daya):
    """Menghitung rata-rata, daya maksimum, dan daya minimum dari seluruh data."""
    rata_rata = sum(daftar_daya) / len(daftar_daya)
    daya_maks = max(daftar_daya)
    daya_min = min(daftar_daya)
    return rata_rata, daya_maks, daya_min


def main():
    daftar_daya = []
    jumlah_aman = 0
    jumlah_waspada = 0
    jumlah_tinggi = 0

    print("=== HASIL MONITORING BEBAN / DAYA LISTRIK (KELOMPOK A) ===")
    print(f"{'No':<4} | {'Arus (A)':<10} | {'Daya (W)':<12} | {'Status'}")
    print("-" * 48)

    for i, arus in enumerate(semua_arus, start=1):
        daya = hitung_daya(arus, TEGANGAN)
        status = tentukan_status(daya)
        daftar_daya.append(daya)

        if status == "AMAN":
            jumlah_aman += 1
        elif status == "WASPADA":
            jumlah_waspada += 1
        else:
            jumlah_tinggi += 1

        print(f"{i:<4} | {arus:<10.2f} | {daya:<12.2f} | {status}")

    rata_rata, daya_maks, daya_min = hitung_statistik(daftar_daya)

    print("-" * 48)
    print("=== RINGKASAN STATISTIK ===")
    print(f"Total Data          : {len(semua_arus)}")
    print(f"Jumlah AMAN         : {jumlah_aman}")
    print(f"Jumlah WASPADA      : {jumlah_waspada}")
    print(f"Jumlah BEBAN TINGGI : {jumlah_tinggi}")
    print(f"Rata-rata Daya      : {rata_rata:.2f} W")
    print(f"Daya Maksimum       : {daya_maks:.2f} W")
    print(f"Daya Minimum        : {daya_min:.2f} W")


if __name__ == "__main__":
    main()