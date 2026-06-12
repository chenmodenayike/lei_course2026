"""
参考：9. 论文绘图/src/直方图.py
主题：高峰时段(19:00)资源优化前后各接入点负载分布
对应论文图2.2
"""
import os
import numpy as np
import matplotlib.pyplot as plt
from simulation_data import generate_ap_loads, setup_matplotlib_chinese, OUTPUT_DIR

setup_matplotlib_chinese()

peak_idx = 11  # 19:00
loads_before = generate_ap_loads(0.832, target_mean=0.68, seed=201)
loads_after = generate_ap_loads(0.562, target_mean=0.58, seed=202)

plt.figure(figsize=(7, 5))
plt.hist([loads_before, loads_after], label=["优化前", "优化后"], bins=8,
         color=["#868686", "#0073C2"], edgecolor="white", alpha=0.85)
plt.grid(True, axis="y")
plt.xlabel("接入点综合负载评分")
plt.ylabel("接入点数量")
plt.title("高峰时段(19:00)资源优化前后负载分布")
plt.legend()
plt.tight_layout()

out = os.path.join(OUTPUT_DIR, "fig06_负载分布直方图.png")
plt.savefig(out, dpi=300, bbox_inches="tight")
print(f"已保存: {out}")
