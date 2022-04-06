from django.utils import timezone
from django.db import models

from User.models import Users


class HeartSounds(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=5000,
                                   default='在生理学中，心音（英语：heart sounds），即心脏的声音，是心脏在运作时，血液流经心脏时产生的震动波。具体来说，是瓣膜开起与关闭时产生的湍流造成的震动波，或由心肌收缩、心脏瓣膜关闭和血液撞击心室壁、大动脉壁等引起的振动。一般来说，这种震动波能量较低，不易传递至空气形成声波，但仍可用听诊器在胸壁一定部位将该波转成声音，由于该声音可反映心脏瓣膜的运作情形，因此在心脏听诊，医师可以使用听诊器听这些独特而鲜明的声音提供有关心脏情况的重要资讯。')
    file_path = models.CharField(max_length=100)
    created_time = models.DateTimeField('心音主体创建时间', default=timezone.now)
    owner = models.ForeignKey(Users, on_delete=models.CASCADE)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = '心音主体'
        verbose_name_plural = '心音主体'


class Introduce(models.Model):
    """关联心音数据的参数"""
    choices = (
        ('male', 'male'),
        ('female', 'female'),
        ('child', 'child'),
        ('standard','standard'),
    )
    name = models.CharField(max_length=50)
    heartSounds = models.ForeignKey(HeartSounds, on_delete=models.CASCADE)
    sample_from = models.CharField('采样来源', choices=choices, max_length=10,default='暂无')
    duration_for_sample = models.CharField('采样时间', help_text='请采用秒数为计时单位', max_length=20,default='暂无')
    style_of_sampling = models.CharField('采样方式', max_length=50,default='暂无')
    sample_frequency = models.CharField('采样频率', max_length=50,default='暂无')

    def __str__(self):
        return self.heartSounds.name

    class Meta:
        verbose_name = '心音介绍'
        verbose_name_plural = '心音介绍'

class Dynamic(models.Model):
    """数据库的动态字段"""
    heartSounds = models.ForeignKey(HeartSounds, on_delete=models.CASCADE)
    count_for_download = models.IntegerField(default=0)
    dynamicPicture = models.ImageField('心音动图,暂未实现', default='static/images/heartsounds_images/1200px'
                                                            '-First_heart_sound_110bpm.png')

    class Meta:
        verbose_name = '心音动态部分'
        verbose_name_plural = '心音动态部分'

class PopuOfScience(models.Model):
    """科普部分"""
    heartSounds=models.ForeignKey(HeartSounds,on_delete=models.CASCADE)
    # 科普描述文本.
    text=models.TextField(default='暂时还没有科普文本',max_length=3000)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name="心音科普"
        verbose_name_plural="心音科普"
