import datetime
from pyecharts import options as opts
from pyecharts.charts import Grid, Liquid, Gauge
from pyecharts.commons.utils import JsCode
from pyecharts.globals import CurrentConfig

CurrentConfig.ONLINE_HOST = 'http://127.0.0.1:8000/static/js/echarts-liquidfill/'


class Chart(object):
    dt = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # cpu平均使用率水球图
    def liquid_html(self, chart_id, title, val):
        """
        :param chart_id:  图形id
        :param title:  图形标题
        :param val: 指定值
        :return:  返回html结构代码
        """

        liquid = Liquid(opts.InitOpts(width='100%', height='100%')).add(
            title,
            [val / 100],
            center=["50%", "50%"],
            label_opts=opts.LabelOpts(
                font_size=50,
                formatter=JsCode(
                    """function (param) {
                            return (Math.floor(param.value * 10000) / 100) + '%';
                        }"""
                ),
                position="inside",
            ),
        )

        # 生成返回文件
        # grid = Grid().add(liquid, grid_opts=opts.GridOpts()).add(liquid, grid_opts=opts.GridOpts())
        # grid.render("multiple_liquid.html")

        # 设置全局参数
        liquid.set_global_opts(
            title_opts=opts.TitleOpts(title=title + '\n' + self.dt, pos_left='center', pos_top='1px'))
        liquid.chart_id = chart_id
        return liquid.render_embed()

    # 每核cpu使用率仪表盘图
    def gauge_html(self, chart_id, title, value):
        gauge = (
            Gauge(init_opts=opts.InitOpts(width="100%", height="100%"))
                .add(series_name=title,
                     data_pair=[[title, value]],
                     radius='70%',
                     split_number=10,
                     detail_label_opts=opts.LabelOpts(
                         formatter="{value}%",font_size=22, color="blue", font_family="Microsoft YaHei"
                     ),
                 )
        )
        gauge.set_global_opts(title_opts=opts.TitleOpts(title=title + '\n' + self.dt, pos_left='center', pos_top='16px'))
        gauge.chart_id = chart_id
        return gauge.render_embed()
