# Generated by Django 5.1.1 on 2024-09-16 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('practic7', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(null=True, upload_to='book/%Y/%m/%d'),
        ),
    ]
