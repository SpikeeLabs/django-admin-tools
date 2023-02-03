# Generated by Django 3.2.5 on 2021-07-02 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("market", "0012_auto_20210326_0240"),
    ]

    operations = [
        migrations.AlterField(
            model_name="itemsale",
            name="total",
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name="shoppingmall",
            name="shops",
            field=models.ManyToManyField(blank=True, to="market.Shop"),
        ),
        migrations.AlterField(
            model_name="transaction",
            name="total",
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
    ]