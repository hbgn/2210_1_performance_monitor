from django.db import models

"""
    cpu模型类分析
    采集时间
    cpu平均使用率
    每核使用率
    核心数量
    线程数量
"""


class BaseModel(models.Model):
    """
    日期基类
    """
    create_date = models.DateField(verbose_name="创建日期", auto_now_add=True)  # 创建日期
    create_time = models.TimeField(verbose_name="采集时间", auto_now_add=True)  # 创建时间
    create_dt = models.DateTimeField(verbose_name="采集日期时间", auto_now_add=True)  # 创建日期时间

    class Meta:
        abstract = True


class Cpu(BaseModel):
    percent_avg = models.FloatField(verbose_name="cpu平均使用率")
    percent_per = models.CharField(verbose_name="每核cpu使用率", max_length=200)
    num_p = models.IntegerField(verbose_name="核心数量")
    num_l = models.IntegerField(verbose_name="线程数量")
