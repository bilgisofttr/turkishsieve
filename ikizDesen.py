import os
import math

def ritmik_resetleme_cift(asallar, baslangiclar, boy):
    n = len(asallar)
    # 1 - Her asal için 1'lerden oluşan matrisi hazırla
    diziler = [[1 for _ in range(boy)] for _ in range(n)]

    # 2 - Her asalı kendi periyodu ve başlangıç değerleriyle sıfırla
    for i in range(n):
        p = asallar[i]
        for start in baslangiclar[i]:
            for j in range(start, boy, p):
                diziler[i][j] = 0

    # Son asal dizisi ve önceki diziler
    son_p_dizisi = diziler[-1]
    onceki_diziler = diziler[:-1]
    
    # İSTATİSTİK: Son kopyalanan dizideki (P_son) filtreleme öncesi tüm sıfırlar
    filtre_oncesi_toplam_sifir = son_p_dizisi.count(0)

    son_dizi_liste = []
    indisler = [] 

    # 3 - Ortak 0'ları 1'e çevirme ve Filtreleme
    for j in range(boy):
        oncekilerde_sifir_var_mi = any(onceki_diziler[i][j] == 0 for i in range(len(onceki_diziler)))
        
        if son_p_dizisi[j] == 0:
            if not oncekilerde_sifir_var_mi:
                son_dizi_liste.append("0")
                indisler.append(j)
            else:
                son_dizi_liste.append("1")
        else:
            son_dizi_liste.append("1")

    son_dizi_str = "".join(son_dizi_liste)
    
    return son_dizi_str, indisler, filtre_oncesi_toplam_sifir

def ritmik_resetleme_genel(asallar, baslangiclar, boy):
    n = len(asallar)
    # 1 - Her asal için 1'lerden oluşan matrisi hazırla
    diziler = [[1 for _ in range(boy)] for _ in range(n)]

    # 2 - Her asalı kendi periyodu ve başlangıç değerleriyle sıfırla
    for i in range(n):
        p = asallar[i]
        for start in baslangiclar[i]:
            for j in range(start, boy, 2*p):
                diziler[i][j] = 0

    # Son asal dizisi ve önceki diziler
    son_p_dizisi = diziler[-1]
    onceki_diziler = diziler[:-1]
    
    # İSTATİSTİK: Son kopyalanan dizideki (P_son) filtreleme öncesi tüm sıfırlar
    filtre_oncesi_toplam_sifir = son_p_dizisi.count(0)

    son_dizi_liste = []
    indisler = [] 

    # 3 - Ortak 0'ları 1'e çevirme ve Filtreleme
    for j in range(boy):
        oncekilerde_sifir_var_mi = any(onceki_diziler[i][j] == 0 for i in range(len(onceki_diziler)))
        
        if son_p_dizisi[j] == 0:
            if not oncekilerde_sifir_var_mi:
                son_dizi_liste.append("0")
                indisler.append(j)
            else:
                son_dizi_liste.append("1")
        else:
            son_dizi_liste.append("1")

    son_dizi_str = "".join(son_dizi_liste)
    
    return son_dizi_str, indisler, filtre_oncesi_toplam_sifir

def lineer_elek_analizi(asallar, baslangiclar, boy):
    n = len(asallar)
    kumulatif_dizi = [1 for _ in range(boy)]
    tablo_verileri = []
    
    # Toplam değerleri hesaplamak için bakiye kutuları
    t_oncekilerle = 0
    t_yeni = 0
    t_toplam_islem = 0

    for i in range(n):
        p = asallar[i]
        oncekilerle_bileşik = 0
        yeni_bileşikler = 0
        
        for start in baslangiclar[i]:
            for j in range(start, boy, p):
                if kumulatif_dizi[j] == 0:
                    oncekilerle_bileşik += 1
                else:
                    yeni_bileşikler += 1
                    kumulatif_dizi[j] = 0 
        
        islem_yuku = oncekilerle_bileşik + yeni_bileşikler
        t_oncekilerle += oncekilerle_bileşik
        t_yeni += yeni_bileşikler
        t_toplam_islem += islem_yuku

        tablo_verileri.append({
            "P": p,
            "Oncekilerle": oncekilerle_bileşik,
            "Yeni": yeni_bileşikler,
            "Toplam": islem_yuku,
            "Kalan": kumulatif_dizi.count(1),
            "Yuzde": (yeni_bileşikler / boy) * 100,
            "Kazanc": (oncekilerle_bileşik / islem_yuku) * 100 if islem_yuku > 0 else 0
        })

    # Genel İstatistikler (TOPLAM satırı için)
    t_eleme_yuzdesi = (t_yeni / boy) * 100 if boy > 0 else 0
    t_kazanc_orani = (t_oncekilerle / t_toplam_islem) * 100 if t_toplam_islem > 0 else 0
    
    toplam_satiri = {
        "Oncekilerle": t_oncekilerle,
        "Yeni": t_yeni,
        "Toplam": t_toplam_islem,
        "Kalan": kumulatif_dizi.count(1), # Son kalan bakiye
        "Yuzde": t_eleme_yuzdesi,
        "Kazanc": t_kazanc_orani
    }

    return tablo_verileri, kumulatif_dizi, toplam_satiri

