# Generated by Django 4.1.3 on 2022-11-07 01:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('financial_system', '0035_delete_miscproduct_remove_othertransaction_agent_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=125)),
                ('firm', models.CharField(max_length=125)),
                ('address', models.CharField(max_length=125)),
                ('fee', models.DecimalField(decimal_places=2, max_digits=7)),
            ],
        ),
        migrations.CreateModel(
            name='MiscProduct',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=125)),
                ('product_type', models.CharField(max_length=125)),
                ('description', models.TextField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=125)),
                ('open_price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('close_price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('high_price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('low_price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('volume', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TransactionTypes',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=125)),
            ],
            options={
                'verbose_name': 'Transaction Type',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=125)),
                ('address', models.CharField(max_length=125)),
                ('age', models.CharField(max_length=3)),
                ('sex', models.CharField(max_length=6)),
                ('occupation', models.CharField(max_length=125)),
            ],
        ),
        migrations.CreateModel(
            name='StockTransaction',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField(auto_now=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('shares', models.IntegerField()),
                ('agent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='financial_system.agent')),
                ('transaction_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='financial_system.transactiontypes')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='financial_system.user')),
            ],
            options={
                'verbose_name': 'Stock Transaction',
            },
        ),
        migrations.CreateModel(
            name='PropertyTransaction',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField(auto_now=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('agent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='financial_system.agent')),
                ('transaction_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='financial_system.transactiontypes')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='financial_system.user')),
            ],
            options={
                'verbose_name': 'Property Transaction',
            },
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('address', models.CharField(max_length=125)),
                ('transaction_price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='financial_system.agent')),
            ],
            options={
                'verbose_name_plural': 'properties',
            },
        ),
        migrations.CreateModel(
            name='OtherTransaction',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('product', models.CharField(max_length=125)),
                ('date', models.DateTimeField(auto_now=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('amount', models.IntegerField()),
                ('agent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='financial_system.agent')),
                ('transaction_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='financial_system.transactiontypes')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='financial_system.user')),
            ],
            options={
                'verbose_name': 'Other Product Transaction',
            },
        ),
    ]