# Generated by Django 4.1.3 on 2022-11-08 22:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('financial_system', '0061_bond_alter_agent_table_alter_user_table'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ListStocksOnDate',
        ),
        migrations.DeleteModel(
            name='ListUserTransactions',
        ),
    ]