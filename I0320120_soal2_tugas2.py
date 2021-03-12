#biodata diri
nama_lengkap = "Alfina Diva Ramadhanty"
nama_panggilan = "Diva"
tempat_tinggal = "Semanggi Rt 09 Rw 06, Pasar Kliwon, Surakarta"
tanggal_lahir = 27
bulan_lahir = 11
tahun_lahir = 2002
tempat_lahir = "Surakarta"
tanggal_sekarang = 12
bulan_sekarang = 3
tahun_sekarang = 2021
agama = "islam"
hobi = "naik gunung"
alasan_hobi = "sangat suka melihat sesuatu yang berbau alam"
cita_cita = " bekerja sebagi HRD di sebuah perusahaan "
pendidikan = "Universitas Sebelas Maret"
prodi = "Teknik Industri"
organisasi = "menjadi staff PSDM BEM FT UNS 2021"

#lain-lain
ukuran_sepatu = "37"
berat_badan = "42 kg"
tinggi_badan = "154 cm"
idola = "Leonardo DiCaprio"

#menghitung umur dalam bulan dan tahun
umur_bulan = ((tanggal_sekarang - tanggal_lahir)/30) + (bulan_sekarang - bulan_lahir) + ((tahun_sekarang - tahun_lahir) * 12)
umur_tahun = tahun_sekarang - tahun_lahir

print("Deskripsi biodata diri\n", "Hallo,Namaku", nama_lengkap, "\n", "Aku biasa di panggil", nama_panggilan, "\n", "Aku tinggal di", tempat_tinggal)
print("Aku lahir pada tanggal", tanggal_lahir,"bulan", bulan_lahir, "tahun", tahun_lahir,"\n", "Di", tempat_lahir)
print("Tahun ini aku berumur", umur_tahun, "\n", "tepatnya berumur", int(umur_bulan))
print("Aku beragama", agama,"aku juga mempunyai hobi", hobi, "\n", "aku suka naik gunung karena", alasan_hobi)
print("Sekarang aku berkuliah di", pendidikan, "di jurusan", prodi,"\n", "Aku juga mengikuti organisasi", organisasi)
print("Lain-lain\n", "Ukuran sepatu ku adalah", ukuran_sepatu, "\n", "Berat badanku", berat_badan, "Tinggi badanku", tinggi_badan)
print("Aku sangat mengidolakan", idola, "Karena beliau sosok yang juga menyukai alam dan lingkungan")








