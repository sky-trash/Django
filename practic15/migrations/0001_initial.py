# Generated by Django 5.1.1 on 2024-09-29 09:13

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('practic7', '0002_product_image'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.Auto(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_email', models.EmailField(max_length=254)),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('На рассмотрении', 'Pendindg'), ('В обработке', 'Processed'), ('Отправлен', 'Shipped'), ('Доставлен', 'Delivered')], max_length=50)),
                ('paid', models.BooleanField(default=False)),
                ('customer_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.Auto(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='practic15.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='practic7.product')),
            ],
        ),
    ]
