# Generated by Django 2.2 on 2020-09-14 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cds', '0004_auto_20200914_1702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='route',
            name='route',
            field=models.CharField(default='', max_length=2, verbose_name='Номер маршрута'),
        ),
    ]
