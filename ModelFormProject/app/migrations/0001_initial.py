# Generated by Django 4.2.11 on 2024-05-07 05:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Topic",
            fields=[
                (
                    "title",
                    models.CharField(max_length=50, primary_key=True, serialize=False),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Website",
            fields=[
                (
                    "name",
                    models.CharField(max_length=50, primary_key=True, serialize=False),
                ),
                ("url", models.URLField()),
                ("email", models.EmailField(max_length=254)),
                (
                    "title",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.topic"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Access",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateField()),
                ("author", models.CharField(max_length=50)),
                (
                    "name",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.website"
                    ),
                ),
            ],
        ),
    ]
