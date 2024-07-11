# Generated by Django 5.0.6 on 2024-07-11 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_rename_variacao_variation_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='descricao_curta',
            field=models.TextField(max_length=255),
        ),
        migrations.AlterField(
            model_name='product',
            name='tipo',
            field=models.CharField(choices=[('V', 'Variavél'), ('S', 'Simples')], default='V', max_length=1),
        ),
    ]
