# 🚀 Turkish Sieve Engine (TSE) V.1.0.0
### Unique, Compact & Massive-Parallel Prime Discovery Engine

## 📌 Introduction
Turkish Sieve Engine (TSE) is a revolutionary application that combines unprecedented computational efficiency, compact memory structures, and massive parallelization in prime number research. 
Based on the scientific methodology published on Zenodo (DOI:10.5281/zenodo.18038661), TSE is the most efficient academic tool designed for the detection of **primes, twin primes, and cousin primes** within any given range, including massive scales ($10^{14}$ and beyond).

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
==============================================================
                PERFORMANCE ANALYSIS & REPORT
==============================================================
Range              : [0 - 1,000,000,000,000]
Engine Type        : GPU Segmented Sieve (Cuda Parallel.)
Device             : NVIDIA GeForce RTX 3070
Total Process Time : 5s 510ms
Throughput         : 181.488 G-items/s
CUDA Occupancy     : %100.0 (Architectural Efficiency)
TOTAL PAIRS FOUND  : 1,870,585,220
==============================================================
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

## Citation: 
### If you use this software in your research, please cite:
H. Cakanli, "The Turkish Sieve Methodology: Deterministic Computation of Twin and Cousin Primes", Zenodo, 2026. 

DOI: 10.5281/zenodo.18038661

### Contact & Licensing: 📧 bilgisoft.tr@gmail.com

## 🤝 Support and Sponsorship

This project aims for unprecedented computational efficiency. 

We welcome any hardware sponsorship (for high-capacity server testing and multi-vendor GPU development), donations, or technical suggestions. 

To partner in the development of this engine, please open an Issue on GitHub or contact us directly.
