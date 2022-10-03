import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'websocket_chat.settings')
import django
django.setup()

import time
from monitor.models import Cpu
from monitor.tools.monitor_info import Monitor



def logs_monitor():
    m = Monitor()
    cpu_info = m.cpu()
    Cpu.objects.create(percent_avg=cpu_info['percent_avg'], percent_per=cpu_info['percent_per'],
                       num_p=cpu_info['num_p'], num_l=cpu_info['num_l']
                       )
if __name__ == '__main__':
    while True:
        logs_monitor()
        time.sleep(0.1)
        print('每隔0.1s写一次数据库')
