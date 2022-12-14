# Generated by Django 4.1.1 on 2022-09-30 11:59

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code_name', models.CharField(max_length=125, verbose_name='Кодовое наименование марки автомобиля')),
            ],
            options={
                'verbose_name': 'Марки авто',
                'db_table': 'brands',
            },
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code_name', models.CharField(default='white', max_length=15, verbose_name='Кодовое наименование цвета')),
                ('hex_value', models.CharField(default='#ffffff', max_length=7, verbose_name='HEX-значение цвета #AABBCC')),
            ],
            options={
                'verbose_name': 'Цвета',
                'db_table': 'colors',
            },
        ),
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code_name', models.CharField(max_length=125, verbose_name='Кодовое наименование модели автомобиля')),
            ],
            options={
                'verbose_name': 'Модели авто',
                'db_table': 'models',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date(2022, 9, 30), verbose_name='Дата заказа')),
                ('amount', models.PositiveIntegerField(default=0, verbose_name='Кол-во')),
                ('brand', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cars.brand')),
                ('color', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cars.color')),
                ('model', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cars.model')),
            ],
            options={
                'verbose_name': 'Заказы',
                'db_table': 'orders',
            },
        ),
    ]
