# Generated by Django 4.1.3 on 2023-10-29 06:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0019_barang_alter_cartitem_makanan_delete_makanan'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartitem',
            old_name='makanan',
            new_name='barang',
        ),
    ]
