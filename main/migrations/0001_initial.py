# Generated by Django 3.0.8 on 2020-07-09 15:19

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
                ('product_name', models.CharField(max_length=150)),
                ('product_type', models.CharField(max_length=25)),
                ('product_description', models.TextField()),
                ('product_price', models.IntegerField()),
            ],
        ),
    ]
