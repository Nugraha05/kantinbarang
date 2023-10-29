from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import CartItem, Barang
from django.shortcuts import get_object_or_404

# Create your views here.
def makanan(request):
    searchMakanan = request.GET.get('nama')
    if searchMakanan:
        datas = Barang.objects.filter(nama__icontains=searchMakanan)
    else:
        datas = Barang.objects.all()
    return render(request, 'makanan.html', {'searchMakanan':searchMakanan, 'datas':datas})

def minuman(request):
    searchMinum = request.GET.get('nama')
    if searchMinum:
        datas = Barang.objects.filter(nama__icontains=searchMinum)
    else:
        datas = Barang.objects.all()
    return render(request, 'minuman.html', {'searchMinum':searchMinum, 'datas':datas})

def detail(request,data_id):
    data = get_object_or_404(Barang,pk=data_id)
    return render(request,'detail.html', {'data' : data})

def add_to_cart(request, data_id):
    data_id = int(data_id)
    barang = Barang.objects.get(pk=data_id)

    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))

        if quantity < 1:
            quantity = 1

        cart_item, created = CartItem.objects.get_or_create(barang=barang)

        if not created:
            cart_item.quantity += quantity
            cart_item.item_total = cart_item.quantity * barang.harga

            if quantity <= barang.stok:
                barang.stok -= quantity
                barang.save()
                cart_item.save()
            else:
                err = "error"
                return render(request,'error.html', {'err' : err, 'barang' : barang, 'quantity': quantity})
            
        else:
            cart_item.quantity = quantity
            cart_item.item_total = quantity * barang.harga

            if quantity <= barang.stok:
                barang.stok -= quantity
                barang.save()
                cart_item.save()
            else:
                err = "error"
                return render(request,'error.html', {'err' : err, 'barang' : barang, 'quantity': quantity})
            
    return redirect('pesanan')

def view_cart(request):
    cart_items = CartItem.objects.all()
    total_price = sum(item.item_total for item in cart_items)
    return render(request, 'pesanan.html', {'semua_barang': cart_items, 'total_harga': total_price})

def remove_from_cart(request, data_id):
    data_id = int(data_id)
    barang = Barang.objects.get(pk=data_id)
    try:
        cart_item = CartItem.objects.get(barang=barang)
        barang.stok += cart_item.quantity
        barang.save()
        cart_item.delete()
    except CartItem.DoesNotExist:
        pass
    return redirect('pesanan')