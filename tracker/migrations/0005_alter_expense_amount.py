# Generated by Django 3.2.9 on 2021-12-14 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0004_remove_expense_balance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='amount',
            field=models.FloatField(default=0),
        ),
    ]
