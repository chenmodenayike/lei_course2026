"""
参考：9. 论文绘图/src/地图热力图.py
主题：智慧校园四类区域网络负载热力图（pyecharts Geo）
"""
import os
from pyecharts import options as opts
from pyecharts.charts import Geo
from pyecharts.globals import ChartType
from simulation_data import REGION_NAMES, REGION_PEAK_LOAD, OUTPUT_DIR

# 南京邮电大学仙林校区周边示意坐标
region_coords = {
    "教学楼": [118.958, 32.118],
    "宿舍区": [118.962, 32.115],
    "图书馆": [118.960, 32.117],
    "实验室": [118.955, 32.120],
}

values = [REGION_PEAK_LOAD[r] * 100 for r in REGION_NAMES]

geo = Geo()
geo.add_schema(maptype="china")
for name, coord in region_coords.items():
    geo.add_coordinate(name, coord[0], coord[1])

geo.add(
    "区域峰值负载(%)",
    [list(z) for z in zip(REGION_NAMES, values)],
    type_=ChartType.EFFECT_SCATTER,
)
geo.set_series_opts(label_opts=opts.LabelOpts(is_show=True))
geo.set_global_opts(
    title_opts=opts.TitleOpts(title="智慧校园各区域网络负载热力图"),
    visualmap_opts=opts.VisualMapOpts(max_=100, min_=40, is_piecewise=False),
)

out = os.path.join(OUTPUT_DIR, "fig08_校园区域热力图.html")
geo.render(out)
print(f"已保存: {out}")
