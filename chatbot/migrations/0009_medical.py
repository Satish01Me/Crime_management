# Generated by Django 4.2 on 2023-05-10 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0008_education'),
    ]

    operations = [
        migrations.CreateModel(
            name='medical',
            fields=[
                ('SNo', models.AutoField(primary_key=True, serialize=False)),
                ('que', models.CharField(max_length=1000)),
                ('dept', models.CharField(max_length=100)),
            ],
        ),
    ]
