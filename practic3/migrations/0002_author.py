# Generated by Django 5.1.1 on 2024-09-11 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('practic3', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.Auto(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('date_of_birth', models.CharField(blank=True, max_length=10, null=True)),
                ('gender', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
    ]
