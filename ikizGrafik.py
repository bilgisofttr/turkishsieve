import matplotlib.pyplot as plt
import numpy as np

# Data
N = np.array([1e9, 1e10, 1e11, 5e11, 8e11, 1e12])
cpu = np.array([0.141, 1.285, 14.074, 88.4, 146.2, 191.9])
gpu = np.array([0.033, 0.273, 2.569, 15.866, 29.891, 37.862])

# Create log-log plot
plt.figure(figsize=(9,6))
plt.loglog(N, cpu, marker='o', label='CPU', linewidth=2)
plt.loglog(N, gpu, marker='o', label='GPU', linewidth=2)

plt.xlabel("N (üst sınır, log)")
plt.ylabel("Süre (saniye, log)")
plt.title("CPU vs GPU – Log-Log Ölçekli Süre Karşılaştırması")
plt.grid(True, which="both", linestyle="--", alpha=0.6)
plt.legend()

plt.show()
