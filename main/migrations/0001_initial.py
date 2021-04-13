# Generated by Django 3.1.7 on 2021-04-11 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название товара')),
                ('product_image', models.ImageField(blank=True, upload_to='images')),
                ('description', models.CharField(max_length=200, verbose_name='Описание товара')),
            ],
        ),
    ]