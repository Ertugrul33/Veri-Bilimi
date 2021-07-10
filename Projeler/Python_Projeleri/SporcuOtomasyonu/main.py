# -*- coding: utf-8 -*-
"""
Created on Sun Jul  4 20:08:59 2021

@author: lenovo
"""

#-----------------KÜTÜPHANE---------------
#-----------------------------------------

import sys
from PyQt5 import QtWidgets #Formda oluşturulan tüm Widget'lar QtWidgets class'ından türediği için bu sınıfı import ettik.
from PyQt5.QtWidgets import * #QtWidgets class'ındaki tüm fonskyonları import ettik.
from AnaSayfaUI import *

#-------------UYGULAMA OLUŞTUR------------
#-----------------------------------------

Uygulama=QApplication(sys.argv)
#Formda oluşturduğumuz argümanları aldık ve bu class'a parametre olarak verdik.
#Yani biz diyoruz ki: bir uygulama oluştur ve kod içerisindeki argümanlar bu uygulamaya parametre olarak verilebilsin diyoruz.

penAna=QMainWindow() #Bir pencere oluşturduk.
ui=Ui_MainWindow() #Widgetları eklediğimiz tasarım formun yani ana formun obje ismini aldık ve bu formu kullanabilmek için nesne olarak bir değişkene atadık.
#Yani tasarımımız için form oluşturmuştuk ve bu formdaki widgetlara erişirken ve kullanırken bu "ui" adlı değişkenle erişmiş olacağız.

ui.setupUi(penAna) #penAna isminde oluşturduğumuz pencereyi, tasarım olarak yapmış olduğumuz pencereyi birleştirmiş olduk.
penAna.show()

#-------------VERİTABANI OLUŞTUR----------
#-----------------------------------------

import sqlite3 #Python ile kullanılan veritabanı hızlı ve Python'ı desteklediği için genelde sqlite3'tir. 
global curs
global conn
conn=sqlite3.connect('sporcular.db') #Eğer böyle bir veritabanı varsa ona bağlanacak, yoksa otomatik oluşturulacaktır.
curs=conn.cursor() #Bu fonksiyon veritabanı ile dialog kurmamız açısından önemlidir. Yeni bir sorgu çalıştırmak istediğimizde bu nesneyi(curs) kullanacağız.
sorguCreTblSpor=("CREATE TABLE IF NOT EXISTS spor(               \
                 ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,  \
                 TCNo TEXT NOT NULL UNIQUE,                      \
                 SporcuAdi TEXT NOT NULL,                        \
                 SporcuSoyadi TEXT NOT NULL,                     \
                 KulupAdi TEXT NOT NULL,                         \
                 Brans TEXT NOT NULL,                            \
                 Cinsiyet TEXT NOT NULL,                         \
                 DTarihi TEXT NOT NULL,                          \
                 MHal TEXT NOT NULL,                             \
                 Kilo TEXT NOT NULL)")
curs.execute(sorguCreTblSpor) #SQL sorgusu yazacağımız kısımdır.
conn.commit() #Veritabanı ile bağlantı kurmaya yarar.



sys.exit(Uygulama.exec_()) #Uygulamadan çıkarken tüm işlemleri sonlandır demektir.






