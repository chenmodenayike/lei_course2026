"""
参考：9. 论文绘图/src/散点图.py
主题：各时段吞吐量与时延的散点分布（两种策略）
"""
import os
import numpy as np
import matplotlib.pyplot as plt
from simulation_data import (
    TRADITIONAL_THROUGHPUT, OPTIMIZED_THROUGHPUT,
    TRADITIONAL_DELAY, OPTIMIZED_DELAY,
    setup_matplotlib_chinese, OUTPUT_DIR,
)

setup_matplotlib_chinese()

plt.figure(figsize=(7, 5))
plt.scatter(TRADITIONAL_THROUGHPUT, TRADITIONAL_DELAY, c="#0073C2", marker="o", s=50,
            alpha=0.8, label="传统RSSI优先策略")
plt.scatter(OPTIMIZED_THROUGHPUT, OPTIMIZED_DELAY, c="#CD534C", marker="s", s=50,
            alpha=0.8, label="负载感知优化策略")
plt.grid(True)
plt.xlabel("平均吞吐量 (Mbps)")
plt.ylabel("平均时延 (ms)")
plt.title("吞吐量与时延关系散点图")
plt.legend()
plt.tight_layout()

out = os.path.join(OUTPUT_DIR, "fig05_吞吐量时延散点图.png")
plt.savefig(out, dpi=300, bbox_inches="tight")
print(f"已保存: {out}")
