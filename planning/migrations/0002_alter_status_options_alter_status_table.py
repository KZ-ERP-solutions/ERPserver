# Generated by Django 4.1.7 on 2023-03-16 09:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('planning', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='status',
            options={'managed': True},
        ),
        migrations.AlterModelTable(
            name='status',
            table='Status',
        ),
    ]