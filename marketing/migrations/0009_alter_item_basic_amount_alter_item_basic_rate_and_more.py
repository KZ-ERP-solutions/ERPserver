# Generated by Django 4.1.7 on 2023-03-26 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0008_alter_marketing_delivery_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='basic_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='item',
            name='basic_rate',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='item',
            name='dp',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='item',
            name='gross_weight_per_unit',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='item',
            name='is_std',
            field=models.BooleanField(blank=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='item',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='item',
            name='model',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='item',
            name='net_weight_per_unit',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='item',
            name='quantity',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='rating',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='item',
            name='serial_nos',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='item',
            name='si_no',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='total_weight',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='item',
            name='unit',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='item',
            name='wo_nos',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
