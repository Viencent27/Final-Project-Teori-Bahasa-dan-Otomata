def dictCFG():
  cfg_final = {}
  # Gabungan CFG 1 kelas
  cfg = ["K → S P | S P Ket | S P O | S P O Ket | S P Pel | S P Pel Ket | S P O Pel | S P O Pel Ket | S P Ket Pel",
         "S → NP",
         "P → VP | AdjP",
         "O → NP",
         "Ket → PP",
         "Pel → AdjP | NP | NumP | PP | VP",
         "NP → Noun | NP Noun | NP PP | NP PropNoun | Pronoun | PropNoun | Adv NP | NP Adj | NumP NP | VP NP | NP Adv | NP Pronoun | Adj NP | NP Num | Num NP | NP VP | NP NumP",
         "VP → Verb | Adv VP | AdjP | Adj VP | VP Adv | VP PP | Verb NP",
         "PP → Prep NP | Prep AdjP | Prep VP | Prep NumP",
         "AdjP → Adv Adj | Adj | Adv AdjP",
         "NumP → Num | NumP Adv | NumP Noun | Adv Num",
         "Noun → acara | orang | sayur | pasir | uang | panitia | bapak | karcis | proposal | eksemplar | tsunami | rapat | ekor | ayam | penerbit | penyunting | bedah | seseorang | daring | kg | lagu | tali | pertandingan | pemain | cadangan | perusahaan | unit | rumah | ruangan | benih | ikan | lele | kucing | wasit | petani | sawah | benua | musim | puding | kambing | tahun | universitas | mahasiswa | buah | buku | kuliah | perpustakaan | kampus | karyawan | ibu | setel | baju | olah-raga | biologi | mikroskop | kamera | jenis | es | krim | bayam | toko | basket | tugas | sekolah | selokan | jendela | kamar | kursi-kursi | sejoli | sekawan | serangkai | anggota | geng | mall | bersahabat | kilogram | taman | bersaudara | daging | sekelas | masalah | warung | adonan | air | aturan | rakyat | rejeki | penjuru | mujair | organisasi | terima | kasih | ikat | tengkorak | penjual | cangkir | umat | muslim | depan | budak | tragedi | dunia | luka | istri | bencana | gempa | pengungsi | bantuan | gedung | ban | kode | listrik | etik | pelajar | tentara | papan | hutan | bakau | oknum | polisi | prosedur | bola | jawaban | adikku | lapangan | tim | sepak | kali | pak | objek | kampungku | penghargaan | pengabdian | relawan | hari | jadi | peringkat | kelas | mobil | ulang | bupati | anak | atas | keluarga | sehari | beras | deret | teluk | pagi | jam | kegiatan | motor | roda | ayah | semangka | tulis | pensil | bu | sepeda | ponsel | sapi | sofa | pasang | sepatu | kangkung | hotel | mangga | durian | pohon | buaya | saudara | apel | belakang | kartu | pos | ronda | gazebo | laptop | adik | tetangga | dalam | kota | kafe | sahabat | patung | kuda | rumput | kandang | pisang | gula | kopi | hal | ujian | tni | pengunjung | kerja | tiket | halaman | mata | persoalan | keringat | insan | tangan | sisir | tas | permen | cerita | potong | korban | perang | petak | umpet | siswa | upacara | bendera | kelompok | rombongan | gelas | suara | gorengan | penonton | generasi | edisi | kaset | peserta | pasien | sakit | gol | urutan | kejadian | galon | persepsi | masyarakat | wahana | paman | adegan | teman | paras | pengalaman | gadis | perhatian | wanita | telur | hati | bujang | pemalu | pacar | pria | pendendam | remaja | pencuri | penyayang | orang-orang | kakek | seorang | pejuang | negara | banteng | meja | perusak | kebun | kelapa | sawit | malam | petinju | turnamen | film | bioskop | suasana | pantai | olimpiade | matematika | uang | pemotong | kayu | desa | penipu | kantor | pemalas | prestasi | tenda | kukang | hewan | peneliti | laboratorium | penyabar | bakso | anjing | tongkat | parfum | bunga | mawar | hadiah | onar | sifat | pemaaf | kue | konser | burung | bulu | ember | liter | saat | hakim | pengampun | kasus | kakak | umum | pemberontak | nenek | pelupa | kancil | pembohong | pepohonan | kedatangan | kepala | serigala | keadaannya | kecelakaan | sandal | hektar | konglomerat | tangan-tangan | mimpiku | manusia | suara-suara | turis | hadirin | seisi | presentasi | galaksi | seniman | lukisan-lukisan | belatung | mie | internet | dosen | nilainya | video | pembicara | seminar | keindahan | kualitas | grafisnya | provinsi | hal-hal | tempat | kuburan | hawa | gunung | film-film | keganasannya | pembangunan | tindakan | bangsa | masa | penjajahan | dahulu | cara | permainan | pembawa | penampilan | opera | lelucon | pelawak | makalah | isi | berita | pembicaraan | olahraga | rumahmu | makanan | minuman | pinggir | selama | rasa | snack | pemandangan | tanaman | kepemimpinan | gaya | bicara | kondisi | hasil | pekerjaan | perbuatan | servis | serdadu | kelakuan | diri | hukum | riasan | kecuraman | jalan | pejalan | kaki | kemarin | wajah | adalah | senyum | tawa | tadi | kehilangan | bom | atom | para | kotanya | novel | penulis | sekolahnya | penari | sawitku | desaku | kakekku | nenekku | pendiam | pencemburu | pemarah | tongkatnya | kepalanya | bulunya | hatiku | drama | pertunjukan | penyanyi | rumahnya | temannya | pamannya | tuaku | padaku | pacarnya | diriku | disini | usia | budaya | apartemen | kenegaraan | Mangga | warnet",
         "PropNoun → gagak | saman | kuta | tbo | shawn | mendes | cyberpunk | 2077 | bima | sakti | biznet | indonesia | iphone | nanggroe | aceh | darussalam | piranha | jepang | hantu | udin | akhirudin | awaludin | kirudin | kamarudin | samsudin | saipudin | sarafudin | bahrudin | yando | dila | arga | deni | wena | arya | rika | botak | darma | dewi | santi | winda | andri | wendi | weli | asti | wendy | budi | tuli | aris | surabaya | baharudin | amir | inggris | amanda | mangrove | widia | singaraja | yanto | sista | ngurah | saripudin | adi | dimas | eropa | udayana | anto | lita | gunggus | bhadrika | salim | sari | eka | ary | saleh | fredy | andi | kadir | wawin | surya | mahayasa | jalaludin | fika | octa | lindung | dede | asep | lohan | rama | bella | nia | faisal | paragon | trisna | aris | pkk | bali | monas | cianjur | kanjuruhan | benoa | adit | parman | made | rudi | ketut | klungkung | putu | alit",
         "Pronoun → itu | nya | mereka | ku | ini | saya | ia | sesuatu | anda | kalian | kita | kamu | kami | pak | si | kakek | nenek",
         "Verb → membuat | terbiasa | menundukkan | menghadiahi | menang | berdiskusi | ulang | setuju | dengar | dikumpul | menampilkan | muncul | dihapus | terjadi | dibagikan | disaksikan | ditulis | menghadiri | dianjurkan | melakukan | mengoleksi | terasa | memiliki | mendaki | mengganti | merenovasi | merupakan | terlihat | terdengar | menjadi | bermain | menyeruduk | menghampiri | mengajar | makan | minum | terjatuh | hidup | tercinta | terus | menenteramkan | mengubah | memadati | berbahaya | menelan | terlantar | diasuh | memerankan | terkejut | memukau | merekam | mengharukan | memalukan | menarik | memikat | memarahi | membunuh | mengangkat | memasuki | ditangkap | membantu | adalah | membawa | dikalahkan | merasakan | menolak | menyedihkan | menonton | melawan | menghantui | mencekam | membanggakan | mengherankan | beristirahat | tertidur | berjalan | bisa | membelikan | berdarah | menuduh | menawarkan | terkenal | selama | memuat | memelihara | mengakui | mendapatkan | bertemu | menyukai | wisata | menakutkan | menebang | memenangkan | tinggal | mengajak | tidur | menyenangkan | membeli | melemparkan | menyebabkan | memakai | terharu | melukai | kehilangan | mengusir | dapat | menceritakan | menggembirakan | berbekas | memerlukan | menggoreng | memasak | memetik | membutuhkan | mempunyai | menjual | mencari | membaca | membangun | belajar | memakan | mengendarai | memanjat | menyembunyikan | dijual | mengambil | melempar | mengerjakan | memberikan | berisi | membersihkan | berdatangan | menanam | bercucuran | menyelesaikan | bermandikan | berpegangan | melontarkan | berjatuhan | berlatih | beranggotakan | pergi | memecahkan | menyulutkan | mendaftar | mencetak | menyebar | menyembelih | tersisa | memandikan | melihat | berkurban | memberhentikan | meminjam | menyewakan | datang | merapikan | terpisahkan | melaksanakan | liburan | bekerja | menghadapi | dilestarikan | diikuti | dibungkam | gotong | royong | mengucapkan | ada | mencuci | bertahan | beribadah | bersama-sama | bergotong | mengalami | menderita | meninggal | mengungsi | melanggar | bersembunyi | ditendang | menulis | menginjak | turun | kalah | memperoleh | terpilih | merayakan | mendapat | bertelur | berada | didapatkan",
         "Adj → mencekam | menjemukan | mengerikan | nasional | sempit | kesepian | memalukan | menjijikkan | lebar | terpukau | suka | terbengkalai | sama | instan | tua | banyak | menakutkan | besar | kecil | keras | aneh | merdu | menarik | terkenal | bahagia | pemarah | pendiam | senang | tangguh | pelupa | kali | selalu | tidak | handal | aktif | sungguh | pusing | khawatir | baik | syok | megah | pintar | kompak | akrab | baru | kembar | segar | bagus | berat | mahal | keren | cantik",
         "Adv → sangat | makin | dengan | secara | begitu | sebagian | sering | selalu | dapat | telah | sudah | ingin | paling | sedang | sempat | masih | saja | baru | akan | selamanya | harus | sekali | sekitar | lagi | hanya",
         "Num → beberapa | sebuah | berhari-hari | semua | banyak | setiap | seluruh | kedua | semangkok | dua | setangkai | tiga | puluh | seratus | sebelas | lima | ratus | sembilan | empat | satu | belas | ribu | enam | sepuluh | berempat | berdua | bertiga | berlima | bersembilan | berbulan-bulan | berenam | bertujuh | bersepuluh | bersebelas | berdelapan | berdua-lima | berbagai | pelbagai | sedikit | segala | segenap | berpuluh-puluh | beratus-ratus | beribu-ribu | berjuta-juta | belasan | puluhan | ratusan | ribuan | separuh | segelintir | ketiga | kesembilan | kesebelas | keempat | kedua-puluh-lima | kelima | pertama | keenam | ketujuh | kedelapan | delapan | tujuh | kesepuluh | keseratus | seorang | seekor | juta | 11 | 3 | 25 | 5 | 10 | 15 | 2 | 1 | 7 | 8 | 27 | seikat | sepasang | setengah | bertahun-tahun | selusin",
         "Prep → setelah | ke | yang | pada | dalam | dengan | di | kepada | bagi | karena | dari | oleh | supaya | sampai | hingga | untuk | si | akibat"
  ]
  for i in cfg:
    seperate_LHSnRHS = i.split(" → ") # Memisahkan LHS dan RHS
    cfg_final[seperate_LHSnRHS[0]] = seperate_LHSnRHS[1].split(" | ") # RHS menjadi key dan LHS menjadi value
  
  return cfg_final

if __name__ == '__main__':
  dictCFG()
