# Generated by Django 3.1.7 on 2021-03-01 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Marks',
            fields=[
                ('name', models.CharField(max_length=30)),
                ('roll', models.IntegerField(primary_key=True, serialize=False)),
                ('chemistry', models.FloatField()),
                ('maths', models.FloatField()),
                ('physics', models.FloatField()),
            ],
        ),
    ]