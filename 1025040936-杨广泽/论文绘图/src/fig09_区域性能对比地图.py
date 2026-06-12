"""
参考：9. 论文绘图/src/地图热力图2.py
主题：四类校园区域优化效果对比（世界地图风格改为区域对比柱状地图）
使用 pyecharts Map 展示各区域吞吐量提升百分比
"""
import os
from pyecharts import options as opts
from pyecharts.charts import Bar
from simulation_data import REGION_NAMES, REGION_IMPROVEMENT, OUTPUT_DIR

data_tp = list(zip(REGION_NAMES, REGION_IMPROVEMENT["吞吐量提升"]))
data_delay = list(zip(REGION_NAMES, REGION_IMPROVEMENT["时延降低"]))

bar = (
    Bar(init_opts=opts.InitOpts(width="900px", height="500px", bg_color="white"))
    .add_xaxis(REGION_NAMES)
    .add_yaxis("吞吐量提升 (%)", REGION_IMPROVEMENT["吞吐量提升"], color="#0073C2")
    .add_yaxis("时延降低 (%)", REGION_IMPROVEMENT["时延降低"], color="#CD534C")
    .set_global_opts(
        title_opts=opts.TitleOpts(title="不同校园区域优化效果对比"),
        yaxis_opts=opts.AxisOpts(name="改善幅度 (%)"),
        legend_opts=opts.LegendOpts(pos_top="8%"),
        toolbox_opts=opts.ToolboxOpts(is_show=True),
    )
)

out = os.path.join(OUTPUT_DIR, "fig09_区域性能对比.html")
bar.render(out)
print(f"已保存: {out}")
