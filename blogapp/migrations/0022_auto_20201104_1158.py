# Generated by Django 3.1.3 on 2020-11-04 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0021_auto_20201104_1104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='video',
            field=models.FileField(upload_to='video/%y'),
        ),
    ]