from django.forms import ModelForm
from main.models import ProductEntry

class ProductEntryForm(ModelForm):
    class Meta:
        model = ProductEntry
        fields = ["name", "price", "stock", "condition", "description"]
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Styling untuk semua field
        common_styles = 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-cyan-500 focus:border-transparent'
        
        # ubah class dan placeholder untuk setiap field
        self.fields['name'].widget.attrs.update({
            'class': common_styles,
            'placeholder': 'Masukkan nama produk'
        })
        self.fields['price'].widget.attrs.update({
            'class': common_styles,
            'placeholder': 'Masukkan harga produk'
        })
        self.fields['stock'].widget.attrs.update({
            'class': common_styles,
            'placeholder': 'Masukkan stok produk'
        })
        self.fields['condition'].widget.attrs.update({
            'class': common_styles,
            'placeholder': 'Masukkan kondisi produk'
        })  
        self.fields['description'].widget.attrs.update({
            'class': common_styles,
            'placeholder': 'Masukkan deskripsi produk',
            'rows': '4'
        })