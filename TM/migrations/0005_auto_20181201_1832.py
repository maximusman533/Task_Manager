# Generated by Django 2.1.2 on 2018-12-01 15:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TM', '0004_auto_20181201_1826'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'verbose_name': 'Задача', 'verbose_name_plural': 'Задачи'},
        ),
        migrations.AlterModelTable(
            name='task',
            table='Задача',
        ),
    ]