# Generated by Django 4.2.1 on 2023-05-25 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("transactions", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="transaction",
            name="amount",
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name="transaction",
            name="time",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
