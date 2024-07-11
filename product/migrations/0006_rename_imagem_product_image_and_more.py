# Generated by Django 5.0.6 on 2024-07-11 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_alter_product_descricao_curta_alter_product_tipo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='imagem',
            new_name='image',
        ),
        migrations.RemoveField(
            model_name='product',
            name='descricao_curta',
        ),
        migrations.RemoveField(
            model_name='product',
            name='descricao_longa',
        ),
        migrations.RemoveField(
            model_name='product',
            name='nome',
        ),
        migrations.RemoveField(
            model_name='product',
            name='preco_marketing',
        ),
        migrations.RemoveField(
            model_name='product',
            name='preco_marketing_promocional',
        ),
        migrations.RemoveField(
            model_name='product',
            name='tipo',
        ),
        migrations.AddField(
            model_name='product',
            name='long_description',
            field=models.TextField(default='', verbose_name='Descrição Longa'),
        ),
        migrations.AddField(
            model_name='product',
            name='name',
            field=models.CharField(default='', max_length=120, verbose_name='nome'),
        ),
        migrations.AddField(
            model_name='product',
            name='price_marketing',
            field=models.FloatField(default=0, verbose_name='Preço Marketing'),
        ),
        migrations.AddField(
            model_name='product',
            name='promotion_price_marketing',
            field=models.FloatField(default=0, verbose_name='Preço Marketing Promocional'),
        ),
        migrations.AddField(
            model_name='product',
            name='short_description',
            field=models.TextField(default='', max_length=255, verbose_name='Descrição Curta'),
        ),
        migrations.AddField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('V', 'Variável'), ('S', 'Simples')], default='V', max_length=1, verbose_name='Tipo'),
        ),
    ]
