# Generated by Django 2.2.4 on 2021-05-08 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mikar9', '0006_auto_20210507_1713'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='claim',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='invoice',
            name='paid',
            field=models.BooleanField(default=False),
        ),
    ]