# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 15:48:12 2021

@author: GeTo
"""


# =============================================================================
# 09.04.2021 - ALPER TELLIOGLU PANDAS 

import numpy as np
import pandas as pd

# 1 ile 100 arasındaki çift sayıları yazdırınız.
def EvenNumberFinder():
    for i in range(1,1000):
        if i % 2 == 0:
            print(i)
EvenNumberFinder()
# 1 ile 100 arasındaki tek sayıları yazdırınız.
def OddNumberFinder():
    for i in range(1,1000):
        if i % 2 == 1:
            print(i)
OddNumberFinder()
def Average(a,b):
    return (a+b)/2
Average(3,7)

liste = [1,2,3,4,5]
seri = pd.Series(liste)
IndexList = ["a","b","c","d","e"]
pd.Series(liste, IndexList)
sozluk = {"Ahmet":"Forvet",
          "Veli":"Defans",
          "Eren":"Kaleci"}
sozlukserisi = pd.Series(sozluk)
seri.dtypes
seri.is_unique # ATTRIBUTE
seri.size
seri.shape
seri.head() # METHOD
seri.describe()
sozlukserisi.describe()
def toplama(sayi1,sayi2):
    return sayi1 + sayi2 # sayi1, sayi2 PARAMETRE
toplama(5,3)

?pd.Series

employers = ["Ali","Veli","Deniz"]
salary = [1000,2000,1000]
pd.Series(employers,salary)

pd.read_csv("taylorswift_ibotatlises_challenge.csv")
pd.read_csv("kumbara_gunler.csv", usecols=["Günler"], squeeze=True)
# "Günler" kolonunu dataframe yerine series olarak okutmuş olduk. 

liste = [12,2,3,42,43]
listeseri = pd.Series(liste)
len(liste) # BUILT-IN FUNCTIONS pandas serieste de kullanılır.
sorted(seri)
?listeseri.sort_values
listeseri.sort_values(ascending=False)
listeseri.sort_values(inplace=True)
listeseri
listeseri.sort_index(inplace=True)
listeseri

# Seri ve Liste Farklılıkları
liste
liste[2]
listeseri[2]
gun_kumbara = pd.read_csv("kumbara_gunler.csv", squeeze=True)
gun_kumbara.head()
gun_kumbara[-20:-10]
"Pazartesi" in gun_kumbara.values
gunler_serisi = pd.read_csv("kumbara_gunler.csv", index_col = "Günler", squeeze=True)
gunler_serisi["Pazartesi"]
gunler_serisi.get([0,10])
gunler_serisi.get("Monday", default = "Aradığınız kelime bu seride yok")
# type(None)

# Max Min Ozellikleri
randListe = [5,7,9,8,3,8,4,8,2]
seri_randListe = pd.Series(randListe)
max(randListe)
min(randListe)
seri_randListe

maxSayi = 0
for i in seri_randListe:
    if maxSayi < i:
        maxSayi = i
maxSayi

minSayi = 100
for i in seri_randListe:
    if minSayi > i:
        minSayi = i
minSayi

seri_randListe.max()
seri_randListe.min()
seri_randListe.idxmax() # en yüksek değer hangi indexte

def ikiEkle(sayi): # değere iki ekleyen function
    return sayi + 2
sayi = 5
ikiEkle(sayi)

seri_randListe.apply(ikiEkle)
seri_randListe

def stringeCevir(i):
    if i == 1:
        return "bir"
    elif i == 2:
        return "iki"

seri_randListe.apply(stringeCevir)

employers = ["Ali","Veli","Deniz","Gamze","Gizem","Fatih"]
employersSeries = pd.Series(employers)

kura_sonucu = {"Ali":5,"Veli":4,"Deniz":3,"Gamze":2,"Gizem":1,"Fatih":0}
kuraSerisi = pd.Series(kura_sonucu)

kuraSerisi.map(employersSeries)

# DATAFRAME
pd.set_option('display.max_columns', None)

df = pd.read_csv("calisan_data.csv") # veriyi kaggledan aldık
df

df.isnull().sum() # NaN değer sayısı, toplam NaN sayısı için sona bir sum() daha eklenecek
df.shape
df.head()
type(df)

matris = df.values
matris
type(matris)

df.Isimler[5]
df.dtypes
df.describe()
df.describe().T
df.columns
df.info()
df.DogumTarihi # boşluklu değerli olsaydı sütunu df["Dogum Tarihi"] olarak çağıracaktık.
df.rename(columns={"DogumTarihi":"Dogum Tarihi"}, inplace=True) # sütun adını kalıcı olarak değiştirdik.
df["Dogum Tarihi"]

df[["Dogum Tarihi","Maas"]]

df.rename(columns={"Dogum Tarihi":"DogumTarihi"}, inplace=True)

toplamMaas = 0 # Challenge: Toplam Maasi bul
for i in df.Maas:
    toplamMaas += i    
toplamMaas

df.Maas.sum() # Challenge: Toplam Maasi bul

kullaniciAdlari = [] # Challenge: Her Çalışana bir Kullanıcı Ada Ata
for i in range(0, len(df)): 
    kullaniciAdlari.append(df.Isimler[i] + df.Soyisimler[i])
kullaniciAdlari

df["kullaniciAdi"] = kullaniciAdlari # Kullanici Adlarini yeni sütun olarak SONA ekledik
df

df.insert(loc=2, column="kullaniciAdlari2", value=kullaniciAdlari) 
df #Kullanici adlarini loc ile 2. index sütunu olarak ekledik, kalan sütunlar sağa kaydı.

# MATEMATIKSEL ISLEMLER

df["Maas"].add(1000) 
df["Maas"].sub(2000)
df["Maas"].mul(1.2)
averageMaas = df["Maas"].mean()
averageMaas

# NULL DEGERLER

df = pd.read_csv("netflix_titles.csv")
df.head()
df.info()
# df.dropna() tüm NaN degerler listeden çıktı.
# dropna parametrelerinden how=all olarak ayarlarsak tüm satır boş ise siler. default any.
# dropna axis="columns" ile boş kolonu siler.
df["director"].fillna("Yönetmen bilinmiyor", inplace=True) # null hücreleri istenen metinle değiştirdik.

df.sort_values("release_year", ascending=False) # release_year'ı baz alarak yeniden eskiye göre sıraladık, nulları sona atar.
# na_position parametresiyle null değerlerin pozisyonları ayarlanabilir, default'u last.
# =============================================================================