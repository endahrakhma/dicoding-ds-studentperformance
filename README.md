# Proyek Akhir : Menyelesaikan Permasalahan Institusi Pendidikan
## Business Understanding
Jaya Jaya Institut merupakan salah satu institusi pendidikan perguruan yang telah berdiri sejak tahun 2000. Hingga saat ini ia telah mencetak banyak lulusan dengan reputasi yang sangat baik. Akan tetapi, terdapat banyak juga siswa yang tidak menyelesaikan pendidikannya alias dropout.
Jumlah dropout yang tinggi ini tentunya menjadi salah satu masalah yang besar untuk sebuah institusi pendidikan. Oleh karena itu, Jaya Jaya Institut ingin mendeteksi secepat mungkin siswa yang mungkin akan melakukan dropout sehingga dapat diberi bimbingan khusus.
## Permasalahan Bisnis

    
## Cakupan Proyek

  
## Persiapan
Sumber Data : Data berisi rincian demografi, metrik terkait pekerjaan, dan attrition flag berupa label 0 dan 1 [source link](https://github.com/dicodingacademy/dicoding_dataset/tree/main/employee)

Setup Environment :

    a. Setup Environment - Anaconda
        - Create an environment: conda create --name emp-attr python=3.11
        - Activate the environment: conda activate emp-attr
        - Install library: pip install -r requirements.txt
        - launch jupyter notebook
        - executing ML tasks
        
    b. Setup BI tool - Looker Studio
        - Kunjungi: https://lookerstudio.google.com
        - Signing with google account
        - Pilih Blank Report
        - Add data to report: CSV File Upload

ML tasks :

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
    j. Penyimpanan dataset hasil prediksi : exporting CSV File untuk visualisasi dashboard

## Business Dashboard

  Student's Performance Dashboard ini dibuat menggunakan [Looker Studio](https://lookerstudio.google.com/reporting/c1276d50-2499-4481-82b2-cd34b7226983).
  Top 8 fitur penting yang mempengaruhi model, yang mana akan kita fokuskan pada visualisasi dalam dashboard antara lain: 
  
    1. Curricular_units_1st_sem_approved
    2. Tuition_fees_up_to_date
    3. Curricular_units_2nd_sem_evaluations
    4. Age_at_enrollment
    5. Scholarship_holder
    6. Application_mode
    7. Admission_grade
    8. Previous_qualification_grade

#### Kesimpulan
    a. Secara umum, sebagian besar mahasiswa:
    
    b. Dropout sebesar 39,8% atau sebanyak 1762 orang, didominasi oleh:


#### Rekomendasi Aksi
