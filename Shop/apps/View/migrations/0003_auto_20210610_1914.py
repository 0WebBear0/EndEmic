# Generated by Django 3.2.4 on 2021-06-10 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('View', '0002_alter_product_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='Description',
            field=models.CharField(default=' ', max_length=1000, verbose_name='Описание продукта'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=25, verbose_name='Название продукта'),
        ),
    ]
