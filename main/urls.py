from django.urls import path
from main.views import show_main, sell_product_entry, show_xml, show_json, show_json_by_id, show_xml_by_id
from main.views import register, login_user, logout_user, edit_product, hapus_product, add_product_ajax
from main.views import create_product_flutter


app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('sell-product-entry', sell_product_entry, name='sell_product_entry'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('edit-product/<uuid:id>', edit_product, name='edit_product'),
    path('delete/<uuid:id>', hapus_product, name='hapus_product'),
    path('add-product-ajax/', add_product_ajax, name='add_product_ajax'),
    path('create-product-flutter/', create_product_flutter, name='create_product_flutter'),
]