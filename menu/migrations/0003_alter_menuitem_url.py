# Generated by Django 5.0.4 on 2024-04-11 17:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("menu", "0002_alter_menuitem_parent"),
    ]

    operations = [
        migrations.AlterField(
            model_name="menuitem",
            name="url",
            field=models.CharField(max_length=255),
        ),
    ]
