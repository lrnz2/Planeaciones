# Generated by Django 5.0 on 2023-12-18 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planeacion', '0003_alter_pedido_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Planeacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clave', models.CharField(max_length=15)),
                ('status', models.CharField(choices=[('Pendiente', 'Pendiente'), ('En proceso', 'En proceso'), ('Entregado', 'Entregado')], max_length=15)),
            ],
        ),
    ]