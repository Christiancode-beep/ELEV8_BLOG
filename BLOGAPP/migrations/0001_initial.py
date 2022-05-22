# Generated by Django 4.0.4 on 2022-05-14 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=400)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('body', models.TextField()),
            ],
        ),
    ]
