# Generated by Django 2.2.11 on 2020-06-12 15:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0003_auto_20200612_1547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscriber',
            name='date_joint',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 12, 15, 51, 37, 700727)),
        ),
    ]
