# Generated by Django 3.2.6 on 2021-09-08 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('owner', '0003_alter_order_expected_delivery_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='expected_delivery_date',
            field=models.DateField(default='elp', null=True),
        ),
    ]
