# Generated by Django 4.2.1 on 2024-03-21 17:58

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("places", "0006_alter_photo_place_alter_place_description_long_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="place",
            old_name="description_long",
            new_name="long_description",
        ),
        migrations.RenameField(
            model_name="place",
            old_name="description_short",
            new_name="short_description",
        ),
    ]
