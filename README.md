# Proyek Akhir : Menyelesaikan Permasalahan Institusi Pendidikan
## Business Understanding
Jaya Jaya Institut merupakan salah satu institusi pendidikan perguruan yang telah berdiri sejak tahun 2000. Hingga saat ini ia telah mencetak banyak lulusan dengan reputasi yang sangat baik. Akan tetapi, terdapat banyak juga siswa yang tidak menyelesaikan pendidikannya alias dropout.
## Permasalahan Bisnis
Jumlah dropout yang tinggi ini tentunya menjadi salah satu masalah yang besar untuk sebuah institusi pendidikan. Oleh karena itu, Jaya Jaya Institut ingin mendeteksi secepat mungkin siswa yang mungkin akan melakukan dropout sehingga dapat diberi bimbingan khusus.
## Cakupan Proyek
Setelah memahami permasalahan yang dihadapi, maka kita kumpulkan data yang diperlukan dan memahaminya sehingga dapat memformulasikan masalah menjadi bentuk ML tasks hingga menghasilkan sebuah dataset baru dengan label status yang lengkap melalui model klasifikasi terbaik yang telah diuji. Dataset baru tersebut digunakan membangun dashboard untuk membantu Jaya Jaya Institut dalam memahami data dan memonitor performa siswa dengan menggunakan Looker Studio sebagai BI tool-nya. Selain itu juga mengembangkan solusi machine learning yang siap digunakan oleh user dalam bentuk prototype yang dibuat menggunakan streamlit dan menghubungkan prototype tersebut dengan Streamlit Community Cloud sehingga ia dapat dijalankan pada environment cloud dan diakses secara remote. 
## Persiapan
[Sumber Data](https://github.com/dicodingacademy/dicoding_dataset/tree/main/students_performance) : Dataset yang dibuat dari lembaga pendidikan tinggi yang terkait dengan mahasiswa yang terdaftar dalam berbagai gelar sarjana, seperti agronomi, desain, pendidikan, keperawatan, jurnalisme, manajemen, layanan sosial, dan teknologi. Dataset tersebut mencakup informasi yang diketahui pada saat pendaftaran mahasiswa (jalur akademik, demografi, dan faktor sosial-ekonomi) dan kinerja akademik mahasiswa pada akhir semester pertama dan kedua. Data tersebut digunakan untuk membangun model klasifikasi guna memprediksi putus kuliah (dropout) dan keberhasilan akademik (graduate) mahasiswa.

Setup Environment :

    a. Setup Environment - Anaconda
        - Create an environment: conda create --name std-perform python=3.11
        - Activate the environment: conda activate std-perform
        - Install library: pip install -r requirements.txt
        - launch jupyter notebook
        - executing ML tasks
        
    b. Setup BI tool - Looker Studio
        - Kunjungi: https://lookerstudio.google.com
        - Signing with google account
        - Pilih Blank Report
        - Add data to report: CSV File Upload (dataset baru : studentperformance_final.csv)

## Menjalankan Sistem Machine Learning
    - Buat script python filename app.py melalui code editor (saya menggunakan spyder)
    - Import library streamlit dan dependencies lainnya
    - Load model yang telah disimpan setelah menyelesaikan ML tasks
    - Terapkan top 8 fitur penting yang dibutuhkan model sebagai interaksi user
    - Lakukan prediksi status mahasiswa melalui interaksi tombol
    - Running di lokal : streamlit run app.py
    - Siapkan file requirements.txt berisi library sekaligus versinya yang digunakan untuk membangun aplikasi tersebut
    - Jika berhasil running di lokal, deploy ke Streamlit Community Cloud
    
Visit web app : [https://studentsperformance-endahrakhma.streamlit.app/](https://studentsperformance-endahrakhma.streamlit.app/)

Detail ML tasks :

    a. Data Collection dan Data Understanding
    b. Exploratory Data Analysis (EDA) : univariate analysis
    c. Data Preprocessing : Feature Engineering, encoding, outlier handling, feature scaling
    d. Modeling : splitting data, model selection (memilih algoritma ML classifier yang tepat)
    e. Evaluasi : confussion matrix (accuracy dan f1-score)
    f. Optimasi model : hyperparameter tuning, gridSearchCV
    g. Feature Importance : menentukan top 8 fitur penting dalam model 
    h. Membuat pipeline model yang digunakan
    h. Penyimpanan model : format .pkl
    i. Implementasi model : prediksi status mahasiswa
    j. Penyimpanan dataset baru : exporting CSV File untuk visualisasi dashboard
    g. Deployment : create status prediction web app dengan tool streamlit

## Business Dashboard
  Student's Performance Dashboard ini dibuat menggunakan [Looker Studio](https://lookerstudio.google.com/reporting/c1276d50-2499-4481-82b2-cd34b7226983).
  Top 8 fitur penting yang mempengaruhi prediksi status student's academic performance oleh model, yang mana akan kita fokuskan pada visualisasi dalam dashboard antara lain: 
  
    1. Curricular_units_1st_sem_approved
    2. Tuition_fees_up_to_date
    3. Curricular_units_2nd_sem_evaluations
    4. Age_at_enrollment
    5. Scholarship_holder
    6. Application_mode
    7. Admission_grade
    8. Previous_qualification_grade

#### Kesimpulan
    a. Total mahasiswa 4424 orang, terdiri dari graduate sebanyak 2662 orang (60.2%) dan dropout sebanyak 1762 orang (39.8%).
        Didominasi oleh:
        - Gender : Female
        - Age at enrollment : 15-20
        - Marital status : Single
        - Top 3 courses : Nursing, Management, Social Service
        - Tuition fees up to date : Yes
        - Scholarship holder : No
        - Debtor : No
        - Application mode : 1st phase - general contingent
        - Admission grade : 100-150
        - Previous qualification grade : 100-150
        - Curricular units 1st semester (approved) : 0-10
        - Curricular units 2nd semester (evaluations) : 0-10
        
    b. Dropout sebesar 39.8% atau sebanyak 1762 orang, didominasi oleh:
        - Gender : Female
        - Tuition fees up to date : Yes
        - Scholarship holder : No
        - Debtor : No
        
        Persentase dropout diatas graduate atau lebih dari 50%:
        - Age at enrollment diatas 20 tahun
        - Marital status selain Single
        - Kursus Management
        - Application mode : Over 23 years old
        - Admission grade : 50-100
        - Previous qualification grade : 50-100
        - Curricular units 1st semester (approved) : 0-10
        - Curricular units 2nd semester (evaluations) : 11-20
        
## Rekomendasi Aksi
1. Early warning system: Identifikasi mahasiswa berisiko DO (admission grade dan previous qualification grade bernilai kecil 50-100).
2. SKS mahasiswa pada semester 1 yang disetujui jumlahnya 0-10, akan membutuhkan waktu jauh lebih lama untuk lulus. Hal ini bisa menyebabkan kelelahan mental, frustrasi, dan hilangnya motivasi. Dampak lainnya masa studi yang makin panjang maka biaya hidup dan kuliah semakin besar, apalagi mahasiswa bukan penerima beasiswa ataupun tidak mau jadi peminjam (debitur) dengan tuition fees yang up to date (biaya kuliah terkini).
3. Meringankan beban finansial agar mahasiswa (terutama age at enrollment diatas 20 tahun maupun yang pernikahannya problematik selain status single) bisa fokus menyelesaikan kuliah dengan memberikan kemudahan administratif seperti potongan biaya kuliah, cicilan UKT, atau penghapusan denda keterlambatan.
4. Evaluasi SKS mahasiswa pada semester 2 yang berjumlah 0-10 jumlah dropout-nya diatas 50%, 11-20 jumlah dropout diatas graduate. Semakin banyak SKS yang dievaluasi semakin besar mahasiswa yang dropout. Peluang mahasiswa memperbaiki IPK secara cepat akan terbatas. Mahasiswa yang hanya diizinkan mengambil sedikit SKS pada semester 2 karena IP rendah, akan kesulitan mengejar target lulus tepat waktu.
5. Memberi kelas remedial/mata kuliah pengganti antarsemester agar mahasiswa bisa memperbaiki IP dan menambah SKS.
6. Pendampingan intensif bagi mahasiswa berisiko agar mereka bisa kembali ke jalur normal. Buat program asistensi atau mentoring akademik (senior membimbing junior)
7. Pada kursus Management yang persentase dropout-nya lebih besar dari graduate (kursus populer kedua), pihak kampus perlu melakukan survey mahasiswa: kesulitan materi, metode ajar, beban tugas, atau gaya mengajar dosen. Jika perlu, rotasi dosen pengampu atau hadirkan dosen tamu/praktisi sebagai pendamping.
8. Tinjau ulang apakah beban SKS, cakupan materi, dan prasyarat mata kuliah sudah sesuai. Pecah mata kuliah besar jadi dua tahap (misal: "Matematika Lanjut 1" dan "2").
