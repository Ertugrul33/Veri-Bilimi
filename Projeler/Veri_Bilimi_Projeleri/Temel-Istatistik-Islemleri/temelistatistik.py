#!/usr/bin/env python
# coding: utf-8

# In[10]:


def medyan(a):
    a_sirali = sorted(a)
    n = len(a)
    medyan_tek = (n + 1) // 2
    onceki_indeks = n // 2
    sonraki_indeks = (n // 2) + 1
    if len(a) % 2 == 1:
        return a_sirali.__getitem__(medyan_tek - 1)
    else:
        return (a_sirali.__getitem__(onceki_indeks - 1) + a_sirali.__getitem__(sonraki_indeks - 1)) / 2
        
def mod(a):
    b = []
    for i in a:
        b.append(a.count(i))
    for i in a:
        if max(b) == a.count(i):
            return i
        
def degisim_araligi(a):
    return max(a) - min(a)

def ortalama(a):
    toplam = 0
    for i in a:
        toplam += i
    ort = toplam / len(a)
    return ort

def ssapma(a):
    import math
    toplam = 0
    for i in a:
        toplam += (i - ortalama(a))**2
    ss = toplam / (len(a) - 1)
    return math.sqrt(ss)

def varyans(a):
    toplam = 0
    for i in a:
        toplam += (i - ortalama(a))**2
    ss = toplam / (len(a) - 1)
    return ss

def pcarpiklik(a):
    pcarpiklik = (3*(ortalama(a) - medyan(a))) / ssapma(a)
    if pcarpiklik > 0:
        print("Seri pozitif(sağdan) çarpıktır. Sonuç:")
    elif pcarpiklik < 0:
        print("Seri negatif(soldan) çarpıktır. Sonuç:")
    else:
        print("Seri simetriktir. Sonuç:")
    return pcarpiklik
        
        
def basiklik(a):
    toplam = 0
    for i in a:
        toplam += (i - ortalama(a))**4
    m4 = toplam / (len(a) - 1)
    bk = m4 / ssapma(a)**4
    if bk > 3:
        print("Dağılım sivridir. Sonuç:")
    elif bk < 3:
        print("Dağılım basıktır. Sonuç:")
    else:
        print("Dağılım standart normal dağılıma uygundur. Sonuç:")
    return bk