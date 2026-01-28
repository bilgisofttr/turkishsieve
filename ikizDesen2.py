import os
girinti = "  " # 2 karakter boşluk

def ritmik_resetleme_final_and_eklentili(asallar, baslangiclar, boy):
    n = len(asallar)
    girinti = "  "
    # 1 - Her asal için 1'lerden oluşan matrisi hazırla
    diziler = [[1 for _ in range(boy)] for _ in range(n)]

    # 2 - Her asalı kendi periyodu ve başlangıç değerleriyle sıfırla
    for i in range(n):
        p = asallar[i]
        for start in baslangiclar[i]:
            for j in range(start, boy, p):
                diziler[i][j] = 0
        print(f"{girinti}{p} için Oluşan Desen:\n{girinti}{diziler[i]}")

    # --- YENİ EKLENTİ: TÜM DESENLERİN AND EDİLMİŞ HALİ ---
    # Başlangıçta hepsi 1 (True), herhangi bir asal 0 yaparsa o nokta 0 olur
    and_sonuc_dizisi = [1 for _ in range(boy)]
    for j in range(boy):
        for i in range(n):
            if diziler[i][j] == 0:
                and_sonuc_dizisi[j] = 0
                break # Bir tane 0 bulması yeterli (AND mantığı)
    
    print(f"\n{girinti}TÜM DESENLERİN AND EDİLMİŞ HALİ (Kümülatif Maske):")
    print(f"{girinti}{and_sonuc_dizisi}")
    # ----------------------------------------------------

    son_p_dizisi = diziler[-1]
    onceki_diziler = diziler[:-1]
    filtre_oncesi_toplam_sifir = son_p_dizisi.count(0)

    son_dizi_liste = []
    sifir_indisleri = []

    # 3 - Ortak 0'ları 1'e çevirme ve Filtreleme
    for j in range(boy):
        oncekilerde_sifir_var_mi = any(onceki_diziler[i][j] == 0 for i in range(len(onceki_diziler)))
        if son_p_dizisi[j] == 0:
            if not oncekilerde_sifir_var_mi:
                son_dizi_liste.append("0")
                sifir_indisleri.append(j)
            else:
                son_dizi_liste.append("1") # Daha önce elenmişse resetlemeyi iptal et (Kazanç)
        else:
            son_dizi_liste.append("1")

    son_dizi_str = "".join(son_dizi_liste)
    return son_dizi_str, sifir_indisleri, filtre_oncesi_toplam_sifir

def ritmik_resetleme_final_bit_tabanli(asallar, baslangiclar, boy):
    n = len(asallar)
    
    # Her asal için bit dizilerini (string olarak) oluşturacağız
    # Başlangıçta hepsi '1' (bitişik bitler)
    bit_dizileri = []

    for i in range(n):
        p = asallar[i]
        # Geçici bir liste oluştur (manipülasyon için)
        temp_liste = [1] * boy
        for start in baslangiclar[i]:
            for j in range(start, boy, 2*p):
                temp_liste[j] = 0
        
        # Bitleri yan yana string olarak birleştir
        bit_str = "".join(map(str, temp_liste))
        bit_dizileri.append(bit_str)
        print(f"P={p:2} Bit Dizisi: {bit_str}")

    # --- TÜM BİTLERİN AND EDİLMİŞ (BİTİŞİK) HALİ ---
    and_sonuc_liste = []
    for j in range(boy):
        # Tüm asalların j. bitini kontrol et
        bit_and = 1
        for i in range(n):
            if bit_dizileri[i][j] == '0':
                bit_and = 0
                break
        and_sonuc_liste.append(str(bit_and))
    
    and_sonuc_bit_str = "".join(and_sonuc_liste)
    print(f"\nKÜMÜLATİF AND MASKESİ (BİTİŞİK): {and_sonuc_bit_str}")
    
    return and_sonuc_bit_str

def ritmik_resetleme_final(asallar, baslangiclar, boy):
    n = len(asallar)
    # 1 - Her asal için 1'lerden oluşan matrisi hazırla
    diziler = [[1 for _ in range(boy)] for _ in range(n)]

    # 2 - Her asalı kendi periyodu ve başlangıç değerleriyle sıfırla
    for i in range(n):
        p = asallar[i]
        for start in baslangiclar[i]:
            for j in range(start, boy, p):
                diziler[i][j] = 0
        print(f"{girinti}{p} için Oluşan Desen:\n{girinti}{diziler[i]}")
    # Son asal dizisi ve önceki diziler
    son_p_dizisi = diziler[-1]
    onceki_diziler = diziler[:-1]
    
    # İSTATİSTİK: Son kopyalanan dizideki (P_son) filtreleme öncesi tüm sıfırlar
    filtre_oncesi_toplam_sifir = son_p_dizisi.count(0)

    son_dizi_liste = []
    sifir_indisleri = []

    # 3 - Ortak 0'ları 1'e çevirme ve Filtreleme
    for j in range(boy):
        oncekilerde_sifir_var_mi = any(onceki_diziler[i][j] == 0 for i in range(len(onceki_diziler)))
        if son_p_dizisi[j] == 0:
            if not oncekilerde_sifir_var_mi:
                # Sadece sonuncuya özgü 0'lar kalır
                son_dizi_liste.append("0")
                sifir_indisleri.append(j)
            else:
                # Ortak olanlar 1 yapılır
                son_dizi_liste.append("1")
        else:
            son_dizi_liste.append("1")

    son_dizi_str = "".join(son_dizi_liste)
    
    return son_dizi_str, sifir_indisleri, filtre_oncesi_toplam_sifir

