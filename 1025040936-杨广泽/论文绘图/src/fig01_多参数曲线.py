"""
参考：9. 论文绘图/src/main.py
主题：不同负载权重下用户关联评分随链路质量的变化曲线
对应论文式(2.3)，展示 w1 取不同值时 Sij 对链路质量的响应
"""
import os
import numpy as np
import matplotlib.pyplot as plt
from simulation_data import association_score, setup_matplotlib_chinese, OUTPUT_DIR

setup_matplotlib_chinese()

link_quality = np.linspace(0.3, 1.0, 201)
ap_load = 0.65
priority = 0.8

fig, ax = plt.subplots(figsize=(4, 3), dpi=200)
colors = ["#0073C2", "#EFC000", "#868686", "#CD534C", "#7AA6DC", "#003C67"]
for w1, c in zip([0.2, 0.3, 0.4, 0.5, 0.6, 0.7], colors):
    w2 = (1 - w1) * 0.67
    w3 = 1 - w1 - w2
    scores = [association_score(q, ap_load, priority, w1, w2, w3) for q in link_quality]
    ax.plot(link_quality, scores, color=c, label=f"w1={w1:.1f}")

ax.set_xlabel("链路质量 Qij")
ax.set_ylabel("关联评分 Sij")
ax.set_title("不同权重下用户关联评分曲线")
ax.legend(fontsize=7, title="链路质量权重", loc="lower right")
ax.grid(ls="--", alpha=0.6)
fig.tight_layout()

out = os.path.join(OUTPUT_DIR, "fig01_关联评分多参数曲线.png")
fig.savefig(out, dpi=300, bbox_inches="tight")
print(f"已保存: {out}")
