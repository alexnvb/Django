# Generated by Django 3.0.7 on 2020-06-27 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('title', models.TextField()),
                ('text', models.TextField()),
            ],
        ),
    ]
