# Generated by Django 4.1.3 on 2023-10-28 13:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_minuman_rename_tes_makanan_toko'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=250)),
                ('gambar', models.ImageField(upload_to='movie/images/')),
                ('listmakanan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.makanan')),
                ('listminuman', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.minuman')),
            ],
        ),
    ]
