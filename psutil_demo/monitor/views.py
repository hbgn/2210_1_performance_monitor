from django.shortcuts import render
from .tools.charts import Chart
from .tools.monitor_info import Monitor


def index(request):
    return render(request, 'index.html')


def cpu_m(request):
    m = Monitor()
    c = Chart()
    cpu_info = m.cpu()
    data = c.liquid_html('cpu_avg', 'cpu平均使用率', cpu_info['percent_avg'])
    data_gauge = []
    for i in range(len(cpu_info['percent_per'])):
        data_gauge.append(c.gauge_html(chart_id='per'+str(i),title='CPU'+str(i)+'使用率',value=cpu_info['percent_per'][i]))
    return render(request, 'cpu_m.html', locals())

# def liquid(request):
#     return render(request, 'multiple_liquid.html')
