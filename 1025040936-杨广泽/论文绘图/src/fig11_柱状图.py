"""
参考：9. 论文绘图/src/bar_base_.html
主题：各时段两种策略吞吐量差值柱状图（优化增益）
对应论文第四章仿真结果分析
"""
import os
from pyecharts import options as opts
from pyecharts.charts import Bar
from simulation_data import (
    TIME_LABELS, TRADITIONAL_THROUGHPUT, OPTIMIZED_THROUGHPUT, OUTPUT_DIR,
)

gain = [round(o - t, 2) for t, o in zip(TRADITIONAL_THROUGHPUT, OPTIMIZED_THROUGHPUT)]

bar = (
    Bar(init_opts=opts.InitOpts(width="900px", height="500px", bg_color="white"))
    .add_xaxis(TIME_LABELS)
    .add_yaxis("吞吐量提升 (Mbps)", gain, color="#0073C2",
               label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(
        title_opts=opts.TitleOpts(title="负载感知策略各时段吞吐量增益"),
        xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=45)),
        yaxis_opts=opts.AxisOpts(name="Mbps"),
        toolbox_opts=opts.ToolboxOpts(is_show=True),
    )
)

out = os.path.join(OUTPUT_DIR, "fig11_吞吐量增益柱状图.html")
bar.render(out)
print(f"已保存: {out}")
