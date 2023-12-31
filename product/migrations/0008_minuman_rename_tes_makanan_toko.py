# Generated by Django 4.1.3 on 2023-10-28 13:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_rename_makanan_tes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Minuman',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=250)),
                ('harga', models.IntegerField()),
            ],
        ),
        migrations.RenameModel(
            old_name='Tes',
            new_name='Makanan',
        ),
        migrations.CreateModel(
            name='Toko',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=250)),
                ('gambar', models.ImageField(upload_to='movie/images/')),
                ('listmakanan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.makanan')),
                ('listminuman', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.minuman')),
            ],
        ),
    ]
