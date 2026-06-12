"""一键生成全部论文配图"""
import importlib
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

scripts = [
    "fig01_多参数曲线",
    "fig02_折线图",
    "fig03_双轴折线图",
    "fig04_热力图",
    "fig05_散点图",
    "fig06_直方图",
    "fig07_三维图",
    "fig08_校园区域热力图",
    "fig09_区域性能对比地图",
    "fig10_论文风格图",
    "fig11_柱状图",
]

for name in scripts:
    print(f"\n>>> 运行 {name} ...")
    importlib.import_module(name)

print("\n全部配图生成完成，输出目录: ../output/")
