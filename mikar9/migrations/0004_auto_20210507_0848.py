# Generated by Django 2.2.4 on 2021-05-07 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mikar9', '0003_auto_20210507_0849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='log_date',
            field=models.DateTimeField(),
        ),
    ]
