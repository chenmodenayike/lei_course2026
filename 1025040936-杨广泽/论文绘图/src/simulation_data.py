"""智慧校园无线网络仿真数据（与论文附录表1.1、表1.2及第四章表格一致）"""
import os
import numpy as np

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "output")

TIME_LABELS = [
    "8:00", "9:00", "10:00", "11:00", "12:00", "13:00",
    "14:00", "15:00", "16:00", "17:00", "18:00", "19:00",
    "20:00", "21:00", "22:00",
]

USER_COUNT = [95, 120, 180, 260, 210, 160, 145, 170, 230, 285, 310, 340, 355, 330, 260]

TRADITIONAL_THROUGHPUT = [
    65.93, 63.85, 67.95, 72.95, 68.29, 66.80, 65.97, 64.54,
    72.26, 74.64, 74.05, 77.14, 78.35, 75.90, 71.06,
]

OPTIMIZED_THROUGHPUT = [
    73.84, 71.52, 76.58, 84.26, 77.68, 74.82, 73.89, 72.69,
    82.80, 86.81, 86.61, 90.25, 92.02, 88.54, 82.08,
]

TRADITIONAL_DELAY = [
    23.54, 30.31, 36.05, 45.15, 36.05, 36.90, 32.26, 35.05,
    41.27, 47.89, 49.15, 54.43, 56.12, 51.36, 43.55,
]

OPTIMIZED_DELAY = [
    19.31, 24.85, 29.38, 35.89, 29.11, 30.26, 26.45, 28.62,
    33.12, 37.63, 38.25, 41.33, 42.48, 39.44, 34.62,
]

TRADITIONAL_LOAD_STD = [
    0.539, 0.566, 0.597, 0.726, 0.627, 0.588, 0.562, 0.603,
    0.671, 0.754, 0.781, 0.832, 0.851, 0.809, 0.704,
]

OPTIMIZED_LOAD_STD = [
    0.352, 0.388, 0.424, 0.496, 0.422, 0.415, 0.384, 0.408,
    0.449, 0.513, 0.529, 0.562, 0.574, 0.548, 0.478,
]

AP_NAMES = [
    "教学楼AP1", "教学楼AP2", "教学楼AP3", "教学楼AP4",
    "宿舍区AP1", "宿舍区AP2", "宿舍区AP3", "宿舍区AP4",
    "图书馆AP1", "图书馆AP2",
    "实验室AP1", "实验室AP2",
]

REGION_NAMES = ["教学楼", "宿舍区", "图书馆", "实验室"]

REGION_IMPROVEMENT = {
    "吞吐量提升": [16.8, 14.2, 10.6, 8.9],
    "时延降低": [21.5, 23.1, 17.4, 12.7],
}

WEIGHT_SENSITIVITY = [
    {"alpha": 0.50, "beta": 0.30, "eta": 0.20, "throughput": 82.14, "delay": 34.80, "load_std": 0.402},
    {"alpha": 0.33, "beta": 0.34, "eta": 0.33, "throughput": 83.27, "delay": 33.76, "load_std": 0.391},
    {"alpha": 0.25, "beta": 0.45, "eta": 0.30, "throughput": 84.05, "delay": 34.12, "load_std": 0.398},
    {"alpha": 0.20, "beta": 0.30, "eta": 0.50, "throughput": 81.66, "delay": 32.95, "load_std": 0.409},
]

REGION_PEAK_LOAD = {
    "教学楼": 0.82,
    "宿舍区": 0.91,
    "图书馆": 0.68,
    "实验室": 0.55,
}


def association_score(link_quality, ap_load, priority, w1=0.4, w2=0.4, w3=0.2):
    """用户关联评分 Sij = w1*Qij + w2*(1-Lj) + w3*Pi"""
    return w1 * link_quality + w2 * (1 - ap_load) + w3 * priority


def generate_ap_loads(target_std, target_mean=0.62, n_ap=12, seed=42):
    """生成与给定标准差一致的12个接入点负载序列"""
    rng = np.random.default_rng(seed)
    loads = rng.normal(target_mean, target_std * 0.85, n_ap)
    loads = np.clip(loads, 0.15, 0.95)
    loads = loads - loads.mean() + target_mean
    scale = target_std / (loads.std() + 1e-9)
    loads = loads - loads.mean()
    loads = loads * scale + target_mean
    return np.clip(loads, 0.12, 0.96)


def setup_matplotlib_chinese():
    import matplotlib.pyplot as plt
    plt.rcParams["font.sans-serif"] = ["SimHei", "Microsoft YaHei", "DejaVu Sans"]
    plt.rcParams["axes.unicode_minus"] = False
