import math

def ozel_ritmik_elek(N, sabit_uc_boyutlu_dizi):
    """
    N: Toplam sayı sınırı
    sabit_uc_boyutlu_dizi: [[p1, start1, adim1], [p2, start2, adim2], ...] yapısında liste
    """
    # L = N/6 bitlik dizi, tüm elemanları 1 (başlangıçta hepsi aday)
    L = N // 6
    bit_dizisi = [1] * L
    
    # Eleme sınırı: kök(N)
    sinir = int(math.sqrt(N))
    print(f"Başlangıçta : {bit_dizisi} \nSınır L: {sinir}")
    # 3 boyutlu yapı üzerinden döngü: her p için tek start ve tek adim
    for veri in sabit_uc_boyutlu_dizi:
        p = veri[0]
        start = veri[1]
        adim = veri[2]
        #print(f"\nİşlenen p: {p}, start: {start}, adim: {adim}")
        # Eğer p, kök(L) değerinden büyük ise döngüyü sonlandır
        if p > sinir:
            break
        
        # Belirlenen start'tan başla, adim kadar ilerleyerek ele (0 yap)
        # Dizinin dışına çıkana kadar ritmik devam et
        idx = start
        while idx < L:
            if idx < p and p!=5: 
                idx += adim
                continue
            bit_dizisi[idx] = 0
            idx += adim
          
    # Kalan 1'leri say ve sonucu göster
    bit_dizisi[0] = 1 # (5,7) çifti için ilk elemanı 1 yap
    
    kalan_birler = sum(bit_dizisi)
    print(f"Oluşan : {bit_dizisi}") 

    print(f"İşlem Tamamlandı.")
    print(f"L Boyutu: {L}")
    print(f"İkiz Sayısı (3,5) dahil: {kalan_birler+1}")
    
    return kalan_birler

# Örnek Kullanım İçin Veri Yapısı:
# [[p, start, adim], ...]
ornek_sabitler = [
    # p=5 için
    [5, 0, 5],  [5, 3, 5],
    
    # p=7 için
    [7, 7, 35], [7, 12, 35], [7, 14, 35], [7, 19, 35], [7, 21, 35], [7, 26, 35],
    
    # p=11 için
    [11, 1, 385],[11, 34, 385],[11, 41, 385],[11, 52, 385],[11, 67, 385],[11, 74, 385], [11, 107, 385], [11, 111, 385], [11, 122, 385], [11, 129, 385], [11, 144, 385], [11, 151, 385], [11, 162, 385], [11, 177, 385], [11, 184, 385],
    [11, 199, 385], [11, 206, 385],[11, 221, 385],[11, 232, 385],[11, 239, 385],[11, 254, 385],[11, 261, 385],[11, 272, 385],[11, 276, 385],[11, 309, 385],[11, 316, 385],[11, 331, 385],[11, 342, 385],[11, 349, 385],[11, 382, 385],

    # p=13 için
    [13,27,5005],[13, 36, 5005],
    [13, 62, 5005],[13, 66, 5005],
    [13, 79, 5005],[13, 92, 5005],
    [13, 101, 5005],[13, 114, 5005],
    [13, 127, 5005],[13, 157, 5005],
    [13, 179, 5005],[13, 209, 5005],
    [13, 244, 5005],[13, 274, 5005],
    [13, 296, 5005],[13,326, 5005]
]

# Test:
ozel_ritmik_elek(388, ornek_sabitler)