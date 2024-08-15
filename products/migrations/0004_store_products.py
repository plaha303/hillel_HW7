# Generated by Django 5.0.7 on 2024-08-15 16:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0003_store_inventory"),
    ]

    operations = [
        migrations.AddField(
            model_name="store",
            name="products",
            field=models.ManyToManyField(
                through="products.Inventory", to="products.product"
            ),
        ),
    ]
