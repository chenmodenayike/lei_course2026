"""
参考：9. 论文绘图/src/折线图2.py
主题：左轴为用户数量，右轴为平均时延（两种策略对比）
对应论文图4.2相关分析
"""
import os
import numpy as np
import matplotlib.pyplot as plt
from simulation_data import (
    TIME_LABELS, USER_COUNT, TRADITIONAL_DELAY, OPTIMIZED_DELAY,
    setup_matplotlib_chinese, OUTPUT_DIR,
)

setup_matplotlib_chinese()

x = np.arange(len(TIME_LABELS))

fig, ax1 = plt.subplots(figsize=(7, 4))
ax1.plot(x, USER_COUNT, "b", lw=1.5, label="活跃用户数")
ax1.plot(x, USER_COUNT, "bo", ms=4)
ax1.set_xlabel("时段")
ax1.set_ylabel("活跃用户数")
ax1.set_xticks(x)
ax1.set_xticklabels(TIME_LABELS, rotation=45)
ax1.grid(True)
ax1.legend(loc="upper left")

ax2 = ax1.twinx()
ax2.plot(x, TRADITIONAL_DELAY, "g", lw=1.5, label="传统策略时延")
ax2.plot(x, TRADITIONAL_DELAY, "g^", ms=4)
ax2.plot(x, OPTIMIZED_DELAY, "r", lw=1.5, label="优化策略时延")
ax2.plot(x, OPTIMIZED_DELAY, "rs", ms=4)
ax2.set_ylabel("平均时延 (ms)")
ax2.legend(loc="upper right")

plt.title("用户数与平均时延双轴对比")
fig.tight_layout()

out = os.path.join(OUTPUT_DIR, "fig03_双轴折线图.png")
fig.savefig(out, dpi=300, bbox_inches="tight")
print(f"已保存: {out}")
