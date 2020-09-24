# Generated by Django 2.2 on 2020-09-24 13:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cds', '0006_auto_20200924_1319'),
    ]

    operations = [
        migrations.AddField(
            model_name='rollingstock',
            name='depot',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='cds.Depot', verbose_name='Депо'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rollingstock',
            name='transport',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='cds.Transport', verbose_name='Транспорт'),
            preserve_default=False,
        ),
    ]
