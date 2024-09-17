from django.shortcuts import render, redirect   # Tambahkan import redirect di baris ini
from main.forms import ProductEntryForm
from main.models import ProductEntry
# Create your views here.
def show_main(request):
    product_entries = ProductEntry.objects.all()
    context = {
        'name': 'Daffa Desra Hastiar',
        'npm': '2306165490',
        'class': 'PBP C',
        'product_entries': product_entries
    }

    return render(request, "main.html", context)

def sell_product_entry(request):
    form = ProductEntryForm(request.POST or None)
    
    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')
    
    context = {'form': form}
    return render(request, "sell_product_entry.html", context)