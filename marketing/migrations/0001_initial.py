# Generated by Django 4.1.7 on 2023-03-11 07:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Marketing',
            fields=[
                ('no', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('customer', models.CharField(max_length=100)),
                ('po_no', models.CharField(max_length=100)),
                ('po_date', models.DateField()),
                ('marketing_item', models.CharField(max_length=100)),
                ('consignee_tel_no', models.CharField(max_length=100)),
                ('buyer_tel_no', models.CharField(max_length=100)),
                ('payment_terms', models.CharField(max_length=100)),
                ('paying_authority', models.CharField(max_length=100)),
                ('penalty_clause', models.CharField(max_length=100)),
                ('insurance', models.CharField(max_length=100)),
                ('delivery_date', models.DateField()),
                ('delivery_place', models.CharField(max_length=100)),
                ('freight', models.CharField(max_length=100)),
                ('mode_of_despatch', models.CharField(max_length=100)),
                ('inspection', models.CharField(max_length=100)),
                ('special_instruction', models.CharField(max_length=100)),
                ('despatch_additional_info', models.CharField(max_length=100)),
                ('note', models.CharField(max_length=100)),
                ('remarks', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'marketing',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('si_no', models.IntegerField()),
                ('is_std', models.BooleanField()),
                ('item', models.CharField(max_length=100)),
                ('rating', models.CharField(max_length=100)),
                ('quantity', models.IntegerField()),
                ('unit', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('wo_nos', models.CharField(max_length=100)),
                ('basic_rate', models.DecimalField(decimal_places=2, max_digits=10)),
                ('basic_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('dp', models.DecimalField(decimal_places=2, max_digits=10)),
                ('net_weight_per_unit', models.DecimalField(decimal_places=2, max_digits=10)),
                ('gross_weight_per_unit', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total_weight', models.DecimalField(decimal_places=2, max_digits=10)),
                ('serial_nos', models.CharField(max_length=100)),
                ('item_group', models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, related_name='item_order', to='marketing.marketing')),
            ],
            options={
                'db_table': 'item',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='addresss',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('org', models.CharField(blank=True, max_length=255)),
                ('addr_line1', models.CharField(blank=True, max_length=255)),
                ('addr_line2', models.CharField(blank=True, max_length=255)),
                ('addr_line3', models.CharField(blank=True, max_length=255)),
                ('pin', models.CharField(blank=True, max_length=10)),
                ('phone_no', models.CharField(blank=True, max_length=15)),
                ('gst_no', models.CharField(blank=True, max_length=15)),
                ('type', models.CharField(blank=True, max_length=255)),
                ('group', models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, related_name='addrees', to='marketing.marketing')),
            ],
            options={
                'db_table': 'addresss',
                'managed': True,
            },
        ),
    ]
