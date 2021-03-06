# Generated by Django 4.0.3 on 2022-04-06 12:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Exhibition', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='heartsounds',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='dynamic',
            name='heartSounds',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Exhibition.heartsounds'),
        ),
    ]
