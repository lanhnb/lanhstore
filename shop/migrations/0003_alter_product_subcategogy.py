# Generated by Django 3.2.6 on 2021-10-12 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_alter_product_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='subcategogy',
            field=models.TextField(),
        ),
    ]
