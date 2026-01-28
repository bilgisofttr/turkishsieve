import re, os, glob, subprocess
from datetime import datetime

# AYARLAR
BASE_DIR = "."

# --- EKSİKSİZ ŞABLONLAR ---

GPU_TEMPLATE = """# User Benchmarks (0 - {RANGE})

**Last updated:** {DATE} 

This file presents the scoreboard of users who ran the application on their own machines and shared their results.  
**Thanks to all contributors!** 🙏

Rankings are sorted by **average time (seconds)** (lowest time at the top).

**Current World Leader (Fastest Verified):** {LEADER_INFO}

| Rank | User Name (Nick)      | Email                          | Date-Time         | GPU Hardware               | Occup. | {COUNT_LABEL} | Runs | Avg. Time(s) |
|------|-----------------------|--------------------------------|-------------------|----------------------------|--------|-----------------|------|--------------|
{TABLE_ROWS}

**Notes:**
- Count: Number of twin/cousin prime pairs found in the range (should be consistent across all valid runs for verification).
- Test Count: How many times the user repeated the same range (higher count = more reliable average).
- Average Time: Total runtime of all runs divided by Test Count.
- Ties in average time are broken by earliest submission timestamp.

 
**To submit your results:** Please share your log files ( **analysis_log.rtf & analysis_log.txt** ) via [email](mailto:bilgisoft.tr@gmail.com) or open a GitHub Issue.
"""

CPU_TEMPLATE = """# User Benchmarks (0 - {RANGE})

**Last updated:** {DATE} 

This file presents the scoreboard of users who ran the application on their own machines and shared their results.  
**Thanks to all contributors!** 🙏

Rankings are sorted by **average time (seconds)** (lowest time at the top).

**Current World Leader (Fastest Verified):** {LEADER_INFO}

| Rank | User Name (Nick)      | Email                          | Date-Time               | CPU Hardware                          | Count (Pairs) | Runs | Avg. Time(s) |
|------|-----------------------|--------------------------------|-------------------------|---------------------------------------|---------------|------|--------------|
{TABLE_ROWS}

**Notes:**
- Count: Number of twin/cousin prime pairs found in the range (should be consistent across all valid runs for verification).
- Test Count: How many times the user repeated the same range (higher count = more reliable average).
- Average Time: Total runtime of all runs divided by Test Count.
- Ties in average time are broken by earliest submission timestamp.

 
**To submit your results:** Please share your log files ( **analysis_log.rtf & analysis_log.txt** ) via [email](mailto:bilgisoft.tr@gmail.com) or open a GitHub Issue.
"""

def run_git_command(command, path, action_name):
    try:
        subprocess.run(command, cwd=path, check=True, capture_output=True, text=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"[X] {action_name} hatası: {e.stderr}")
        return False

# --- GÜVENLİK AYARLARI ---
# Token ve kullanıcı bilgilerini buraya bir kez yazıyorsun
GITHUB_TOKEN = ""
GITHUB_USER = "bilgisofttr"
GITHUB_REPO = "turkishsieve"

# Otomatik URL Oluşturma
REMOTE_URL = f"https://{GITHUB_TOKEN}@github.com/{GITHUB_USER}/{GITHUB_REPO}.git"

