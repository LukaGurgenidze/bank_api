# Generated by Django 4.2.1 on 2023-05-25 09:01

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0006_rename_title_account_description"),
    ]

    operations = [
        migrations.CreateModel(
            name="Transaction",
            fields=[
                ("account_id", models.CharField(default="", max_length=100)),
                ("time", models.DateTimeField()),
                (
                    "transaction_id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
            ],
            options={
                "ordering": ["time"],
            },
        ),
        migrations.DeleteModel(
            name="AccountHistory",
        ),
        migrations.AlterField(
            model_name="account",
            name="transaction_history",
            field=models.ManyToManyField(blank=True, to="accounts.transaction"),
        ),
    ]
