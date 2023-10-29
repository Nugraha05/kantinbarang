from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Kantin(models.Model):
    nama = models.CharField(max_length=250)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="min 8 digit")
    telpon = models.CharField(validators=[phone_regex], max_length=15, blank=True)
    def __str__(self) -> str:
        return self.nama
    
class Barang(models.Model):
    nama = models.CharField(max_length=250)
    harga = models.IntegerField()
    gambar = models.ImageField(upload_to = 'images/')
    stok = models.IntegerField()
    kantin = models.ForeignKey(Kantin, on_delete = models.CASCADE)

    type = (
        (1, 'Makanan'),
        (0, 'Minuman')
    )
    type = models.IntegerField(max_length=1, choices=type)

    tersedia = (
        (1, 'Tersedia'),
        (0, 'Tidak tersedia')
    )
    tersedia = models.IntegerField(max_length=1, choices=tersedia)

    def __str__(self) -> str:
        return self.nama
    
class CartItem(models.Model):
    barang = models.ForeignKey(Barang, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    item_total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)