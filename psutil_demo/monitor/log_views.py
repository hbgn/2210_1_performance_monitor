from django.shortcuts import render
from .models import Cpu
from monitor.tools.logs_echarts import LogEcharts


def cpu_avg_log(request):
    cpu_data = Cpu.objects.all()
    date_time = []
    cpu_avg_data = []
    for line_data in cpu_data:
        date_time.append(line_data.create_dt.strftime('%Y-%m-%d %H:%M:%S'))
        cpu_avg_data.append(line_data.percent_avg)
    line_cpu_log = LogEcharts.cpu_avg_html(cpu_avg=cpu_avg_data, date_time=date_time, title="cpu平均使用率日志统计")
    return render(request, 'cpu_avg_log.html', locals())
