# Generated by Django 4.1.3 on 2023-10-28 16:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0015_cartitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='Minuman',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=250)),
                ('harga', models.IntegerField()),
                ('gambar', models.ImageField(upload_to='images/')),
                ('stok', models.IntegerField()),
                ('TERSEDIA', models.CharField(choices=[('1', 'Tersedia'), ('0', 'Tidak tersedia')], max_length=1)),
                ('kantin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.kantin')),
            ],
        ),
    ]