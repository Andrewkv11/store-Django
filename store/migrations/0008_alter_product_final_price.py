# Generated by Django 4.1.4 on 2022-12-10 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_product_final_price_alter_product_cat_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='final_price',
            field=models.PositiveIntegerField(verbose_name='fin_price $'),
        ),
    ]