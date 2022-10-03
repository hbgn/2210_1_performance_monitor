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
        data_gauge.append(
            c.gauge_html(chart_id='per' + str(i), title='CPU' + str(i) + '使用率', value=cpu_info['percent_per'][i]))
    return render(request, 'cpu_m.html', locals())


def net_m(request):
    m = Monitor()
    net_info = m.net()
    return render(request, 'net_m.html', locals())


def mem_m(request):
    m = Monitor()
    c = Chart()
    mem_info = m.mem()
    data = []
    # for k, v in mem_info.items():
    #     data.append(c.mem_html(chart_id='mem_' + k, title='mem_' + k, value=v))

    data.append(c.mem_html(chart_id='mem_used', title='内存使用率', value=mem_info['used']/mem_info['total']))

    return render(request, 'mem_m.html', locals())


def liquid(request):
    return render(request, 'multiple_liquid.html')
