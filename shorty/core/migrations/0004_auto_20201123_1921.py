# Generated by Django 3.1.3 on 2020-11-23 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20201123_1130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shorties',
            name='alias',
            field=models.URLField(max_length=5, unique=True),
        ),
    ]
