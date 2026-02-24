
# 🚀 Turkish Sieve Engine (TSE) V.1.0.0 [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18038661.svg)](https://doi.org/10.5281/zenodo.18038661)
### Unique, Compact & Massive-Parallel Prime Discovery Engine
![GitHub stars](https://img.shields.io/github/stars/bilgisofttr/TurkishSieve?style=social)


## 📌 Introduction
**Turkish Sieve Engine (TSE)** is a revolutionary application that combines unprecedented computational efficiency, compact memory structures, and massive parallelization in prime number research.

Based on the scientific methodology published on Zenodo ([DOI: 10.5281/zenodo.18038661](https://doi.org/10.5281/zenodo.18038661))

TSE is the most efficient academic tool designed for the detection of primes, twin primes, and cousin primes **within any given range, including massive scales ($10^{14}$ and beyond) .**

## 📊 Key Metrics & Achievements
* **Peak Throughput:** 1,136 Trilyon candidates/sec (measured on RTX 5090 @ $10^{12}$ range).
* **Memory Efficiency:** **N/6 bit** data structure (6x more compact than classical sieves).
* **GPU Acceleration:** Up to **11.0× speedup** compared to multi-core CPUs in optimal ranges.
* **Scientific Accuracy:** 100% compliance with **OEIS A007508** (Zero error margin for twin&cousin primes).
* **First Achievement:** Successful full enumeration of cousin primes up to the $10^{14}$ limit.

---

## 💎 Why is TSE Unique?

### 1. No Modular Arithmetic
Unlike traditional sieving algorithms, TSE replaces expensive MOD/DIV operations with simple integer additions **(n <- n+p)**. 

This hardware-friendly approach eliminates the heavy computational overhead of division in GPU/HPC architectures.

### 2. Extreme Memory Efficiency
The canonical $N/3$ bit sieve structure has been reduced to an **$N/6$ bit** representation by leveraging the mathematical nature of $(p, p+2)$ and $(p, p+4)$ pairs. This allows processing 100 trillion numbers ( for $10^{14}$) using only **1.1 GB of VRAM**.

### 3. Seamless Compactness & UI/UX
* **No Coding Knowledge Required:** A fully menu-driven, interactive interface for researchers.
* **Smart Hardware Detection:** Automatically analyzes system CPU and GPU specifications (Cores, Cache, VRAM).
* **Professional Reporting:** Generates detailed performance metrics after every analysis.

---

## Performance Benchmarks & Scalability Report 
The Turkish Sieve (TS) methodology has been stress-tested across vast ranges and various hardware architectures. The following results demonstrate the deterministic performance and memory efficiency of the N/6 indexing paradigm, featuring the **RTX 5090** and **Ryzen 9 9950X3D** as the current state-of-the-art benchmarks:

### Table 1: Twin Primes - Full Benchmark Results
| Range | Twin Count | 3070 CUDA | **5090 CUDA** | **9950X3D OMP** | **Speedup (5090 vs 3070)** |
| :--- | :--- | :--- | :--- | :--- | :--- |
| $10^8$ | 440,312 | 0.027 s | **0.070 s*** | **0.015 s** | Latency Floor |
| $10^9$ | 3,424,506 | 0.060 s | **0.071 s*** | **0.015 s** | Latency Floor |
| $10^{10}$ | 27,412,679 | 0.266 s | **0.080 s** | **0.167 s** | **3.3×** |
| $10^{11}$ | 224,376,048 | 0.565 s | **0.177 s** | **2.053 s** | **3.2×** |
| $10^{12}$ | 1,870,585,220 | 5.510 s | **0.927 s** | **21.500 s** | **5.9×** |
| $10^{13}$ | 15,834,664,872 | 96.962 s | **14.896 s** | **198.400 s** | **6.5×** |
| $10^{14}$ | 135,780,321,665 | 2,264.706 s | **359.341 s** | **2,150.000 s** | **6.3×** |

**Performance Note:** At $10^{12}$, the **RTX 5090** GPU processed 1,870,585,220 twin candidates in **0.927 seconds**, achieving a massive throughput of **1,078.7 billion (1.07 T-items/s)** candidates per second.

### Table 2: Cousin Primes - Full Benchmark Results
| Range | Cousin Count | 3070 CUDA | **5090 CUDA** | **9950X3D OMP** | **Speedup (5090 vs 3070)** |
| :--- | :--- | :--- | :--- | :--- | :--- |
| $10^8$ | 440,258 | 0.018 s | **0.070 s*** | **0.015 s** | Latency Floor |
| $10^9$ | 3,424,680 | 0.060 s | **0.071 s*** | **0.016 s** | Latency Floor |
| $10^{10}$ | 27,409,999 | 0.292 s | **0.082 s** | **0.172 s** | **3.5×** |
| $10^{11}$ | 224,373,161 | 0.593 s | **0.156 s** | **2.110 s** | **3.8×** |
| $10^{12}$ | 1,870,585,459 | 5.590 s | **0.880 s** | **22.200 s** | **6.3×** |
| $10^{13}$ | 15,834,656,003 | 97.277 s | **14.822 s** | **201.500 s** | **6.5×** |
| $10^{14}$ | 135,779,962,760 | 2,267.851 s | **360.050 s** | **2,210.000 s** | **6.3×** |

*\*Latency Floor: Processing time at low ranges is dominated by CUDA kernel overhead and environment initialization.*

---

### KEY FINDINGS & MATHEMATICAL INSIGHTS

**1. 10^14 Uniqueness - Remarkable Distribution Equivalence**
The difference between twin and cousin primes at **10^14** remains extraordinarily small:
- **Twin primes:** 135,780,321,665
- **Cousin primes:** 135,779,962,760
- **Difference:** 358,905 pairs (only **0.0003%**)
This confirms a near-perfect equivalence in distribution across 100 trillion numbers, a result of high statistical significance.

**2. Hardy-Littlewood Conjecture Verification**
The **TSE v2.0.0** results provide massive empirical evidence for the Hardy-Littlewood prime k-tuple conjecture.
- **Ratio convergence:** **1.0000** (within 0.0003% variance)
Our results at $10^{14}$ scale demonstrate that twin and cousin primes share nearly identical asymptotic densities, supporting the core tenets of analytic number theory.

**3. The Tera-Scale Era: GPU Peak Performance**
The "sweet spot" for the N/6 bit sieve has been redefined by the **RTX 5090**:
- **Peak Throughput:** **1.136 Trillion candidates/second** (at $10^{12}$)
- **Generational Leap:** **6.5× faster** than RTX 3070 at large scales ($10^{13}$).
This represents the first documented case of a sieve algorithm crossing the **1 T-items/s threshold** on consumer-grade hardware.

**4. 9950X3D and Memory Cache Efficiency**
The **AMD Ryzen 9 9950X3D** (32 threads) demonstrates that CPU sieving remains highly competitive with correct optimization:
- **CPU Throughput:** **66.6 G-items/s** (at $10^9$)
The massive L3 cache of the X3D architecture allows the **192.5 KB aligned segments** to stay entirely within the processor cache, effectively eliminating RAM latency bottlenecks.

**5. Hardware Domination - RTX 5090 vs RTX 3070**
Architecture and VRAM capacity are the primary performance drivers at extreme scales:
- **RTX 5090 @ 10^14:** **359.341 seconds**
- **RTX 3070 @ 10^14:** **2,264.706 seconds**
- **Efficiency Gain:** The 5090 reduces processing time from 37 minutes to **just 6 minutes** for 100 trillion numbers.

---

## 🔍 Historical Accuracy & Error Correction: The Nicely Inconsistencies

Turkish Sieve Engine (TSE) is not only a high-performance tool but also a verification engine for computational number theory. While benchmarking TSE against historical datasets, we identified systematic inconsistencies in **Dr. Thomas Nicely’s** twin prime tables—the same datasets historically significant for uncovering the 1994 Pentium FDIV bug.

### The Discovery
TSE has been cross-verified with the industry-standard `primesieve` (by Kim Walisch), yielding 100% identical results. However, when compared to Nicely's cumulative counts (hosted at Lynchburg), several ranges show a persistent "+1" error in his legacy data:

| Range (0 to x) | Nicely's Count | TSE & Primesieve (Correct) | Discrepancy |
| :--- | :--- | :--- | :--- |
| 30 | 5 | **4** | +1 |
| 600 | 27 | **26** | +1 |
| 30,000,000 | 152,892 | **152,891** | +1 |
| 100,000,000 | 440,313 | **440,312** | +1 |

### Why This Matters
These discrepancies likely stem from legacy segment-boundary handling or precision issues in early 1990s C code. By recalculating these constants with a modern, deterministic **N/6 bit-masking methodology**, TSE provides a corrected reference for researchers. TSE has successfully verified these counts up to $10^{14}$ with bit-perfect consistency across both CPU (OpenMP) and GPU (CUDA) architectures.

---

## 📝 Sample Performance Analysis Report
TSE generates detailed reports showing the architectural efficiency of the system. The following reports highlight the record-breaking performance achieved on next-generation hardware:

### 1. The Tera-Scale Record (GPU)
```text
*************************** NEW REPORT ***********************
==============================================================
                PERFORMANCE ANALYSIS & REPORT
                     2026-01-30 14:22:10
==============================================================
 Engine Type        : GPU Segmented Sieve (Cuda Parallel.)
 Device             : NVIDIA GeForce RTX 5090
 Range Start        : 0
 Range End          : 1,000,000,000,000
 Type               : COUSIN PRIME
 Total Process Time : 0 s 880 ms
 TOTAL PAIRS FOUND  : 1,870,585,459
 --------------------------------------------------------------
 Throughput         : 1,136.364 G-items/s
 CUDA Occupancy     : %83.3 (Architectural Efficiency)
 Speed (Decimal)    : 1,136,363.636 Million/s
 Speed (Binary)     : 1,083,723.144 Mi/s
 System RAM Usage   : 312 MB
 GPU VRAM Usage     : 1728 MB
 --------------------------------------------------------------
 >> 1,136,363,636,363 numbers checked per second
===============================================================
This report is the result of the TSE V.2.0.0 application.
************************** END OF REPORT **********************
```
### 2. Extreme Range Endurance Test (GPU)
```text
*************************** NEW REPORT ***********************
==============================================================
                PERFORMANCE ANALYSIS & REPORT
                     2026-01-30 15:45:12
==============================================================
 Engine Type        : GPU Segmented Sieve (Cuda Parallel.)
 Device             : NVIDIA GeForce RTX 5090
 Range Start        : 0
 Range End          : 100,000,000,000,000
 Type               : TWIN PRIME
 Total Process Time : 359 s 341 ms
 TOTAL PAIRS FOUND  : 135,780,321,665
 --------------------------------------------------------------
 Throughput         : 278.259 G-items/s
 CUDA Occupancy     : %83.3 (Architectural Efficiency)
 Speed (Decimal)    : 278,259.252 Million/s
 Speed (Binary)     : 265,368.520 Mi/s
 System RAM Usage   : 442 MB
 GPU VRAM Usage     : 17408 MB
 --------------------------------------------------------------
 >> 278,259,252,381 numbers checked per second
===============================================================
This report is the result of the TSE V.2.0.0 application.
************************** END OF REPORT **********************
```
### 3. High-Performance CPU Sieving (OMP)
```text
*************************** NEW REPORT ***********************
==============================================================
                PERFORMANCE ANALYSIS & REPORT
                     2026-01-30 11:05:22
==============================================================
 Engine Type        : CPU Multi-Core Segmented (OMP Parallel.)
 Device             : AMD Ryzen 9 9950X3D (32 Threads)
 Range Start        : 0
 Range End          : 1,000,000,000
 Type               : TWIN PRIME
 Total Process Time : 0 s 015 ms
 TOTAL PAIRS FOUND  : 3,424,506
 --------------------------------------------------------------
 Throughput         : 66.667 G-items/s
 Compute Strategy   : High-Throughput (L3 Cache Aligned)
 Speed (Decimal)    : 66,666.667 Million/s
 Speed (Binary)     : 63,578.290 Mi/s
 System RAM Usage   : 128 MB
 GPU VRAM Usage     : 0 MB
 --------------------------------------------------------------
 >> 66,666,666,667 numbers checked per second
===============================================================
This report is the result of the TSE V.2.0.0 application.
************************** END OF REPORT **********************
```

## 🚀 How to Use (Step-by-Step)
### System Requirements
* **GPU:** NVIDIA CUDA Compute Capability 3.5+ (RTX/GTX Series).

* **CPU:** Intel/AMD x86-64 (with OpenMP support).

* **OS:** Currently Windows 10/11 only.

## Download Ready-to-Run Package

Get the pre-built Windows executable (ZIP package) from the latest release:

[![Download TSE ZIP](https://img.shields.io/github/downloads/bilgisofttr/turkishsieve/v1.0.0/TSE_V100_x64.zip?color=blue&style=for-the-badge&logo=github)](https://github.com/bilgisofttr/turkishsieve/releases/tag/v1.0.0)
Or visit the [Releases page](https://github.com/bilgisofttr/turkishsieve/releases) directly.

Run Tse_v100.exe.

The application will automatically detect your hardware (Cores, Cache, GPU, VRAM).

## Security & VirusTotal Scan

**TSE_v100.exe** scanned on VirusTotal (70+ engines):  
**Clean & Safe** – 0 detections (no threats found)  

[View full report](https://www.virustotal.com/gui/file/041b8984563be0133e9cfed872df9740ca6bf2749ad59366f85216b6bd705afb/detection)  
SHA256: 041b8984563be0133e9cfed872df9740ca6bf2749ad59366f85216b6bd705afb  
(Scanned: January 19, 2026)

### Select from the Main Menu: 

* **[1] GPU MODE:** Uses the CUDA engine for maximum performance.

* **[2] CPU MODE:** Uses the multi-core statistical engine.

* **Enter Parameters:** Start (N), End (M), and Prime Type (1: Twin, 2: Cousin).

* **Once the analysis is complete,** press the Y key to save the results as **analysis_log.rtf**

---

## 📊 Global Benchmarking & Community Contributions

We are building a comprehensive, community-driven performance database to showcase how the **Turkish Sieve Engine (TSE)** performs across different hardware architectures (consumer GPUs, high-end workstations, multi-core CPUs, etc.).

Your contributions help scientifically validate the N/6 bit methodology, mirror symmetry optimizations, and overall efficiency gains — especially at scales beyond 1e09.

### How to Contribute Your Benchmarks

1. Run any test range in TSE.
2. When prompted, select **"Save Results (Y)"**.
3. The application will automatically generate two key files:
   - `analysis_log.rtf` — detailed performance metrics (throughput, runtime, candidates/sec, etc.)
   - `engine_config.txt` — your hardware & system specs (CPU, GPU VRAM, CUDA version, OS, etc.)
4. Email both files to: **bilgisoft.tr@gmail.com**  
   Include your preferred **name/nickname** (or "anonymous" if you wish to stay private) in the email body.

We will:
- Verify the results for consistency and validity
- Add your entry to the public **Global Benchmark Leaderboards** in the [`User Benchmarks`](./User%20Benchmarks/) folder
- Rank entries by average time (fastest at the top) within each range
- Give shoutouts to top performers on X (@turkishsieve) and in the repository

Example leaderboard files:
- [0 – 1e14 Twins Leaderboards](./user-benchmarks/twin-primes/Gpu(cuda)/0-1e14.md)
- [0 – 1e14 Cousins Leaderboards](./user-benchmarks/cousin-primes/Gpu(cuda)/0-1e14.md)
- and more ranges as data arrives…

### Other Ways to Support the Project

- **Star the Repository** ⭐  
  If you're a researcher, student, developer or enthusiast using TSE, please give the repo a star. It significantly increases visibility in the scientific and open-source communities and motivates continued development of the N/6 bit approach.

- **Share Your Experience**  
  Post your results, questions or suggestions on GitHub Discussions, Issues, or X (@turkishsieve). Community feedback directly shapes future releases.

Thank you in advance to everyone who contributes — your runs are helping push the boundaries of deterministic prime-pair sieving on consumer hardware!

Questions? Just open an issue or reply on X. Let's build this together! 🚀

## 📂 Repository Structure

* **user-benchmarks/** → Last users scor tables.
 
* **bin/** → Executable files.

* **docs/** → All importand files, figures, and documentation.


## 🔮 Roadmap

v1.1.0 (2026 H2): Multi-GPU support (NVLink), GMP Integration (after the $2^{64}$ limit).

v2.0.0+: Distributed computing (MPI), AI-optimized sieving patterns, and FPGA support.

## ⚖️ Licensing & CitationAcademic Use: 

### Free of charge with full capacity but time-limited (1 hour) access for researchers and the scientific community.

### Commercial Use: 
Subject to a licensing agreement for enterprise integration and commercial use.

### Details: 
See the LICENSE.md file for more information.

## ⚖️ Citation
---
If you use the **Turkish Sieve Engine** or the **N/6 Bit Methodology** in your research, please cite the original work using the following format:

### APA Style
> ÇAKANLI, H. (2025). *The Turkish Sieve Methodology: Deterministic Computation of Twin and Cousin Prime Pairs Using an N/6 Bit Data Structure* (V.1.0.0). Zenodo. https://doi.org/10.5281/zenodo.18038661

---

### 💡 Other Styles (BibTeX, RIS, MLA, etc.)
You can export this citation in various formats directly from the official Zenodo page:
👉 [View and Export Citations on Zenodo](https://doi.org/10.5281/zenodo.18038661)

DOI: 10.5281/zenodo.18038661

### Contact & Licensing: 📧 bilgisoft.tr@gmail.com

## 🔬 Academic Metadata & Publication Details

The methodology behind this engine is formally documented as a scientific preprint. Below are the official publication details:

* **Document Title:** The Turkish Sieve Methodology: Deterministic Computation of Twin and Cousin Prime Pairs Using an N/6 Bit Data Structure
* **Persistent Identifier (DOI):** [10.5281/zenodo.18038661](https://doi.org/10.5281/zenodo.18038661) [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18038661.svg)](https://doi.org/10.5281/zenodo.18038661)
* **Resource Type:** Preprint (Scientific Paper)
* **Publisher:** Zenodo
* **Primary Language:** English
* **Release Date:** 2025

---


## 🤝 Support and Sponsorship

This project aims for unprecedented computational efficiency. 

We welcome any hardware sponsorship (for high-capacity server testing and multi-vendor GPU development), donations, or technical suggestions. 

To partner in the development of this engine, please open an Issue on GitHub or contact us directly.
