# Generated by Django 4.1.3 on 2022-11-06 16:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('financial_system', '0020_alter_usertransaction_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usertransaction',
            options={'verbose_name': 'User Transaction'},
        ),
    ]
