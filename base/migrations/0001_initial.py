# Generated by Django 4.2.2 on 2023-06-14 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.TextField(max_length=100)),
                ('location', models.TextField(max_length=100)),
                ('name', models.TextField(max_length=100)),
                ('coordinates', models.IntegerField()),
            ],
        ),
    ]