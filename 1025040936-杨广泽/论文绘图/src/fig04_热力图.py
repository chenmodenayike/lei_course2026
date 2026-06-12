"""
参考：9. 论文绘图/src/热力图.py
主题：12个接入点 × 15个时段的负载热力图（优化策略）
"""
import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from simulation_data import (
    TIME_LABELS, AP_NAMES, OPTIMIZED_LOAD_STD, generate_ap_loads,
    setup_matplotlib_chinese, OUTPUT_DIR,
)

setup_matplotlib_chinese()

load_matrix = np.array([
    generate_ap_loads(std, seed=100 + i) for i, std in enumerate(OPTIMIZED_LOAD_STD)
]).T

fig, ax = plt.subplots(figsize=(10, 5), dpi=200)
im = ax.imshow(load_matrix, aspect="auto", cmap=cm.YlOrRd, vmin=0.2, vmax=0.9)
ax.set_xticks(np.arange(len(TIME_LABELS)))
ax.set_xticklabels(TIME_LABELS, rotation=45)
ax.set_yticks(np.arange(len(AP_NAMES)))
ax.set_yticklabels(AP_NAMES, fontsize=8)
ax.set_xlabel("时段")
ax.set_ylabel("接入点")
ax.set_title("负载感知策略下各接入点负载热力图")
plt.colorbar(im, ax=ax, label="综合负载评分")

out = os.path.join(OUTPUT_DIR, "fig04_接入点负载热力图.png")
fig.savefig(out, dpi=300, bbox_inches="tight")
print(f"已保存: {out}")
