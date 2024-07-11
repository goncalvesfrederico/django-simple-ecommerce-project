# Generated by Django 5.0.6 on 2024-07-11 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_rename_imagem_product_image_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='variation',
            old_name='nome',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='variation',
            old_name='preco',
            new_name='price',
        ),
        migrations.RenameField(
            model_name='variation',
            old_name='preco_promocional',
            new_name='promocion_price',
        ),
        migrations.RenameField(
            model_name='variation',
            old_name='estoque',
            new_name='stock',
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default='', upload_to='product_image/%Y/%m/', verbose_name='Imagem'),
        ),
    ]
