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