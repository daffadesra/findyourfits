from django.urls import path
from main.views import show_main, sell_product_entry

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('sell-product-entry', sell_product_entry, name='sell_product_entry'),

]

