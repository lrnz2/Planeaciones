# Generated by Django 5.0 on 2023-12-17 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planeacion', '0002_rename__type_pedido_type_alter_pedido_producto_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='type',
            field=models.CharField(choices=[('Master', 'Master'), ('Piezas', 'Piezas'), ('Kg', 'Kilogramos')], max_length=15),
        ),
    ]