"""
参考：9. 论文绘图/src/plt2.py
主题：论文正式插图（图4.1、图4.2、图4.3）— 学术风格折线图
"""
import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
from simulation_data import (
    TIME_LABELS, TRADITIONAL_THROUGHPUT, OPTIMIZED_THROUGHPUT,
    TRADITIONAL_DELAY, OPTIMIZED_DELAY,
    TRADITIONAL_LOAD_STD, OPTIMIZED_LOAD_STD,
    OUTPUT_DIR,
)

plt.rcParams["font.sans-serif"] = ["SimHei", "Microsoft YaHei", "Times New Roman"]
plt.rcParams["axes.unicode_minus"] = False
plt.rcParams["font.size"] = 12
plt.rcParams["axes.linewidth"] = 1

colors = ["#0073C2", "#CD534C"]
x = np.arange(len(TIME_LABELS))


def _style_axis(ax, xlabel, ylabel, title):
    yminor = MultipleLocator(ax.get_ylim()[1] / 20)
    xminor = MultipleLocator(1)
    ax.yaxis.set_minor_locator(yminor)
    ax.xaxis.set_minor_locator(xminor)
    ax.tick_params(which="major", length=5, width=1.5, direction="in", top=True, right=True)
    ax.tick_params(which="minor", length=3, width=1, direction="in", top=True, right=True)
    ax.set_xlabel(xlabel, fontsize=13, labelpad=5)
    ax.set_ylabel(ylabel, fontsize=13, labelpad=5)
    ax.set_title(title, fontsize=14, pad=10)
    ax.grid(which="major", ls="--", alpha=0.8, lw=0.8)
    ax.set_xticks(x)
    ax.set_xticklabels(TIME_LABELS, rotation=45, ha="right")


def plot_comparison(y_trad, y_opt, ylabel, title, filename):
    fig, ax = plt.subplots(figsize=(5, 3.5), dpi=400)
    ax.plot(x, y_trad, color=colors[0], lw=1.8, marker="o", ms=4, label="传统RSSI优先")
    ax.plot(x, y_opt, color=colors[1], lw=1.8, marker="s", ms=4, label="负载感知优化")
    _style_axis(ax, "时段", ylabel, title)
    ax.legend(fontsize=9, loc="best")
    fig.tight_layout()
    out = os.path.join(OUTPUT_DIR, filename)
    fig.savefig(out, dpi=600, bbox_inches="tight")
    fig.savefig(out.replace(".png", ".eps"), format="eps", dpi=600)
    print(f"已保存: {out}")
    plt.close(fig)


plot_comparison(
    TRADITIONAL_THROUGHPUT, OPTIMIZED_THROUGHPUT,
    "平均吞吐量 (Mbps)", "平均吞吐量对比", "fig10_图4.1_平均吞吐量对比.png",
)
plot_comparison(
    TRADITIONAL_DELAY, OPTIMIZED_DELAY,
    "平均时延 (ms)", "平均时延对比", "fig10_图4.2_平均时延对比.png",
)
plot_comparison(
    TRADITIONAL_LOAD_STD, OPTIMIZED_LOAD_STD,
    "负载标准差", "接入点负载标准差对比", "fig10_图4.3_负载标准差对比.png",
)
