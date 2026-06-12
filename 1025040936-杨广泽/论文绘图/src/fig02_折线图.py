"""
参考：9. 论文绘图/src/折线图.py
主题：全天平均吞吐量随时间变化（传统策略 vs 负载感知策略）
对应论文图4.1
"""
import os
import numpy as np
import matplotlib.pyplot as plt
from simulation_data import (
    TIME_LABELS, TRADITIONAL_THROUGHPUT, OPTIMIZED_THROUGHPUT,
    setup_matplotlib_chinese, OUTPUT_DIR,
)

setup_matplotlib_chinese()

x = np.arange(len(TIME_LABELS))

plt.figure(figsize=(7, 4))
plt.plot(x, TRADITIONAL_THROUGHPUT, "b", lw=1.5, label="传统RSSI优先策略")
plt.plot(x, TRADITIONAL_THROUGHPUT, "bo", ms=4)
plt.plot(x, OPTIMIZED_THROUGHPUT, "r", lw=1.5, label="负载感知优化策略")
plt.plot(x, OPTIMIZED_THROUGHPUT, "rs", ms=4)
plt.xticks(x, TIME_LABELS, rotation=45)
plt.grid(True)
plt.axis("tight")
plt.xlabel("时段")
plt.ylabel("平均吞吐量 (Mbps)")
plt.title("智慧校园无线网络全天平均吞吐量对比")
plt.legend()
plt.tight_layout()

out = os.path.join(OUTPUT_DIR, "fig02_吞吐量折线图.png")
plt.savefig(out, dpi=300, bbox_inches="tight")
print(f"已保存: {out}")
