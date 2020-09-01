# Tuli-dan-Disleksia
Program "App Ketikan Disleksia atau tuli v --" adalah program untuk menyusun kalimat acak menjadi kalimat yang sesuai struktur bahasa indonesia yang benar (S-P-O-K). Penamaan filenya terinspirasi dari orang yang mengidap penyakit tuli atau disleksia karena jika mereka menuliskan sebuah kalimat cenderung kalimatnya menjadi acak. Misal = aku sedang goreng makan ayam yang sebenernya bermaksud = aku sedang makan ayam goreng.
<br/>
Program ini bekerja yang intinya adalah mencari kombinasi-kombinasi yang mungkin kalimat yang sesuai struktur bahasa indonesia.
<br/>
<br/>

variabel penting
<br/>
data = berisi tentang jenis-jenis kata (S, P, O, K, Konj) bisa di update sendiri.
<br/>
subjek_to_objek = adalah berisi subjek yang mungkin menjadi objek
<br/>
cocok = adalah mencocokan sesuatu predikat yang cocok untuk sebuah objek
<br/>

komentar penting
<br/>
##masalah = adalah masalah yang belum bisa terseleksaikan
<br/>
#jadi atau ##pasti jadi = adalah kalimat yang jadi untuk dirun (sesuai harapan)
<br/>
#engga = adalah kalimat-kalimat yang belum jadi (tidak sesuai harapan)
<br/>
<br/>

contoh hasil dri program ini:
<br/>
Kalimat ngacak:
<br/>
sangat suka minum susu aku rifa sedangkan coklat suka makan
<br/>

Hasil:
<br/>
aku sangat suka makan coklat sedangkan rifa suka minum susu <br/>
rifa sangat suka makan coklat sedangkan aku suka minum susu <br/>
rifa suka makan coklat sedangkan aku sangat suka minum susu <br/>
rifa suka minum susu sedangkan aku sangat suka makan coklat <br/>
aku suka minum susu sedangkan rifa sangat suka makan coklat <br/>
aku sangat suka minum susu sedangkan rifa suka makan coklat <br/>
aku suka makan coklat sedangkan rifa sangat suka minum susu <br/>
rifa sangat suka minum susu sedangkan aku suka makan coklat <br/>