def sync_and_update():
    repo_path = os.path.abspath(BASE_DIR)
    
    # 1. BAĞLANTIYI GÜNCELLE VE VERİ ÇEK
    print("\n[1] Depo bağlantısı kontrol ediliyor...")
    if os.path.exists(os.path.join(repo_path, ".git")):
        # URL'yi her seferinde tokenlı haliyle güncelle (Hatalı URL'leri temizler)
        run_git_command(["git", "remote", "set-url", "origin", REMOTE_URL], repo_path, "URL Güncelleme")
        print("[V] Bağlantı doğrulandı, veriler çekiliyor...")
        run_git_command(["git", "pull", "origin", "main"], repo_path, "Git Pull")
    else:
        print("[!] Hata: Klasörde .git yok. Lütfen önce 'git init' yapın.")
        return
    # 2. GÜNCELLEME ONAYI
    onay = input("\n[2] RTF dosyaları işlensin mi? (e/h): ").lower()
    if onay != 'e': return

    rtf_files = glob.glob("*.rtf")
    folder_map = {"PRIMES": "primes", "TWIN": "twin-primes", "COUSIN": "cousin-primes"}
    update_count = 0

    for file_path in rtf_files:
        full_filename = os.path.splitext(os.path.basename(file_path))[0]
        email_match = re.search(r"\((.*?)\)", full_filename)
        user_email = email_match.group(1).strip() if email_match else "bilgisoft.tr@gmail.com"
        user_name = re.sub(r"\(.*?\)", "", full_filename).strip()

        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        # RTF Temizliği
        clean_content = re.sub(r'\\[a-z0-9]+', '', content).replace('{', '').replace('}', '').replace('\r', '')
        blocks = clean_content.split("NEW REPORT")

        for block in blocks:
            if "ANALYSIS & REPORT" not in block: continue
            try:
                # Veri Ayıklama
                t_match = re.search(r"Type\s*:\s*(PRIMES|TWIN|COUSIN)", block, re.IGNORECASE)
                if not t_match: continue
                algo = t_match.group(1).upper()
                is_gpu = "GPU" in re.search(r"Engine Type\s*:\s*(\w+)", block).group(1).upper()
                r_end = re.search(r"Range End\s*:\s*([\d,]+)", block).group(1)
                device = re.search(r"Device\s*:\s*(.*)", block).group(1).strip()
                t_m = re.search(r"Total Time\s*:\s*(\d+)\s*s\s*(\d+)\s*ms", block)
                count = re.search(r"COUNT\s*:\s*([\d,]+)", block).group(1)
                dt = re.search(r"(\d{4}-\d{2}-\d{2})", block).group(1)
                hr = re.search(r"(\d{2}:\d{2}:\d{2})", block).group(1)
                occ = re.search(r"Occupancy\s*:\s*([\d%]+)", block).group(1) if is_gpu else ""

                # Klasör ve Menzil Ayarı
                target_dir = f"{BASE_DIR}/{folder_map[algo]}/{'Gpu(cuda)' if is_gpu else 'Cpu(Omp)'}"
                clean_r = r_end.replace(",", "").strip()
                label = f"1e{len(clean_r)-1}" if clean_r.startswith("1") else clean_r
                md_path = f"{target_dir}/0-{label}.md"
                
                if not os.path.exists(target_dir):
                    os.makedirs(target_dir, exist_ok=True)

                # Tablo Verilerini Yönet
                table_data = []
                if os.path.exists(md_path):
                    with open(md_path, 'r', encoding='utf-8') as f:
                        for line in f:
                            if line.startswith("|") and "Rank" not in line and "---" not in line:
                                cols = [c.strip() for c in line.split("|")][1:-1]
                                if cols[1] != user_name: table_data.append(cols)
                
                sec = int(t_m.group(1)) + (int(t_m.group(2))/1000)
                if is_gpu:
                    table_data.append(["?", user_name, user_email, f"{dt} {hr[:5]}", device, occ, count, "5", f"{sec:.3f}"])
                else:
                    table_data.append(["?", user_name, user_email, f"{dt} {hr[:5]}", device, count, "5", f"{sec:.3f}"])
                
                table_data.sort(key=lambda x: float(x[-1]))
                
                # Şablonu Yazdır
                speed = int(clean_r) / float(table_data[0][-1])
                rows_str = ""
                for idx, r in enumerate(table_data, 1):
                    row_content = [str(idx)] + r[1:]
                    rows_str += "| " + " | ".join(row_content) + " |\n"
                
                count_lbl = "Prime Count" if algo == "PRIMES" else ("Twin Count" if algo == "TWIN" else "Cousin Count")
                
                final_content = (GPU_TEMPLATE if is_gpu else CPU_TEMPLATE).format(
                    RANGE=label, DATE=datetime.now().strftime('%Y-%m-%d'),
                    LEADER_INFO=f"{speed:,.0f} numbers checked per second – **@{table_data[0][1]}** ({table_data[0][4]})",
                    TABLE_ROWS=rows_str.strip(), COUNT_LABEL=count_lbl
                )
                
                with open(md_path, 'w', encoding='utf-8') as f:
                    f.write(final_content)
                
                update_count += 1
                print(f" [V] Güncellendi: {md_path}")
            except Exception as e:
                print(f" [!] Hata (Blok): {e}")
                continue

    # 3. GITHUB'A GÖNDERME
    if update_count > 0:
        if input("\n[3] GitHub'a gönderilsin mi? (e/h): ").lower() == 'e':
            print("\n--- GITHUB GÜNCELLEMESİ BAŞLIYOR ---")
            run_git_command(["git", "add", "."], repo_path, "Git Add")
            commit_msg = f"Benchmark Auto-update: {datetime.now().strftime('%Y-%m-%d %H:%M')}"
            run_git_command(["git", "commit", "-m", commit_msg], repo_path, "Git Commit")
            # Mevcut satırı şununla değiştir:
            if run_git_command(["git", "push", "-u", "origin", "main"], repo_path, "Git Push"):
                print("[V] REKORLAR GITHUB'A UÇTU!")
    else:
        print("\n[!] İşlenecek yeni veri bulunamadı.")

if __name__ == "__main__":
    sync_and_update()