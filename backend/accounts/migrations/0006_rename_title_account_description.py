# Generated by Django 4.2.1 on 2023-05-25 08:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0005_alter_account_balance"),
    ]

    operations = [
        migrations.RenameField(
            model_name="account",
            old_name="title",
            new_name="description",
        ),
    ]
