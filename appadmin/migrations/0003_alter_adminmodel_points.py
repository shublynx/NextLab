# Generated by Django 4.2.2 on 2023-06-28 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("appadmin", "0002_adminmodel_apppic_adminmodel_points"),
    ]

    operations = [
        migrations.AlterField(
            model_name="adminmodel",
            name="points",
            field=models.CharField(max_length=10),
        ),
    ]
