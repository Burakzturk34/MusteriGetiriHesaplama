# Kural Tabanlı Sınıflandırma ile Potansiyel Müşteri Getirisi Hesaplama

Bu proje, Gezinomi'nin yaptığı satışlar üzerinden bazı özellikleri kullanarak seviye tabanlı yeni satış tanımları oluşturmayı ve bu tanımlara göre müşteri segmentlerini belirlemeyi amaçlamaktadır. Ayrıca, bu segmentlere göre gelebilecek yeni müşterilerin şirkete ortalama ne kadar kazandırabileceğini tahmin etmeyi hedefler.

## İş Problemi

Gezinomi, satışlarının özelliklerini kullanarak yeni satış tanımları oluşturmak ve bu tanımlara göre müşteri segmentleri belirlemek istiyor. Örneğin, Antalya'dan Herşey Dahil bir otele yoğun bir dönemde gitmek isteyen bir müşterinin ortalama ne kadar kazandırabileceği belirlenmek isteniyor.

## Proje Görevleri

### Görev 1: Veri Seti Analizi
- `miuul_gezinomi.xlsx` dosyası okunur ve genel veri seti bilgileri görüntülenir.
- Kaç farklı şehir olduğu ve frekansları, kaç farklı konsept olduğu gibi temel istatistikler hesaplanır.

### Görev 2: Yeni Kategorik Değişken Oluşturma
- `satis_checkin_day_diff` değişkeni `EB_Score` adında yeni bir kategorik değişkene dönüştürülür.

### Görev 3: Şehir, Konsept, ve EB_Score Analizi
- Şehir, Konsept ve `EB_Score` kırılımında ücret ortalamalarına ve frekanslarına bakılır.

### Görev 4: Sıralama ve İndeks Adlandırma
- Şehir, Konsept ve Sezon kırılımında ücret ortalamalarına göre sıralama yapılır.
- İndeks adları değişken adlarına dönüştürülür.

### Görev 5: Yeni Satış Tanımları
- Yeni level-based satış tanımları oluşturulur ve veri setine eklenir.

### Görev 6: Müşteri Segmentasyonu
- Müşteriler, ücretlerine göre segmentlere ayrılır ve bu segmentler analiz edilir.

### Görev 7: Sıralama ve Segment Bilgileri
- Oluşan son dataframe, ücret değişkenine göre sıralanır.
- Örnek bir kullanıcı ("ANTALYA_HERŞEY DAHIL_HIGH") hangi segmentte yer alıyor ve ne kadar ücret bekleniyor analiz edilir.

## Kullanım

Projeyi çalıştırmak için aşağıdaki adımları takip edin:
1. `miuul_gezinomi.xlsx` dosyasını projenin ana dizinine yerleştirin.
2. Python ortamınızda gerekli kütüphaneleri yükleyin.
   ```bash
   pip install pandas
