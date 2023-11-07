# Generated by Django 4.2.5 on 2023-11-07 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livraria', '0014_compra_tipo_pagamento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compra',
            name='tipo_pagamento',
            field=models.IntegerField(choices=[(1, 'Cartão de Crédito'), (2, 'Cartão de Débito'), (3, 'PIX'), (4, 'Boleto'), (5, 'Transferência Bancária'), (6, 'Dinheiro'), (7, 'Outro')], default=1),
        ),
    ]