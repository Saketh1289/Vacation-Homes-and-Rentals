# Generated by Django 4.0.1 on 2024-09-11 12:33

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_invoice_total_alter_product_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoiceitem',
            name='item',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=models.SET(core.models.get_sentinel_product), to='core.product'),
        ),
    ]
