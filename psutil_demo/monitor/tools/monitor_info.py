# from time import sleep
import psutil


class Monitor:

    # 获取cpu的信息
    def cpu(self):
        data = dict(
            percent_avg=psutil.cpu_percent(interval=0, percpu=False),
            percent_per=psutil.cpu_percent(interval=0, percpu=True),
            num_p=psutil.cpu_count(logical=False),  # 核心数量
            num_l=psutil.cpu_count(logical=True)
        )
        return data


# if __name__ == '__main__':
#     m = Monitor()
#     for v in range(20):
#         sleep(1)
#         print(m.cpu())
