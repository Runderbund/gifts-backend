# Generated by Django 5.0 on 2024-05-09 19:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("gifts_app", "0005_remove_member_show_bought"),
    ]

    operations = [
        migrations.AddField(
            model_name="gift",
            name="bought",
            field=models.CharField(blank="not bought", max_length=1000),
        ),
        migrations.AddField(
            model_name="gift",
            name="notes_other",
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]
