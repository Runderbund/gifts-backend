# Generated by Django 5.0 on 2024-04-26 17:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("gifts_app", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="gift",
            name="links",
        ),
        migrations.AddField(
            model_name="link",
            name="gift",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="links",
                to="gifts_app.gift",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="gift",
            name="bought",
            field=models.BooleanField(default=True),
        ),
    ]
