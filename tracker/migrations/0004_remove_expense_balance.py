# Generated by Django 3.2.9 on 2021-12-14 00:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0003_alter_expense_balance'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expense',
            name='balance',
        ),
    ]
