# Generated by Django 3.2.6 on 2021-08-26 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('owner', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
