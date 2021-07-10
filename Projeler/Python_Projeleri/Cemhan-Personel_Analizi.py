# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 10:19:35 2021

@author: senol
"""

import pandas as pd
import numpy as np
class Personel_Analizi:
    def __init__(self,path):
        self.data = pd.read_csv((path), sep=" ", names=['ad','soyad','yas'])

    def bilgileri_al(self):
        ad = list(self.data['ad'])
        soyad = list(self.data['soyad'])
        yas = list(self.data['yas'])
        return ad,soyad,yas
    
    def ortalama(self):
        yas1 = self.bilgileri_al()[2]
        return np.mean(yas1)
    
    def alfabetik_siralama(self):
        soyad1 = self.bilgileri_al()[1]
        return sorted(soyad1)
    
    def isim_sayisi(self):
        ad1 = self.bilgileri_al()[0]
        return dict(pd.Series(ad1).value_counts())

    def bastir(self):
        alf_s = self.alfabetik_siralama()
        is_s = self.isim_sayisi()
        ort = self.ortalama()
        
        print('Alfabetik Siralama : {}'.format(alf_s))
        print(' ')
        print('Isim Sayisi : {}'.format(is_s))
        print(' ')
        print('Yas Ortalamasi : {}'.format(ort))
        
#%% Sonuc

pa = Personel_Analizi('personel_grup1.txt')
pa.bastir()