# Generated by Django 5.0 on 2024-05-06 15:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("gifts_app", "0002_remove_gift_links_link_gift_alter_gift_bought"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="gift",
            name="bought",
        ),
        migrations.RemoveField(
            model_name="gift",
            name="visible_to",
        ),
        migrations.AlterField(
            model_name="link",
            name="url",
            field=models.URLField(blank=True, max_length=400),
        ),
    ]
