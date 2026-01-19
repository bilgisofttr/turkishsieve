
# 🚀 Turkish Sieve Engine (TSE) V.1.0.0 [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18038661.svg)](https://doi.org/10.5281/zenodo.18038661)
### Unique, Compact & Massive-Parallel Prime Discovery Engine
![GitHub stars](https://img.shields.io/github/stars/bilgisofttr/TurkishSieve?style=social)


## 📌 Introduction
**Turkish Sieve Engine (TSE)** is a revolutionary application that combines unprecedented computational efficiency, compact memory structures, and massive parallelization in prime number research.

Based on the scientific methodology published on Zenodo ([DOI: 10.5281/zenodo.18038661](https://doi.org/10.5281/zenodo.18038661))

TSE is the most efficient academic tool designed for the detection of primes, twin primes, and cousin primes **within any given range, including massive scales ($10^{14}$ and beyond) .**

## 📊 Key Metrics & Achievements
* **Peak Throughput:** 181.5 Billion candidates/sec (measured on RTX 3070 @ $10^{12}$ range).
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

## 📝 Sample Performance Analysis Report
TSE generates detailed reports showing the architectural efficiency of the system:

```text
*************************** NEW REPORT ***********************
==============================================================
                PERFORMANCE ANALYSIS & REPORT
                     2026-01-17 15:11:49
==============================================================
 Engine Type        : GPU Segmented Sieve (Cuda Parallel.)
 Device             : NVIDIA GeForce RTX 3070
 Range Start        : 1
 Range End          : 1,000,000,000,000
 Type               : TWIN PRIME
 Total Process Time : 5 s 510 ms
 TOTAL PAIRS FOUND  : 1,870,585,220
 --------------------------------------------------------------
 Throughput         : 181.488 G-items/s
 CUDA Occupancy     : %83.3 (Architectural Efficiency)
 Speed (Decimal)    : 181488.203 Million/s
 Speed (Binary)     : 173080.638 Mi/s
 System RAM Usage   : 281 MB
 GPU VRAM Usage     : 1127 MB
 --------------------------------------------------------------
 >> 181,488,203,266 numbers checked per second
===============================================================
This report is the result of the TSE V.1.0.0 application.
************************** END OF REPORT **********************

*************************** NEW REPORT ***********************
==============================================================
                PERFORMANCE ANALYSIS & REPORT
                     2026-01-17 15:54:30
==============================================================
 Engine Type        : GPU Segmented Sieve (Cuda Parallel.)
 Device             : NVIDIA GeForce RTX 3070
 Range Start        : 1
 Range End          : 100,000,000,000,000
 Type               : TWIN PRIME
 Total Process Time : 2264 s 706 ms
 TOTAL PAIRS FOUND  : 135,780,321,665
 --------------------------------------------------------------
 Throughput         : 44.156 G-items/s
 CUDA Occupancy     : %83.3 (Architectural Efficiency)
 Speed (Decimal)    : 44155.842 Million/s
 Speed (Binary)     : 42110.292 Mi/s
 System RAM Usage   : 314 MB
 GPU VRAM Usage     : 1145 MB
 --------------------------------------------------------------
 >> 44,155,841,862 numbers checked per second
===============================================================
This report is the result of the TSE V.1.0.0 application.
************************** END OF REPORT **********************

*************************** NEW REPORT ***********************
==============================================================
                PERFORMANCE ANALYSIS & REPORT
                     2026-01-17 19:49:20
==============================================================
 Engine Type        : GPU Segmented Sieve (Cuda Parallel.)
 Device             : NVIDIA GeForce GTX 1650 Ti
 Range Start        : 1,000,000,000,000,000
 Range End          : 1,001,000,000,000,000
 Type               : TWIN PRIME
 Total Process Time : 348 s 447 ms
 TOTAL PAIRS FOUND  : 1,106,775,692
 --------------------------------------------------------------
 Throughput         : 2.870 G-items/s
 CUDA Occupancy     : %100.0 (Architectural Efficiency)
 Speed (Decimal)    : 2869.877 Million/s
 Speed (Binary)     : 2736.928 Mi/s
 System RAM Usage   : 279 MB
 GPU VRAM Usage     : 886 MB
 --------------------------------------------------------------
 >> 2,869,876,910 numbers checked per second
===============================================================
This report is the result of the TSE V.1.0.0 application.
************************** END OF REPORT **********************

*************************** NEW REPORT ***********************
==============================================================
                PERFORMANCE ANALYSIS & REPORT
                     2026-01-17 05:05:49
==============================================================
 Engine Type        : CPU Multi-Core Segmented (OMP Parallel.)
 Device             : Intel(R) Core(TM) i7-10750H CPU @ 2.60GHz
 Range Start        : 0
 Range End          : 100,000,000,000
 Type               : COUSIN PRIME
 Total Process Time : 12 s 177 ms
 TOTAL PAIRS FOUND  : 224,373,161
 --------------------------------------------------------------
 Throughput         : 8.212 G-items/s
 Compute Strategy   : High-Throughput Mode
 Speed (Decimal)    : 8212.203 Million/s
 Speed (Binary)     : 7831.767 Mi/s
 System RAM Usage   : 150 MB
 GPU VRAM Usage     : 0 MB
 --------------------------------------------------------------
 >> 8,212,203,334 numbers checked per second
===============================================================
This report is the result of the TSE V.1.0.0 application.
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
