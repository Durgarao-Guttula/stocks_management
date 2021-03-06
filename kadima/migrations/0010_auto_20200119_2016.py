# Generated by Django 3.0.2 on 2020-01-19 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kadima', '0009_stockdata_saved_to_history'),
    ]

    operations = [
        migrations.AddField(
            model_name='stockdata',
            name='dividends',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='stockdata',
            name='profit',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='stockdata',
            name='purchase_price',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='stockdata',
            name='selling_price',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='stockdata',
            name='stocks_bought',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='stockdata',
            name='stocks_sold',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='stockdata',
            name='total_profit',
            field=models.FloatField(null=True),
        ),
    ]
