# Generated by Django 3.1.3 on 2020-11-27 08:52

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_shorties_https'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shorties',
            name='alias',
            field=models.UUIDField(default=uuid.uuid4, unique=True),
        ),
    ]
