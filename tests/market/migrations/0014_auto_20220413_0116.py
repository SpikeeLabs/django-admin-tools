# Generated by Django 3.1.7 on 2022-04-13 01:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("market", "0013_auto_20210702_0041"),
    ]

    operations = [
        migrations.AlterField(
            model_name="shoppingmall",
            name="general_manager",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="market.generalmanager",
                verbose_name="manager",
            ),
        ),
    ]