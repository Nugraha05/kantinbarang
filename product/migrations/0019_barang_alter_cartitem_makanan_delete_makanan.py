# Generated by Django 4.1.3 on 2023-10-29 06:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0018_rename_type_makanan_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Barang',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=250)),
                ('harga', models.IntegerField()),
                ('gambar', models.ImageField(upload_to='images/')),
                ('stok', models.IntegerField()),
                ('type', models.CharField(choices=[('1', 'Makanan'), ('0', 'Minuman')], max_length=1)),
                ('tersedia', models.CharField(choices=[('1', 'Tersedia'), ('0', 'Tidak tersedia')], max_length=1)),
                ('kantin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.kantin')),
            ],
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='makanan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.barang'),
        ),
        migrations.DeleteModel(
            name='Makanan',
        ),
    ]
