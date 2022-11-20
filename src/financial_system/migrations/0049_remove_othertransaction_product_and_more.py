# Generated by Django 4.1.3 on 2022-11-07 03:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('financial_system', '0048_alter_agent_options_alter_user_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='othertransaction',
            name='product',
        ),
        migrations.RemoveField(
            model_name='othertransaction',
            name='transaction_type',
        ),
        migrations.RemoveField(
            model_name='othertransaction',
            name='user',
        ),
        migrations.RemoveField(
            model_name='property',
            name='agent',
        ),
        migrations.RemoveField(
            model_name='propertytransaction',
            name='agent',
        ),
        migrations.RemoveField(
            model_name='propertytransaction',
            name='property',
        ),
        migrations.RemoveField(
            model_name='propertytransaction',
            name='transaction_type',
        ),
        migrations.RemoveField(
            model_name='propertytransaction',
            name='user',
        ),
        migrations.RemoveField(
            model_name='stocktransaction',
            name='agent',
        ),
        migrations.RemoveField(
            model_name='stocktransaction',
            name='stock',
        ),
        migrations.RemoveField(
            model_name='stocktransaction',
            name='transaction_type',
        ),
        migrations.RemoveField(
            model_name='stocktransaction',
            name='user',
        ),
        migrations.DeleteModel(
            name='MiscProduct',
        ),
        migrations.DeleteModel(
            name='OtherTransaction',
        ),
        migrations.DeleteModel(
            name='Property',
        ),
        migrations.DeleteModel(
            name='PropertyTransaction',
        ),
        migrations.DeleteModel(
            name='Stock',
        ),
        migrations.DeleteModel(
            name='StockTransaction',
        ),
        migrations.DeleteModel(
            name='TransactionTypes',
        ),
        migrations.DeleteModel(
            name='Agent',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
