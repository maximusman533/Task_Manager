# Generated by Django 2.1.4 on 2018-12-26 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TM', '0016_auto_20181226_1438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, default='avatars/default_avatar.png', null=True, upload_to='avatars/', verbose_name='Аватар'),
        ),
    ]
