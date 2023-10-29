# Generated by Django 4.1.3 on 2023-10-28 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_tes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='toko',
            name='listmakanan',
        ),
        migrations.RemoveField(
            model_name='toko',
            name='listminuman',
        ),
        migrations.AddField(
            model_name='makanan',
            name='stock',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='minuman',
            name='stock',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Tes',
        ),
        migrations.DeleteModel(
            name='Toko',
        ),
    ]
