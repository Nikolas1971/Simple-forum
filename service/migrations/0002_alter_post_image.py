# Generated by Django 4.1.2 on 2022-10-06 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("service", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="image",
            field=models.ImageField(
                blank=True, null=True, upload_to="", verbose_name="Картинка"
            ),
        ),
    ]
