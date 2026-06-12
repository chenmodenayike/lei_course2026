"""
参考：9. 论文绘图/src/三维图.py
主题：负载评价权重(α, β)与系统平均吞吐量的三维曲面关系
对应论文表4.3参数敏感性分析
"""
import os
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401
from simulation_data import WEIGHT_SENSITIVITY, setup_matplotlib_chinese, OUTPUT_DIR

setup_matplotlib_chinese()

alpha = np.linspace(0.15, 0.55, 24)
beta = np.linspace(0.20, 0.50, 24)
alpha_grid, beta_grid = np.meshgrid(alpha, beta)

# 基于表4.3数据插值构造连续曲面
ref_alpha = np.array([w["alpha"] for w in WEIGHT_SENSITIVITY])
ref_beta = np.array([w["beta"] for w in WEIGHT_SENSITIVITY])
ref_tp = np.array([w["throughput"] for w in WEIGHT_SENSITIVITY])

throughput_surface = np.zeros_like(alpha_grid)
for i in range(alpha_grid.shape[0]):
    for j in range(alpha_grid.shape[1]):
        a, b = alpha_grid[i, j], beta_grid[i, j]
        eta = max(0.05, 1 - a - b)
        dist = (ref_alpha - a) ** 2 + (ref_beta - b) ** 2 + (np.array([w["eta"] for w in WEIGHT_SENSITIVITY]) - eta) ** 2
        weights = 1 / (dist + 0.01)
        throughput_surface[i, j] = np.average(ref_tp, weights=weights)

fig = plt.figure(figsize=(9, 6))
ax = fig.add_subplot(111, projection="3d")
surf = ax.plot_surface(
    alpha_grid, beta_grid, throughput_surface,
    rstride=2, cstride=2, cmap=plt.cm.coolwarm, linewidth=0.5, antialiased=True,
)
ax.set_xlabel("用户数权重 α")
ax.set_ylabel("流量权重 β")
ax.set_zlabel("平均吞吐量 (Mbps)")
ax.set_title("负载评价权重与系统吞吐量关系")
fig.colorbar(surf, ax=ax, shrink=0.5, label="Mbps")

out = os.path.join(OUTPUT_DIR, "fig07_权重吞吐量三维图.png")
fig.savefig(out, dpi=300, bbox_inches="tight")
print(f"已保存: {out}")
