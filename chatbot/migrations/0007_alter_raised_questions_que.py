# Generated by Django 4.1 on 2023-05-10 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("chatbot", "0006_alter_raised_questions_que"),
    ]

    operations = [
        migrations.AlterField(
            model_name="raised_questions",
            name="que",
            field=models.CharField(max_length=1000),
        ),
    ]
