# Türk Eleği – A Novel Prime Sieving Algorithm

## Introduction
Türk Eleği (The Turkish Sieve) is a newly developed algorithm for prime number detection 
that does **not rely on modular arithmetic**.  
It is lightweight, memory-efficient, and highly parallelizable.

Key Features:
- No modular arithmetic, only simple addition and multiplication.
- Extremely low memory footprint (N/24 bits, ~39 MB per 1 billion numbers).
- Parallelizable on CPU (OpenMP) and GPU (CUDA/OpenCL).
- Scales with hardware – usable on GPUs, clusters, and potentially quantum computers.
- Educationally friendly with simple visualization and animations.

## Repository Structure
- `src/` → Source code implementations
- `examples/` → Simple usage demos and performance tests
- `docs/` → Academic paper (LaTeX), figures, documentation

## License
This project is licensed under a **dual-license model**:
- **Free** for academic, research, and non-commercial use.
- **Commercial use requires a paid license.**

See [LICENSE.md](./LICENSE.md) for details.

For licensing inquiries:
📧 Email: your-email-here

## Citation
If you use this algorithm in academic research, please cite:

