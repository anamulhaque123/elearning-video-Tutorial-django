# Generated by Django 2.2.3 on 2019-08-25 16:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0016_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='image',
            new_name='video',
        ),
    ]