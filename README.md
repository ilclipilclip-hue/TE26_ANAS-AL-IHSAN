# UangTerencana

Website sederhana untuk mencatat pemasukan/pengeluaran, memantau anggaran bulanan, dan merencanakan target tabungan.

## Menjalankan di komputer

1. Ekstrak folder `uang-terencana` jika Anda mengunduh versi ZIP.
2. Buka `index.html` dengan browser (Chrome, Edge, Firefox, atau Safari).

Tidak perlu instalasi, server, atau akun.

## Membuat website bisa dibuka orang lain

Website ini berupa situs statis. Agar bisa dibuka lewat tautan publik, unggah `index.html` ke layanan hosting situs statis, misalnya Netlify atau GitHub Pages. Pada Netlify, Anda dapat membuat situs baru dengan metode deploy manual/drag-and-drop dari folder yang berisi `index.html`. Setelah proses publikasi berhasil, layanan hosting akan memberikan URL yang bisa dibagikan.

## Catatan penting tentang data

- Transaksi, anggaran, dan target disimpan di penyimpanan browser/perangkat masing-masing (`localStorage`).
- Orang lain dapat membuka situs yang sama, tetapi data mereka **tidak otomatis terlihat oleh Anda atau pengguna lain**.
- Gunakan menu **Cadangkan data** untuk mengunduh file JSON, lalu **Pulihkan cadangan** untuk memindahkannya ke browser/perangkat lain.
- Jangan masukkan PIN, kata sandi, nomor rekening lengkap, atau informasi rahasia.

## Fitur

- Ringkasan pemasukan, pengeluaran, dan saldo bulanan.
- Grafik pengeluaran enam bulan terakhir.
- Pencatatan transaksi dengan kategori dan tanggal.
- Anggaran per kategori dan indikator saat anggaran terlampaui.
- Target tabungan dengan progres dan penambahan dana.
- Filter dan pencarian transaksi.
- Ekspor CSV serta cadangan/pemulihan JSON.
- Tampilan responsif untuk ponsel dan desktop.
