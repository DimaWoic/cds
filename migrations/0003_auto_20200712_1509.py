# Generated by Django 2.2 on 2020-07-12 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cds', '0002_auto_20200706_1803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='telephone',
            field=models.IntegerField(verbose_name='Телефон'),
        ),
    ]
