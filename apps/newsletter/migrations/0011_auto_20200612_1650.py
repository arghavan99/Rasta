# Generated by Django 2.2.11 on 2020-06-12 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0010_emailtext_link_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscriber',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]