# Generated by Django 4.1 on 2023-05-10 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("chatbot", "0005_raised_questions"),
    ]

    operations = [
        migrations.AlterField(
            model_name="raised_questions",
            name="que",
            field=models.CharField(max_length=1000, unique=True),
        ),
    ]