def lineer_elek_analizi(asallar, baslangiclar, boy):
    n = len(asallar)
    # Başlangıçta hepsi elenmemiş (1)
    # Tek bir dizi üzerinden kümülatif gitmek istatistiği doğru verir
    kumulatif_dizi = [1 for _ in range(boy)]
    
    tablo_verileri = []

    for i in range(n):
        p = asallar[i]
        oncekilerle_bileşik = 0
        yeni_bileşikler = 0
        
        # Bu asala ait geçici bir dizi oluşturup sadece bu asalın etkisine bakıyoruz
        # (Senin önceki istediğin "son p hariç" mantığıyla uyumlu)
        for start in baslangiclar[i]:
            for j in range(start, boy, p):
                if kumulatif_dizi[j] == 0:
                    oncekilerle_bileşik += 1
                else:
                    yeni_bileşikler += 1
                    kumulatif_dizi[j] = 0 # Yeni elendi
        
        toplam_bileşik = oncekilerle_bileşik + yeni_bileşikler
        kalan_elenmemis = kumulatif_dizi.count(1)
        eleme_yuzdesi = (yeni_bileşikler / boy) * 100 if boy > 0 else 0
        
        tablo_verileri.append({
            "P": p,
            "Oncekilerle": oncekilerle_bileşik,
            "Yeni": yeni_bileşikler,
            "Toplam": toplam_bileşik,
            "Kalan": kalan_elenmemis,
            "Yuzde": eleme_yuzdesi
        })

    return tablo_verileri, kumulatif_dizi

def konsolu_temizle():
    # Windows için 'nt', Linux ve Mac için 'posix' kullanılır
    os.system('cls' if os.name == 'nt' else 'clear')
konsolu_temizle()

'''
# Parametreler
P = [5,7]  
#İKİZ ASAL DESEN İÇİN
#Ritmik = [[0, 3], [0, 12], [1, 8], [1,10], [2,13], [2,15],[3,18]]
Ritmik = [[0, 3],[0,12]]
IstenenBoy = 5*7

#KUZEN ASAL DESEN İÇİN
P = [5,7,11]
Ritmik = [[0,4],[1,5],[1,9]]
IstenenBoy = 5*7*11
'''

#GENEL ASAL DESEN İÇİN
P = [5,7,11]
Ritmik = [[0,7],[1,10],[2,17]]
IstenenBoy = 2*5*7*11


#son_dizi, indisler, oncesi_sifir = ritmik_resetleme_final(P, Ritmik, IstenenBoy)
#son_dizi, indisler, oncesi_sifir = ritmik_resetleme_final_and_eklentili(P, Ritmik, IstenenBoy)
son_dizi, indisler, oncesi_sifir = ritmik_resetleme_final_bit_tabanli(P, Ritmik, IstenenBoy)
print(f"{girinti}{'=' * 75}")
print(f"{girinti}(P={P[-1]}) için İKİZ ASAL deseni");
print(f"{girinti}{'-' * 75}")
#print(f"{girinti}Son Oluşan Desen:\n{girinti}{son_dizi}")
print(f"{girinti}{'-' * 75}")
#print(f"{girinti}(P={P[-1]}) için lineer eleme indexleri :\n{girinti}{', '.join(map(str, indisler))}")
# İndislerin sadece ilk 100 tanesini yazdırma
sinirli_indisler = indisler[:100]
print(f"{girinti}(P={P[-1]}) için lineer eleme indexleri (İlk 100 değer) :\n{girinti}{', '.join(map(str, sinirli_indisler))}")
print(f"{girinti}{"indis sayısı:":<20} {len(indisler)}")
p_metni = " X ".join(map(str, P))
print(f"\n{girinti}DESEN BOYU: {p_metni} = {IstenenBoy}")
print(f"{girinti}{'-' * 35}")
print(f"{girinti}Öncekilerle Ortak: {oncesi_sifir - len(indisler)}")
print(f"{girinti}Yeni Bileşik: {len(indisler)}")
print(f"{girinti}Kalan Elenmemiş: {IstenenBoy - oncesi_sifir}")

analiz_sonuclari, final_dizi = lineer_elek_analizi(P, Ritmik, IstenenBoy)

print(f"{girinti}{'-' * 75}")
print(f"{girinti}{'P':<5} | {'Önc. Bileşik':<12} | {'Yeni Bileşik':<12} | {'Toplam':<8} | {'Kalan':<8} | {'Eleme %'}")
print(f"{girinti}{'-' * 75}")
for satir in analiz_sonuclari:
    print(f"{girinti}{satir['P']:<5} | {satir['Oncekilerle']:<12} | {satir['Yeni']:<12} | {satir['Toplam']:<8} | {satir['Kalan']:<8} | %{satir['Yuzde']:.2f}")
print(f"{girinti}{'=' * 75}") 
