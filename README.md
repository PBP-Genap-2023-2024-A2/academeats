# Tugas Kelompok PBP A2

## AcademEats

### Nama-nama anggota kelompok
- Muhammad Firaz Al Aqib (2306217481)
- Carleano Ravelza Wongso (2306213022)
- Kania Almyra Bilqist (2306216996)
- Naila Nursa Krisnazulfa (2306275071)
- Khair Juzaili (2206028623)

### Deskripsi Singkat Aplikasi

Dalam konteks kehidupan mahasiswa, terutama di lingkungan kampus, waktu dan efisiensi menjadi faktor penting dalam memenuhi kebutuhan sehari-hari, termasuk makanan. Di Fakultas Ilmu Komputer Universitas Indonesia, menjaga produktivitas dan keseimbangan antara akademik dan kebutuhan pribadi menjadi prioritas utama bagi mahasiswa dan staf pengajar.

Namun, dalam kegiatan sehari-hari, seringkali terjadi tantangan untuk mengatur waktu antara menghadiri kuliah, diskusi, atau menghabiskan waktu di perpustakaan dengan memenuhi kebutuhan makanan. Kantin fakultas sering menjadi destinasi utama untuk membeli makanan, namun terkadang antrian panjang atau ketersediaan makanan yang terbatas bisa menjadi hambatan.

Untuk mengatasi tantangan tersebut, AcademEats hadir sebagai solusi inovatif yang memanfaatkan teknologi dalam memesan makanan secara praktis dan efisien di kantin fakultas. Dengan menggunakan aplikasi AcademEats, mahasiswa dan staf pengajar dapat melakukan pemesanan makanan dari kantin secara online, sehingga menghemat waktu dan memastikan ketersediaan makanan saat diperlukan.

Fitur-fitur yang disediakan oleh AcademEats mencakup:

- Menampilkan daftar makanan dari setiap toko yang terdaftar pada AcademEats.

- Keranjang menampilkan daftar makanan-makanan yang ingin dibeli oleh seorang pembeli dari toko-toko. Pembeli juga dapat mengeluarkan makanan dari keranjang.

- Melakukan pemesanan makanan (order) dari toko.

- Memberikan review terhadap makanan yang dipesan.

- Menyediakan forum berdiskusi untuk mengobrol antara para mahasiswa serta elemen kantin.

Dengan adanya AcademEats, diharapkan pengguna dapat lebih efisien dalam mengatur waktu mereka dan tidak lagi harus mengalami hambatan dalam mendapatkan makanan di kantin fakultas. Selain itu, aplikasi ini juga membantu meningkatkan pengalaman pengguna dalam hal kenyamanan dan kemudahan dalam memesan makanan.

### Daftar Modul

#### Makanan 
##### Dikerjakan oleh: Naila Nursa Krisnazulfa
Modul ini berfungsi untuk mengolah model makanan dari toko, menambah, mengubah, dan menampilkan makanan yang terdapat pada database.
Pembeli|Penjual
-|-
Pembeli dapat melakukan melihat display makanan dari tiap toko kemudian melakukan pemesanan atau memasukkan ke keranjang|Penjual dapat menambah/mengubah makanan pada toko mereka.


#### Keranjang
##### Dikerjakan oleh: Khair Juzaili
Pada fitur keranjang, pembeli dapat memasukkan makanan-makanan dari toko untuk di-checkout yang akan mengurangi saldo pembeli. Pembeli juga dapat menghapus makanan dari keranjang.
Pembeli|Penjual
-|-
Pembeli dapat memasukkan makanan-makanan yang akan dibeli ke keranjang| Penjual tidak memiliki fitur keranjang

#### Order
##### Dikerjakan oleh: Kania Almyra Bilqist
Modul ini berfungsi untuk mengurus pesanan dari user. Pesanan setelah dicheckout dari keranjang, akan diolah menjadi order, kemudian akan melakukan notifikasi ke pemilik toko untuk diolah.

Pembeli|Penjual
-|-
Pembeli dapat melakukan checkout untuk mengambil makanan-makanan yang telah ditaruh di keranjang dan mengubahnya menjadi order (pesanan)|Penjual dapat melakukan pelaksanaan pesanan dan memberi tahu informasi mengenai order tersebut (belum atau telah selesai dibuat)


#### Review
##### Dikerjakan oleh: Muhammad Firaz Al Aqib
Modul ini untuk menampilkan review dari setiap makanan yang diberikan oleh User. Review ini berisi nilai dan ulasan.
Pembeli|Penjual
-|-
Pembeli dapat memberikan review terhadap makanan yang baru saja diorder|Penjual dapat memberikan balasan terhadap review yang diberikan oleh pembeli


#### Forum
##### Dikerjakan oleh: Carleano Ravelza Wongso
Modul ini berfungsi sebagai tempat para user berdiskusi mengenai suatu topik. Nantinya user dapat membuka topik forum dan berdiskusi di dalamnya.
Pembeli|Penjual
-|-
Pembeli dapat membuka forum dan berdiskusi dalam forum dengan pembeli atau penjual lain|Sama seperti pembeli


### Sumber Dataset Makanan dan Minuman
https://www.kaggle.com/datasets/ariqsyahalam/indonesia-food-delivery-gofood-product-list

### Role atau Peran Pengguna Beserta Deskripsinya

Terdapat dua role, pembeli dan penjual. Detail tiap role telah dijelaskan di bagian daftar modul.
