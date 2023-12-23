# Generated by Django 5.0 on 2023-12-23 14:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("kitchen", "0004_alter_cook_years_of_experience"),
    ]

    operations = [
        migrations.AlterField(
            model_name="dish",
            name="description",
            field=models.TextField(unique=True),
        ),
        migrations.AlterField(
            model_name="dish",
            name="name",
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name="dishtype",
            name="name",
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name="ingredient",
            name="name",
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
