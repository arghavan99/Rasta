# Generated by Django 2.2.11 on 2020-06-27 22:08

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0003_auto_20200627_2207'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscriber',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='subscriber',
            name='unique_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]
