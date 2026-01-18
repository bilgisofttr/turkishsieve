[![Download TSE](https://img.shields.io/badge/Download-TSE_v1.0.0-blue?style=for-the-badge&logo=github)](https://github.com/bilgisofttr/turkishsieve/releases/latest)


# 🚀 Turkish Sieve Engine (TSE) V.1.0.0 [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18038661.svg)](https://doi.org/10.5281/zenodo.18038661)
### Unique, Compact & Massive-Parallel Prime Discovery Engine
![GitHub stars](https://img.shields.io/github/stars/bilgisofttr/TurkishSieve?style=social)


## 📌 Introduction
**Turkish Sieve Engine (TSE)** is a revolutionary application that combines unprecedented computational efficiency, compact memory structures, and massive parallelization in prime number research. Based on the scientific methodology published on Zenodo ([DOI: 10.5281/zenodo.18038661](https://doi.org/10.5281/zenodo.18038661)), TSE is the most efficient academic tool designed for the detection of primes, twin primes, and cousin primes **within any given range, including massive scales ($10^{14}$ and beyond).**

## 📊 Key Metrics & Achievements
* **Peak Throughput:** 339.4 Billion candidates/sec (measured on RTX 3070 @ $10^{12}$ range).
* **Memory Efficiency:** **N/6 bit** data structure (6x more compact than classical sieves).
* **GPU Acceleration:** Up to **11.0× speedup** compared to multi-core CPUs in optimal ranges.
* **Scientific Accuracy:** 100% compliance with **OEIS A007508** (Zero error margin for twin primes).
* **First Achievement:** Successful full enumeration of cousin primes up to the $10^{14}$ limit.

---

## 💎 Why is TSE Unique?

### 1. No Modular Arithmetic
Unlike traditional sieving algorithms, TSE replaces expensive MOD/DIV operations with simple integer additions ($n \leftarrow n+p$). This hardware-friendly approach eliminates the heavy computational overhead of division in GPU/HPC architectures.

### 2. Extreme Memory Efficiency
The canonical $N/3$ bit sieve structure has been reduced to an **$N/6$ bit** representation by leveraging the mathematical nature of $(p, p+2)$ and $(p, p+4)$ pairs. This allows processing 100 trillion numbers ($10^{14}$) using only **1.1 GB of VRAM**.

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

### Usage Steps

Run Tse_v100.exe.

The application will automatically detect your hardware (Cores, Cache, GPU, VRAM).

### Select from the Main Menu: 

* **[1] GPU MODE:** Uses the CUDA engine for maximum performance.

* **[2] CPU MODE:** Uses the multi-core statistical engine.

* **Enter Parameters:** Start (N), End (M), and Prime Type (1: Twin, 2: Cousin).

* **Once the analysis is complete,** press the Y key to save the results as **TSE_Report_[Date].txt.**

---

## 📊 Global Benchmarking & Contribution
We aim to build a comprehensive performance database across different hardware architectures. You can contribute to the development and scientific validation of the **Turkish Sieve Engine**:

1. **Submit Your Benchmarks:** If you run a test and select the **"Save Results (Y)"** option, the application will automatically generate an `analysis_log.rtf` (performance metrics) and an `engine_config.txt` (hardware/system specs). 
   * Please email these two files to **bilgisoft.tr@gmail.com** along with your name or nickname. 
   * We will publish verified results in our official **Global Benchmark Table** to showcase how TSE performs on various GPUs and CPUs worldwide.

2. **Star the Project:** If you are a researcher, academic, or enthusiast using this engine, please consider **giving this repository a Star (⭐)**. Your support helps increase the project's visibility in the scientific community and encourages further development of the N/6 bit methodology.

## 📂 Repository Structure
* **src/** → Source code implementations (CUDA & OpenMP).

* **bin/** → Executable files (tse.exe).

* **docs/** → Academic paper (Zenodo PDF), figures, and documentation.

* **logs/** → Execution and performance logs.

## 🔮 Roadmapv1.1.0 (2026 H2): 

Multi-GPU support (NVLink), GMP Integration (breaking the $2^{64}$ limit).

v2.0.0+: Distributed computing (MPI), AI-optimized sieving patterns, and FPGA support.

## ⚖️ Licensing & CitationAcademic Use: 

### Free of charge with full capacity but time-limited access for researchers and the scientific community.

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
