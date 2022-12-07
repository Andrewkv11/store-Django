# Generated by Django 4.1.4 on 2022-12-07 17:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_manufacturer_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='cat',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='store.product_category'),
        ),
        migrations.AddField(
            model_name='product',
            name='mnf',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='store.manufacturer'),
        ),
    ]
