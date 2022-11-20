# Generated by Django 4.1.3 on 2022-11-06 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financial_system', '0005_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='fee',
            field=models.DecimalField(decimal_places=2, max_digits=7),
        ),
        migrations.AlterField(
            model_name='property',
            name='transaction_price',
            field=models.DecimalField(decimal_places=2, max_digits=9),
        ),
        migrations.AlterField(
            model_name='stock',
            name='close_price',
            field=models.DecimalField(decimal_places=2, max_digits=9),
        ),
        migrations.AlterField(
            model_name='stock',
            name='high_price',
            field=models.DecimalField(decimal_places=2, max_digits=9),
        ),
        migrations.AlterField(
            model_name='stock',
            name='low_price',
            field=models.DecimalField(decimal_places=2, max_digits=9),
        ),
        migrations.AlterField(
            model_name='stock',
            name='open_price',
            field=models.DecimalField(decimal_places=2, max_digits=9),
        ),
        migrations.AlterField(
            model_name='usertransaction',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=9),
        ),
    ]