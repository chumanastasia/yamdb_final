# Generated by Django 2.2.16 on 2022-07-13 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_auto_20220713_2240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('admin', 'Admin'), ('moderator', 'Moderator'), ('user', 'User')], default='user', max_length=50, verbose_name='role'),
        ),
    ]
