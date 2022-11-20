# Generated by Django 4.1.3 on 2022-11-05 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financial_system', '0002_miscproduct_alter_agent_id_alter_property_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='miscproduct',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='property',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='stock',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='usertransaction',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
