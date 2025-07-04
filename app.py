from flask import Flask, render_template

app = Flask(__name__)

# Data semua proyek
data = {
    1: {
        'judul': 'Perbandingan Klasifikasi Cuaca Kota Denpasar dengan Regresi Logistik Multinomial dan Analisis Diskriminan',
        'deskripsi': 'Proyek ini membandingkan kinerja Regresi Logistik Multinomial (MLR) dan Analisis Diskriminan Linear (LDA) untuk klasifikasi kondisi cuaca Kota Denpasar tahun 2019 ke dalam empat kategori: Clear, Clouds, Rain, dan Thunderstorm. Analisis dilakukan menggunakan RStudio, mencakup pemodelan, evaluasi akurasi, dan interpretasi hasil.',
        'tujuan': 'Mengidentifikasi variabel-variabel yang memberikan kontribusi signifikan terhadap pembentukan kategori cuaca serta mengevaluasi tingkat akurasi dan kemudahan interpretasi model yang dihasilkan. ',
        'manfaat': 'Diterapkannya analisis diskriminan dan regresi multinomial untuk membangun model klasifikasi kondisi atmosfer di Kota Denpasar yang akurat dan dapat diinterpretasikan dengan mudah.',
        'gambar': ['ANMUL 1.png', 'ANMUL 2.jpg', 'ANMUL 3.JPG', 'ANMUL 4.png'],
        'rpubs': 'https://rpubs.com/RezaUnesaSada23/RegresiMultinomiaMenggunakanPCA',
        'kolaborasi': 'Kolaborasi Bersama  : Alfathrindra A. Yuliyanto & Hizkia Marvel Abhinaya',
        'tools': [
            {'nama': 'RStudio', 'logo': 'rstudio.png'},
            {'nama': 'Python', 'logo': 'python.png'}
        ]
    },

    4: {
        'judul': 'Covid-19 Visualisasi untuk Literasi Digital',
        'deskripsi': 'Proyek ini merupakan pembuatan dashboard interaktif menggunakan Looker Studio untuk memvisualisasikan data Covid-19. Visualisasi ini menampilkan informasi seperti jumlah kasus, tingkat kesembuhan, tingkat kematian, dan tren persebaran Covid-19 secara mudah dipahami.',
        'tujuan': 'Proyek ini bertujuan untuk membangun dashboard interaktif berbasis Looker Studio yang menyajikan data Covid-19 secara visual, sehingga masyarakat dapat dengan mudah memahami perkembangan kasus, tren penyebaran, dan dampaknya secara real-time.',
        'manfaat': 'Melalui visualisasi yang sederhana dan interaktif, proyek ini membantu meningkatkan literasi digital masyarakat, memudahkan akses informasi terkait Covid-19, serta mendorong kesadaran dan pemahaman yang lebih baik dalam menghadapi pandemi.',
        'gambar': ['LITDIG 1.png', 'LITDIG 2.png', 'LITDIG 3.png'],
        'looker': 'https://lookerstudio.google.com/reporting/ae2362d8-e6d9-43bc-a2e1-1ac57fc41167/page/84Z0D',
        'kolaborasi': 'Kolaborasi Bersama  : Alfathrindra A. Yuliyanto, Hizkia Marvel Abhinaya & Andreas S. Simorangkir',
        'tools': [
            {'nama': 'Looker Studio', 'logo': 'looker (2).jpeg'},
            {'nama': 'Python', 'logo': 'python.png'}
        ]
    },

    3: {
        'judul': 'Forecasting Kualitas Udara  untuk Prediksi Indeks Standar Pencemar Udara (ISPU) di Kota Jakarta',
        'deskripsi': 'Proyek ini merupakan implementasi konsep Data Mining untuk melakukan forecasting atau prediksi terhadap Indeks Standar Pencemar Udara (ISPU) di Kota Jakarta. Pengembangan model prediksi ISPU bertujuan untuk menyediakan proyeksi kualitas udara secara akurat guna mendukung pengambilan kebijakan berbasis data.',
        'tujuan': 'Mengembangkan model prediksi yang dapat memperkirakan Indeks Standar Pencemar Udara (ISPU) di Jakarta berdasarkan data historis ISPU dan faktor-faktor pendukung lainnya. ',
        'manfaat': 'Memberikan rekomendasi berbasis data untuk kebijakan publik yang dapat meningkatkan kualitas udara di Jakarta, serta mengurangi dampak negatif terhadap kesehatan masyarakat.',
        'gambar': ['DATMIN 1.png', 'DATMIN 2.png', 'DATMIN 3.png', 'DATMIN 4.png'],
        'github': 'https://github.com/MuhamadAlfaRezaGobel23/Proyek-Akhir-Data-Mining',
        'kolaborasi': 'Kolaborasi Bersama  : Akhmad Dany & Alfathrindra A. Yuliyanto',
        'tools': [
            {'nama': 'Python', 'logo': 'python.png'},
            {'nama': 'Canva', 'logo': 'canva.jpeg'}
        ]
    },

    11: {
        'judul': 'Sistem Rekomendasi Restoran Berdasarkan Analisis Ulasan dan Rating Menggunakan Metode Clustering',
        'deskripsi': 'Proyek ini bertujuan untuk memberikan rekomendasi restoran yang relevan dan personal dengan memanfaatkan data ulasan dan rating dari pelanggan di beberapa restoran yang ada.',
        'tujuan': 'Proyek ini bertujuan untuk memberikan rekomendasi restoran yang relevan dan personal dengan memanfaatkan data ulasan dan rating dari pelanggan di beberapa restoran yang ada. Proyek ini juga bertujuan untuk meningkatkan efisiensi pengambilan keputusan pengguna dan memberikan informasi yang bermanfaat sesuai preferensi pengguna.',
        'manfaat': 'Proyek ini bermanfaat bagi pengguna dengan mempercepat proses pencarian restoran yang diberikan berdasarkan preferensi pengguna, sehingga menghemat waktu dan usaha dalam memilih tempat makan atau restoran yang ideal. ',
        'gambar': ['PEMTEKS 1.png', 'PEMTEKS 2.png', 'PEMTEKS 3.png', 'PEMTEKS 4.png'],
        'github': 'https://github.com/MuhamadAlfaRezaGobel23/Proyek-Akhir-Pemrosesan-Teks',
        'kolaborasi': 'Kolaborasi Bersama  : Nabila Nasywa Zen & Erma Shafira Zulfianti',
        'tools': [
            {'nama': 'Python', 'logo': 'python.png'}]
    },

    5: {
        'judul': 'DairyMoo: Optimasi Restocking Produk Susu di Peternakan Sapi Perah Menggunakan Algoritma Dynamic Programing',
        'deskripsi': 'DairyMoo adalah sistem berbasis algoritma Dynamic Programming yang dirancang untuk mengoptimalkan proses restocking produk susu di peternakan sapi perah. Sistem ini menganalisis pola penjualan dan permintaan pelanggan untuk menghasilkan keputusan restocking yang efisien, dengan tujuan memastikan ketersediaan stok minimum tanpa menumpuk produk secara berlebih. Dalam proyek ini, tiga algoritma telah dianalisis yaitu Dynamic Programming (Top-Down), Dynamic Programming (Bottom-Up), dan Algoritma Greedy.',
        'tujuan': 'Tujuan utama dari sistem DairyMoo adalah untuk mengoptimalkan proses restocking produkproduk sisi di peternakan sapi perah untuk memastikan ketersediaan minimum tanpa mengakibatkan overstocking. Sistem ini dibangun untuk menganalisis data historis penjualan dan permintaan pelanggan, sehingga dapat memberikan rekomendasi keputusan restocking yang efisien.', 
        'manfaat': 'Sistem ini bermanfaat untuk meningkatkan efisiensi restocking, mengurangi risiko pemborosan akibat overstocking, serta membantu peternakan sapi perah mengelola stok secara berkelanjutan dengan rekomendasi berbasis data yang adaptif terhadap perubahan permintaan.',
        'gambar': ['DAA 1.png', 'DAA 2.png', 'DAA 3.png', 'DAA 4.jpg'],
        'github': 'https://github.com/MuhamadAlfaRezaGobel23/Proyek-Akhir-Desain-Analisis-Algoritma',
        'kolaborasi': 'Kolaborasi Bersama  : Nabila Nasywa Zen & Alfathrindra A. Yuliyanto',
        'tools': [
            {'nama': 'Python', 'logo': 'python.png'}]
    },

    6: {
        'judul': 'Penerapan Data Warehouse dalam Analisis Kasus dan Kematian COVID-19 di Amerika Serikat',
        'deskripsi': 'Proyek ini bertujuan untuk merancang dan membangun sistem Data Warehouse yang berfungsi sebagai pusat integrasi dan penyimpanan data Covid-19 di Amerika Serikat. Sistem ini dirancang untuk menghimpun data dari berbagai sumber secara terstruktur, konsisten, dan historis guna mendukung keperluan analisis dan pelaporan.',
        'tujuan': 'Menyediakan infrastruktur penyimpanan data terintegrasi yang dapat mendukung proses analisis, visualisasi, serta pengambilan keputusan strategis terkait penanganan pandemi Covid-19 di Amerika Serikat.', 
        'manfaat': 'Sistem ini memberikan kemudahan dalam mengakses, mengelola, dan menganalisis data Covid-19 secara efisien, sehingga dapat digunakan oleh pemerintah, lembaga kesehatan, dan peneliti untuk memantau perkembangan pandemi dan merumuskan kebijakan yang lebih tepat sasaran.',
        'gambar': ['DATWER 1.png', 'DATWER 2.png', 'DATWER 3.png', 'DATWER 4.jpg'],
        'github': 'https://github.com/MuhamadAlfaRezaGobel23/Proyek-Akhir-Data-Warehouse-Komputasi-Terdistibusi',
        'kolaborasi': 'Kolaborasi Bersama  : Alfathrindra A. Yuliyanto & Rizki Wahyu Widodo',
        'tools': [
            {'nama': 'Python', 'logo': 'python.png'}]
    },

    7: {
        'judul': 'Sistem Verifikasi Tanda Tangan Menggunakan Artificial Neural Network (ANN) pada Pengolahan Citra Digital',
        'deskripsi': 'Proyek ini mengembangkan sistem verifikasi tanda tangan berbasis Artificial Neural Network (ANN) dengan memanfaatkan teknik pengolahan citra digital. Sistem ini dirancang untuk mengidentifikasi dan memverifikasi keaslian tanda tangan melalui analisis pola visual, bentuk, dan karakteristik unik yang terekam dalam citra digital, sehingga dapat meningkatkan akurasi dan keamanan proses autentikasi.',
        'tujuan': 'Proyek ini bertujuan untuk merancang sistem verifikasi tanda tangan digital berbasis dengan dukungan teknik image preprocessing, guna meningkatkan akurasi dalam membedakan tanda tangan asli dan palsu secara efisien.', 
        'manfaat': 'Sistem ini memberikan solusi yang efektif untuk meningkatkan keamanan dan keakuratan proses verifikasi identitas, khususnya dalam dokumen resmi atau transaksi digital, serta mengurangi potensi pemalsuan tanda tangan secara signifikan.',
        'gambar': ['PCD 1.png', 'PCD 2.png', 'PCD 3.png', 'PCD 4.jpg'],
        'github': 'https://github.com/MuhamadAlfaRezaGobel23/PROYEK-AKHIR-PCD-KELOMPOK-3-SAINSDATA-2023-E',
        'kolaborasi': 'Kolaborasi Bersama  : Hizkia Marvel Abhinaya & Andreas Setiandi Simmorangkir',
        'tools': [
            {'nama': 'Python', 'logo': 'python.png'},
            {'nama': 'Canva', 'logo': 'canva.jpeg'}
        ]
    },

    8: {
        'judul': 'PrediStrok : Klasifikasi Resiko Serangan Stroke Menggunakan Multi Layer Perceptron (MLP)',
        'deskripsi': 'Sistem ini ditujukan untuk membantu tenaga medis dan masyarakat umum dalam mengidentifikasi risiko stroke secara dini, khususnya berdasarkan atribut kesehatan seperti usia, tekanan darah, kadar glukosa, riwayat penyakit, serta kebiasaan hidup seperti merokok. ',
        'tujuan': 'Tujuan dari proyek ini adalah membangun sistem klasifikasi risiko stroke berbasis algoritma Multilayer Perceptron (MLP) yang dilatih menggunakan metode Backpropagation', 
        'manfaat': 'Model diharapkan dapat menangkap hubungan kompleks antar variabel kesehatan, yang tidak dapat diselesaikan secara optimal oleh model linier seperti regresi logistik.',
        'gambar': ['PMD 1.png', 'PMD 2.png', 'PMD 3.png', 'PMD 4.png'],
        'streamlit': 'https://klasifikasi-stroke-app-lr6z7ulfzg37fbhezgb2sk.streamlit.app/',
        'kolaborasi': 'Kolaborasi Bersama  : Akhmad Dany & M. Aqsa Firdaus',
        'tools': [
            {'nama': 'Python', 'logo': 'python.png'},
            {'nama': 'Streamlit', 'logo': 'streamlit.png'}]
    },

    9: {
        'judul': 'SirenSignal: Pengolahan Sinyal Digital untuk Menganalisis Arti Sirene Ambulans menggunakan metode MFCC dengan pendekatan KNN',
        'deskripsi': 'Sistem ini menggunakan Mel-Frequency Cepstral Coeflcients (MFCC) untuk mengekstraksi fitur suara sirene dan K-Nearest Neighbor (KNN) untuk mengklasifikasikan jenis sirene, seperti peringatan darurat atau pengumuman biasa.',
        'tujuan': 'Proyek ini bertujuan untuk mengembangkan sistem yang mampu mengenali arti suara sirene ambulans dengan memanfaatkan teknik pengolahan sinyal digital untuk mengurangi noise, yang sering mengganggu suara sirene di lingkungan lalu lintas yang padat.', 
        'manfaat': 'Memungkinkan pengemudi dan pejalan kaki untuk lebih responsif terhadap sirene darurat, mengurangi risiko kecelakaan serta diharapkan agar masyarakat dapat membedakan antara sirene peringatan darurat dan pengumuman biasa.  ',
        'gambar': ['PSD 1.png', 'PSD 2.png', 'PSD 3.png', 'PSD 4.png'],
        'github': 'https://github.com/MuhamadAlfaRezaGobel23/Proyek-Akhir-Pengolahan-Sinyal-Digital',
        'kolaborasi': 'Kolaborasi Bersama  : Akhmad Dany & Alfathrindra A. Yuliyanto',
        'tools': [
            {'nama': 'Python', 'logo': 'python.png'}]
    },

    10: {
        'judul': 'Sistem Basis Data untuk Pembelian dan Berlangganan E-Book Berbagai Kategori',
        'deskripsi': 'Proyek ini mengembangkan sistem basis data yang terintegrasi untuk mendukung layanan pembelian dan berlangganan e-book berbagai kategori. Sistem ini dirancang untuk menyimpan, mengelola, dan mengorganisir data secara efisien, termasuk data pengguna, katalog e-book, kategori buku, riwayat transaksi, dan paket langganan. Dengan adanya sistem ini, proses pengelolaan data menjadi lebih terstruktur dan dapat menunjang operasional aplikasi secara optimal.',
        'tujuan': 'Proyek ini bertujuan merancang dan membangun Sistem Basis Data untuk mendukung proses pembelian dan langganan e-book. Sistem basis data ini dirancang untuk mengelola data pengguna, kategori buku, katalog e-book, transaksi pembelian, serta data paket langganan.', 
        'manfaat': 'Sistem basis data ini memberikan kemudahan dalam pengelolaan informasi e-book, meningkatkan efisiensi pencatatan transaksi pembelian maupun langganan, serta mendukung penyediaan layanan yang lebih cepat, akurat, dan terorganisir bagi pengguna.',
        'gambar': ['BASDAT 1.png', 'BASDAT 2.png', 'BASDAT 3.png', 'BASDAT 4.png'],
        'github': 'https://github.com/MuhamadAlfaRezaGobel23/Proyek-Akhir-Basis-Data',
        'kolaborasi': 'Kolaborasi Bersama  : Akhmad Dany & Alfathrindra A. Yuliyanto',
        'tools': [
            {'nama': 'SQL', 'logo': 'sql.jpeg'},
            {'nama': 'Figma', 'logo': 'figma.png'},
            {'nama': 'Power Designer', 'logo': 'power.jpeg'}]
    },

     2: {
        'judul': 'NafasKu : Aplikasi Cerdas untuk Pemantauan Kualitas Udara & Prediksi Serangan Asma Berbasis Artificial Intellegence',
        'deskripsi': 'NafasKu adalah aplikasi berbasis teknologi dan kecerdasan buatan (AI) yang dirancang untuk membantu penderita asma dan penyakit pernapasan dalam mendeteksi kualitas udara secara real-time serta merespons serangan asma dengan cepat dan efisien.',
        'tujuan': 'Mengembangkan aplikasi cerdas berbasis kecerdasan buatan (AI) yang mampu memantau kualitas udara secara real-time dan memberikan prediksi potensi serangan asma, sehingga pengguna dapat mengambil langkah pencegahan lebih awal untuk menjaga kesehatan pernapasan.', 
        'manfaat': 'Aplikasi ini memberikan kemudahan bagi penderita asma dan masyarakat umum dalam memantau kondisi udara di sekitar mereka, meningkatkan kewaspadaan terhadap risiko serangan asma, serta membantu pengambilan keputusan cepat dalam upaya pencegahan dan penanganan gangguan pernapasan.',
        'gambar': ['IMK 1.png', 'IMK 2.png', 'IMK 3.png', 'IMK 4.png'],
        'behance': 'https://www.behance.net/gallery/228797915/NafasKu',
        'kolaborasi': 'Kolaborasi Bersama  : Andreas Setiandi Simorangkir & Rizki Wahyu Widodo',
        'tools': [
            {'nama': 'Figma', 'logo': 'figma.png'},
            {'nama': 'Canva', 'logo': 'canva.jpeg'},
            {'nama': 'Form', 'logo': 'form.jpeg'}]
    },

    12: {
        'judul': 'Sicepet : Optimasi jalur pengantaran paket Amazon scout robot  di kota Semarang Menggunakan Algoritma Uniform Cost Search',
        'deskripsi': 'Proyek ini dirancang untuk menemukan jalur pengantaran paling efisien dengan mempertimbangkan jarak dan waktu tempuh di kota semarang pada tahun 2023 dan 2024.',
        'tujuan': 'Mengoptimalkan jalur pengantaran paket dengan algoritma Uniform Cost Search (UCS) untuk menemukan rute paling efisien berdasarkan biaya minimum, seperti jarak & kondisi jalan dan Menyediakan estimasi waktu dan keterlambatan pengantaran, memberikan informasi akurat untuk mendukung perencanaan pengiriman.',
        'manfaat': 'Mengurangi waktu tempuh dan biaya operasional pengantaran paket di wilayah perkotaan seperti Semarang & Memberikan prediksi waktu pengantaran yang lebih akurat, sehingga meningkatkan kepercayaan pelanggan terhadap layanan pengantaran.',
        'gambar': ['AI 1.png', 'AI 2.png', 'AI 3.png', 'AI 4.jpg'],
        'github': 'https://github.com/MuhamadAlfaRezaGobel23/Proyek-Akhir-Kecerdasan-Artifisial',
        'kolaborasi': 'Kolaborasi Bersama  : Akhmad Dany & Alfathrindra A. Yuliyanto',
        'tools': [
            {'nama': 'Python', 'logo': 'python.png'},
            {'nama': 'Canva', 'logo': 'canva.jpeg'},]
    },
    13: {
        'judul': 'Atlas Shoes Care: Sistem Layanan Cuci Sepatu dengan Penyortiran Pesanan Berbasis Queue dan Algoritma Count Sort',
        'deskripsi': 'Atlas Shoes Care merupakan sebuah sistem yang menyediakan layanan untuk mencuci sepatu, dimana pengguna dapat memilih beberapa opsi dalam mencuci sepatu yang  sesuai dengan kebutuhannya. Program ini akan menyortir urutan pesanan menggunakan struktur data queue, serta algoritma count sort untuk mengurutkan rincian pesanan pengguna.',
        'tujuan': 'Membangun sistem layanan cuci sepatu yang memudahkan pengguna dalam melakukan pemesanan sesuai kebutuhan, serta menerapkan struktur data Queue dan algoritma Count Sort untuk mengelola dan mengurutkan pesanan secara efektif dan efisien.',
        'manfaat': 'Sistem  ini memberikan kemudahan bagi pengguna dalam mengakses layanan cuci sepatu dengan berbagai opsi sesuai kebutuhan, sekaligus meningkatkan efisiensi pengelolaan urutan pesanan melalui penerapan struktur data dan algoritma yang tepat, sehingga proses layanan menjadi lebih terorganisir, cepat, dan terhindar dari antrean yang tidak teratur.',
        'gambar': ['SDA 1.jpg', 'SDA 2.png', 'SDA 3.jpg', 'SDA 4.jpg'],
        'github': 'https://github.com/MuhamadAlfaRezaGobel23/Proyek-Akhir-Struktur-Data-Algoritma',
        'kolaborasi': 'Kolaborasi Bersama  : Alfathrindra A. Yuliyanto & Rizki Wahyu Widodo',
        'tools': [
            {'nama': 'Python', 'logo': 'python.png'},
            {'nama': 'Canva', 'logo': 'canva.jpeg'},]
    }
}

@app.route('/')
def index():
    return render_template('index.html', semua_proyek=data)

@app.route('/proyek<int:nomor>')
def detail_proyek(nomor):
    proyek = data.get(nomor)
    if proyek:
        return render_template('detail.html', proyek=proyek)
    else:
        return "<h1>Proyek Tidak Ditemukan</h1>", 404


if __name__ == '__main__':
    app.run(debug=True)
