import pyecharts.options as opts
from pyecharts.charts import Line, Grid
from pyecharts.commons.utils import JsCode
from pyecharts.globals import CurrentConfig

CurrentConfig.ONLINE_HOST = 'http://127.0.0.1:8000/static/js/echarts-liquidfill/'


class LogEcharts(object):

    @classmethod
    def cpu_avg_html(cls, cpu_avg, date_time, title):
        x_data = date_time
        y_data = cpu_avg

        background_color_js = (
            "new echarts.graphic.LinearGradient(0, 0, 0, 1, "
            "[{offset: 0, color: '#c86589'}, {offset: 1, color: '#06a7ff'}], false)"
        )
        area_color_js = (
            "new echarts.graphic.LinearGradient(0, 0, 0, 1, "
            "[{offset: 0, color: '#eb64fb'}, {offset: 1, color: '#3fbbff0d'}], false)"
        )

        cpu_avg_line_log = (
            Line(init_opts=opts.InitOpts(width='100%', height='100%', bg_color=JsCode(background_color_js)))
                .add_xaxis(xaxis_data=x_data)
                .add_yaxis(
                series_name=title,
                y_axis=y_data,
                is_smooth=True,
                is_symbol_show=True,
                symbol="circle",
                symbol_size=6,
                linestyle_opts=opts.LineStyleOpts(color="#fff"),
                label_opts=opts.LabelOpts(is_show=True, position="top", color="white"),
                itemstyle_opts=opts.ItemStyleOpts(
                    color="red", border_color="#fff", border_width=3
                ),
                tooltip_opts=opts.TooltipOpts(is_show=False),
                areastyle_opts=opts.AreaStyleOpts(color=JsCode(area_color_js), opacity=1),
            )
                .set_global_opts(
                title_opts=opts.TitleOpts(
                    title=title,
                    pos_bottom="5%",
                    pos_left="center",
                    title_textstyle_opts=opts.TextStyleOpts(color="#fff", font_size=16),
                ),
                xaxis_opts=opts.AxisOpts(
                    type_="category",
                    boundary_gap=False,
                    axislabel_opts=opts.LabelOpts(margin=30, color="#ffffff63"),
                    axisline_opts=opts.AxisLineOpts(is_show=False),
                    axistick_opts=opts.AxisTickOpts(
                        is_show=True,
                        length=25,
                        linestyle_opts=opts.LineStyleOpts(color="#ffffff1f"),
                    ),
                    splitline_opts=opts.SplitLineOpts(
                        is_show=True, linestyle_opts=opts.LineStyleOpts(color="#ffffff1f")
                    ),
                ),
                yaxis_opts=opts.AxisOpts(
                    type_="value",
                    position="right",
                    axislabel_opts=opts.LabelOpts(margin=20, color="#ffffff63"),
                    axisline_opts=opts.AxisLineOpts(
                        linestyle_opts=opts.LineStyleOpts(width=2, color="#fff")
                    ),
                    axistick_opts=opts.AxisTickOpts(
                        is_show=True,
                        length=15,
                        linestyle_opts=opts.LineStyleOpts(color="#ffffff1f"),
                    ),
                    splitline_opts=opts.SplitLineOpts(
                        is_show=True, linestyle_opts=opts.LineStyleOpts(color="#ffffff1f")
                    ),
                ),
                legend_opts=opts.LegendOpts(is_show=False),
            )
        )

        (
            Grid()
                .add(
                cpu_avg_line_log,
                grid_opts=opts.GridOpts(
                    pos_top="20%",
                    pos_left="10%",
                    pos_right="10%",
                    pos_bottom="15%",
                    is_contain_label=True,
                ),
            )
        )
        return cpu_avg_line_log.render_embed()
