# Generated by Django 4.2.2 on 2023-06-14 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table',
            name='coordinates',
            field=models.FloatField(),
        ),
    ]
