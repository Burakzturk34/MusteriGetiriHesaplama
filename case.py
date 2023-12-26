#############################################
# Kural Tabanlı Sınıflandırma ile Potansiyel Müşteri Getirisi Hesaplama
#############################################

#############################################
# İş Problemi
#############################################
# Gezinomi yaptığı satışların bazı özelliklerini kullanarak seviye tabanlı (level based) yeni satış tanımları
# oluşturmak ve bu yeni satış tanımlarına göre segmentler oluşturup bu segmentlere göre yeni gelebilecek müşterilerin şirkete
# ortalama ne kadar kazandırabileceğini tahmin etmek istemektedir.
# Örneğin: Antalya’dan Herşey Dahil bir otele yoğun bir dönemde gitmek isteyen bir müşterinin ortalama ne kadar kazandırabileceği belirlenmek isteniyor.
#############################################
# PROJE GÖREVLERİ
#############################################

#############################################
# GÖREV 1: Aşağıdaki soruları yanıtlayınız.
#############################################

# Soru 1: miuul_gezinomi.xlsx dosyasını okutunuz ve veri seti ile ilgili genel bilgileri gösteriniz.
import pandas as pd
#pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)
pd.set_option('display.float_format', lambda x: '%.2f' % x)
df_ = pd.read_excel('dataset/miuul_gezinomi.xlsx')
df = df_.copy()
print(df.head())
print(df.shape)
print(df.info())


# Soru 2: Kaç unique şehir vardır? Frekansları nedir?
print(df["SaleCityName"].nunique())
print(df["SaleCityName"].value_counts())

# Soru 3: Kaç unique Concept vardır?
df["ConceptName"].nunique()

# Soru 4: Hangi Concept'dan kaçar tane satış gerçekleşmiş?k
df["ConceptName"].value_counts()

# Soru 5: Şehirlere göre satışlardan toplam ne kadar kazanılmış?
df.groupby("SaleCityName").agg({"Price": "sum"})

# Soru 6: Concept türlerine göre göre ne kadar kazanılmış?
df.groupby("ConceptName").agg({"Price": "sum"})

# Soru 7: Şehirlere göre PRICE ortalamaları nedir?
df.groupby(by=['SaleCityName']).agg({"Price": "mean"})

# Soru 8: Conceptlere  göre PRICE ortalamaları nedir?
df.groupby(by=['ConceptName']).agg({"Price": "mean"})

# Soru 9: Şehir-Concept kırılımında PRICE ortalamaları nedir?
df.groupby(by=["SaleCityName", 'ConceptName']).agg({"Price": "mean"})