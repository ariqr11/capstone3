# **E-COMMERCE CUSTOMER CHURN**

## **Context**
Perusahaan ritel online (E-commerce) merupakan tempat di mana penjual dan pelanggan dapat melakukan transaksi melalui situs web atau aplikasi seluler. Perusahaan ini memperoleh keuntungan dari setiap transaksi yang dilakukan oleh pelanggan, sehingga pertumbuhan jumlah pelanggan sangat penting agar perusahaan dapat meningkatkan keuntungannya. Perusahaan ritel online (E-commerce) ingin mengetahui pelanggan yang akan beralih, sehingga mereka dapat mendekati pelanggan untuk menawarkan beberapa promo yang sesuai.

## **Problem Statement**
E-commerce perlu mengidentifikasi tingkat customer churn untuk mengurangi kerugian pendapatan yang mungkin terjadi. Maka dari itu, e-commerce perlu melakukan prediksi pelanggan sebelum mereka benar-benar meninggalkan layanan, sehingga e-commerce dapat memberikan layanan yang lebih baik kepada pelanggan, seperti menawarkan promosi yang menarik. Namun, penting juga untuk memastikan bahwa promosi tersebut disampaikan kepada orang yang tepat. Dengan melakukan hal ini, perusahaan dapat menghindari kerugian pendapatan akibat kehilangan pelanggan.

## **Goals**
- Mengembangkan model prediksi yang dapat mengidentifikasi pelanggan yang berpotensi akan churn sebelum mereka benar-benar meninggalkan layanan. 
- Mengoptimalisasi strategi promosi dengan memastikan bahwa promosi hanya diberikan kepada pelanggan yang memiliki probabilitas tinggi untuk memanfaatkannya.

## **Analytic Approach**
Pendekatan kami akan terfokus pada dua langkah utama. Pertama, kami akan mengembangkan model prediksi churn dengan menggunakan data pelanggan historis untuk mengidentifikasi pelanggan yang berpotensi akan churn sebelum mereka benar-benar meninggalkan layanan. Kedua, kami akan mengoptimalkan strategi promosi dengan menerapkan segmentasi pelanggan dan menggunakan model probabilitas pemanfaatan promosi untuk memastikan bahwa promosi hanya diberikan kepada pelanggan yang memiliki probabilitas tinggi untuk memanfaatkannya, meningkatkan efisiensi dan efektivitas promosi.

## **Metric Evaluation**

- (TP) True Positive: Model memprediksi pelanggan churn dan memang hasilnya churn
- (FP) False Positive: Model memprediksi pelanggan churn, namun ternyata realitanya tidak churn
- (FN) False Negative: Model memprediksi pelanggan tidak churn, namun ternyata realitanya churn
- (TN) True Negative: Model memprediksi pelanggan tidak churn dan memang hasilnya tidak churn
  
Dapat dilihat dari metric diatas, ada beberapa nilai False. Berikut analisis dari kesalahan prediksi tersebut:

**Type 1 error: False Positive**
  - Promosi diberikan kepada pelanggan yang sebenarnya tidak memerlukan promosi. Ini dapat mengakibatkan menurunnya profit dari produknya.
  - Memberikan promo akan merugi sekitar $100 per orangnya

**Type 2 error: False Negative**
  - Pelanggan yang seharusnya mendapatkan promosi atau perhatian khusus tidak menerima hal tersebut, dan ini bisa berdampak negatif karena mereka mungkin benar-benar meninggalkan layanan yang artinya tidak ada profit dari pelanggan tersebut.
  - Kehilangan customer secara keseluruhan akan merugi sekitar $250 per orangnya karena tidak membeli produk


Berdasarkan penjelasan diatas, FP dan FN keduanya akan merugikan perusahaan apabila terjadi. Namun, kerugian yang dialami oleh perusahaan akan lebih parah jika FN lebih banyak dibanding FP. Maka dari itu, model ini tetap mementingkan keduanya namun lebih mementingkan FN dan pada akhirnya scoring yang dipilih adalah **F2 Score** yang artinya FN lebih merugikan 2x dibandingkan FP.

## **Data Understanding**

Source Data : [DATA ECOMMERCE CUSTOMER CHURN](https://www.kaggle.com/datasets/ankitverma2010/ecommerce-customer-churn-analysis-and-prediction)

**Target** : **Churn** (0 : Tidak Churn , 1 : Churn)

| **Features** | **Description** |
| --- | --- |
| Tenure | Waktu customer menggunakan layanan |
| WarehouseToHome | Jarak dari gudang ke rumah customer |
| NumberOfDeviceRegistered | Total device yang didaftarkan oleh customer |
| PreferedOrderCat | Kategori pilihan dalam satu bulan terakhir |
| SatisfactionScore | Kepuasan customer (range 1-5) |
| MaritalStatus | Status pernikahan customer |
| NumberOfAddress | Total alamat yang didaftarkan oleh customer |
| Complaint | Komplain dalam satu bulan terakhir (0 : tidak ada, 1: ada) |
| DaySinceLastOrder | Berapa hari setelah transaksi terakhir |
| CashbackAmount | Cashback rata-rata dalam satu bulan terakhir |

## **Project Explanation**
Pada project ini, akan dilakukan benchmarking dengan berbagai model seperti Decision Tree Classifier, Logistic Regression, XGBoost Classifier, RandomForest, dan lainnya untuk mengidentifikasi model terbaik. Model terbaik yang dipilih akan menjalani proses hyperparameter tuning guna meningkatkan performanya. Setelah proses tuning, model tersebut akan diuji pada data tes untuk mengukur apakah model tersebut cenderung overfitting atau tidak. Selanjutnya, fokus analisis akan difokuskan pada model dengan hyperparameter tuning terbaik, dengan tujuan mengevaluasi efisiensi machine learning terhadap pengeluaran perusahaan. Selama analisis, akan diidentifikasi pula fitur-fitur yang memiliki dampak paling signifikan dalam memprediksi apakah seorang pelanggan akan melakukan churn atau tidak. Pada akhirnya, model yang telah dihasilkan akan disimpan dan dapat di-load kembali untuk memprediksi data pelanggan baru. Semua proses ini dapat lebih rinci ditemukan dalam Jupiter Notebook yang tersedia di repository project ini.