def konsolu_temizle():
    os.system('cls' if os.name == 'nt' else 'clear')

# Başlatma
konsolu_temizle()

# Parametreler
P = [5,7]  
#İKİZ ASAL DESEN İÇİN
#Ritmik = [[0, 3], [0, 12], [1, 8], [1,10], [2,13], [2,15],[3,18]]
Ritmik = [[0, 3],[0,12]]
IstenenBoy = 5*7
son_dizi, indisler, oncesi_sifir = ritmik_resetleme_cift(P, Ritmik, IstenenBoy)

'''
#KUZEN ASAL DESEN İÇİN
P = [5,7,11,13]
Ritmik = [[0,4],[1,5],[1,9],[2,10]]
IstenenBoy = 5*7*11*13

son_dizi, indisler, oncesi_sifir = ritmik_resetleme_cift(P, Ritmik, IstenenBoy)


#GENEL ASAL DESEN İÇİN
P = [5,7,11,13]
Ritmik = [[0,7],[1,10],[2,17],[3,20]]
IstenenBoy = 2*5*7*11*13
son_dizi, indisler, oncesi_sifir = ritmik_resetleme_genel(P, Ritmik, IstenenBoy)
'''

analiz_sonuclari, final_dizi, t_satir = lineer_elek_analizi(P, Ritmik, IstenenBoy)

girinti = "  "

# --- Sonuçları Göster ---
print(f"{girinti}{'=' * 95}")
print(f"{girinti}(P={P[-1]}) için İKİZ ASAL deseni");
print(f"{girinti}{'-' * 75}")
print(f"{girinti}Son Oluşan Desen:\n{girinti}{son_dizi}")
print(f"{girinti}{'-' * 95}")
#print(f"{girinti}(P={P[-1]}) için lineer eleme indexleri :\n{girinti}{', '.join(map(str, indisler))}")
print(f"{girinti}{'indis sayısı:':<20} {len(indisler)}")
p_metni = " X ".join(map(str, P))
print(f"\n{girinti}DESEN BOYU: {p_metni} = {IstenenBoy}")
print(f"{girinti}{'-' * 35}")
print(f"{girinti}Öncekilerle Ortak: {oncesi_sifir - len(indisler)}")
print(f"{girinti}Yeni Bileşik: {len(indisler)}")
print(f"{girinti}Kalan Elenmemiş: {IstenenBoy - oncesi_sifir}")

print(f"{girinti}{'-' * 95}")
print(f"{girinti}{'P':<5} | {'Önc. Bileşik':<12} | {'Yeni Bileşik':<12} | {'Toplam':<8} | {'Kalan':<8} | {'Eleme %':<8} | {'Kazanç %'}")
print(f"{girinti}{'-' * 95}")

# Satırların yazdırılması
for satir in analiz_sonuclari:
    print(f"{girinti}{satir['P']:<5} | {satir['Oncekilerle']:<12} | {satir['Yeni']:<12} | {satir['Toplam']:<8} | {satir['Kalan']:<8} | %{satir['Yuzde']:<7.2f} | %{satir['Kazanc']:<7.2f}")

# TOPLAM Satırı
print(f"{girinti}{'-' * 95}")
print(f"{girinti}{'TOPLAM':<5} | {t_satir['Oncekilerle']:<12} | {t_satir['Yeni']:<12} | {t_satir['Toplam']:<8} | {t_satir['Kalan']:<8} | %{t_satir['Yuzde']:<7.2f} | %{t_satir['Kazanc']:<7.2f}")
print(f"{girinti}{'=' * 95}")