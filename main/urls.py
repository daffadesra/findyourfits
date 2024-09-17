from django.urls import path
from main.views import show_main, sell_product_entry, show_xml, show_json

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('sell-product-entry', sell_product_entry, name='sell_product_entry'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
]

