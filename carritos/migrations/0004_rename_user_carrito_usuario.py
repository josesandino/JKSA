# Generated by Django 3.2.4 on 2021-07-06 04:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carritos', '0003_rename_usuario_carrito_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carrito',
            old_name='user',
            new_name='usuario',
        ),
    ]