# Generated by Django 3.0.2 on 2020-01-27 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kadima', '0014_auto_20200126_0832'),
    ]

    operations = [
        migrations.AddField(
            model_name='stockdata',
            name='table_index',
            field=models.IntegerField(default=0),
        ),
    ]
