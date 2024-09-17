from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core import serializers
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

def show_xml(request):
    data = ProductEntry.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = ProductEntry.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
    
