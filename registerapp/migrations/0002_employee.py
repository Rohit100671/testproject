# Generated by Django 5.1.2 on 2024-10-21 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registerapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('eid', models.IntegerField(primary_key=True, serialize=False)),
                ('ename', models.CharField(max_length=30)),
                ('esalary', models.IntegerField()),
                ('emono', models.IntegerField()),
            ],
        ),
    ]
