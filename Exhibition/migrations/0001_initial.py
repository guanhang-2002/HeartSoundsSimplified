# Generated by Django 4.0.3 on 2022-04-06 12:42

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dynamic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count_for_download', models.IntegerField(default=0)),
                ('dynamicPicture', models.ImageField(default='static/images/heartsounds_images/1200px-First_heart_sound_110bpm.png', upload_to='', verbose_name='心音动图,暂未实现')),
            ],
            options={
                'verbose_name': '心音动态部分',
                'verbose_name_plural': '心音动态部分',
            },
        ),
        migrations.CreateModel(
            name='HeartSounds',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(default='在生理学中，心音（英语：heart sounds），即心脏的声音，是心脏在运作时，血液流经心脏时产生的震动波。具体来说，是瓣膜开起与关闭时产生的湍流造成的震动波，或由心肌收缩、心脏瓣膜关闭和血液撞击心室壁、大动脉壁等引起的振动。一般来说，这种震动波能量较低，不易传递至空气形成声波，但仍可用听诊器在胸壁一定部位将该波转成声音，由于该声音可反映心脏瓣膜的运作情形，因此在心脏听诊，医师可以使用听诊器听这些独特而鲜明的声音提供有关心脏情况的重要资讯。', max_length=5000)),
                ('file_path', models.CharField(max_length=100)),
                ('created_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='心音主体创建时间')),
            ],
            options={
                'verbose_name': '心音主体',
                'verbose_name_plural': '心音主体',
            },
        ),
        migrations.CreateModel(
            name='PopuOfScience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(default='暂时还没有科普文本', max_length=3000)),
                ('heartSounds', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Exhibition.heartsounds')),
            ],
            options={
                'verbose_name': '心音科普',
                'verbose_name_plural': '心音科普',
            },
        ),
        migrations.CreateModel(
            name='Introduce',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('sample_from', models.CharField(choices=[('male', 'male'), ('female', 'female'), ('child', 'child'), ('standard', 'standard')], default='暂无', max_length=10, verbose_name='采样来源')),
                ('duration_for_sample', models.CharField(default='暂无', help_text='请采用秒数为计时单位', max_length=20, verbose_name='采样时间')),
                ('style_of_sampling', models.CharField(default='暂无', max_length=50, verbose_name='采样方式')),
                ('sample_frequency', models.CharField(default='暂无', max_length=50, verbose_name='采样频率')),
                ('heartSounds', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Exhibition.heartsounds')),
            ],
            options={
                'verbose_name': '心音介绍',
                'verbose_name_plural': '心音介绍',
            },
        ),
    ]