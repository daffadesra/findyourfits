# **README**
Ini adalah repositori untuk tugas PBP 2025 milik Daffa Desra Hastiar (2306165490) dari kelas PBP C.

Link aplikasi PWS : http://daffa-desra-findyourfits.pbp.cs.ui.ac.id/

## **TUGAS 3**
### 1. Jelaskan mengapa kita memerlukan  _data delivery_  dalam pengimplementasian sebuah platform?
Menurut beberapa sumber yang saya baca, _data platform_ penting dalam pengimplementasian sebuah platform karena _data delivery_ memungkinkan platform untuk menjalankan fungsi-fungsi yang melibatkan komunikasi antara komponen maupun user.

**Contoh _data delivery_** antara komponen dengan user dalam konteks tugas kali ini adalah ketika user ingin melihat produk apa saja yang ada di _e-commerce_. Untuk menampilkan produk-produk tersebut ke user, maka platform melakukan **_data delivery_** misalnya dari suatu database produk ke program front-end yang nantinya akan ditampilkan ke user.  

Contoh fungsi lain dari **_data delivery_** dalam kehidupan kita sehari-hari adalah ketika kita melakukan _search_ pada suatu sosial media misalkan _Instagram_. Ketika kita melakukan _search_, maka platform akan berkomunikasi dan melakukan _data delivery_ untuk memunculkan informasi atau data yang dicari oleh user.

Kesimpulannya adalah bahwa **platform memerlukan komunikasi diantara komponen-komponennya untuk melakukan fungsi-fungsinya.** Contoh komunikasi tersebut misalnya  komunikasi antara database dengan program back-end suatu platform. Komunikasi tersebut dapat dilakukan dengan adanya **_data delivery_**. Dengan demikian, suatu platform tidak akan berguna jika kita tidak menerapkan _data delivery_ dalam platform tersebut.
### 2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
Dari beberapa sumber yang saya baca di internet, terdapat beberapa kelebihan dari JSON dibandingkan dengan XML yang menyebabkan JSON menjadi format data yang lebih populer dibanding dengan XML. Berikut adalah beberapa kelebihan JSON dibandingkan dengan XML:
+ JSON bisa menampung _value_ berupa Integer, String, List, dan Array secara langsung. Sementara untuk tipe data yang serupa, **XML memerlukan _parsing_** dari String ke tipe data yang diinginkan.
+ **JSON memiliki sintaks yang lebih pendek dibandingkan XML**, sehingga JSON memiliki ukuran yang lebih kecil dan dapat dibaca ataupun ditulis dengan lebih cepat dibandingkan dengan XML. 
+ **JSON memiliki sintaks yang lebih mmudah untuk dibaca dibandingkan dengan XML**
+ **JSON didukung secara langsung oleh bahasa JavaScript** sehingga lebih mudah untuk terintegrasi dengan aplikasi pada JavaScript dan API.
+ **JSON lebih mudah untuk diparsing dibandingkan dengan XML** sehingga lebih cepat dan efisien ketika dijalankan.

Kesimpulanya adalah bahwa JSON lebih cocok untuk digunakan sebagai format data dalam pengembangan suatu website ataupun aplikasi karena JSON memiliki kecepatan dan efisiensi yang lebih baik dibandingkan dengan XML. Selain itu, JSON juga didukung langsung oleh JavaScript sehingga operasi-operasi dalam data JSON dapat dilakukan dengan lebih efisien dibandingkan dengan menggunakan XML yang harus diparsing terlebih dahulu. 
Dikarenakan dalam penggunaan web dan aplikasi banyak terjadi _data delivery_, maka saya memilih **JSON** sebagai format data yang **lebih baik** dibandingkan XML karena **JSON memakan ruang penyimpanan yang lebih kecil, dapat dijalankan dengan lebih efisien dan lebih mudah untuk dibaca dibandingkan dengan XML.**
### 3. Jelaskan fungsi dari method  `is_valid()`  pada form Django dan mengapa kita membutuhkan method tersebut?
Fungsi method `is_valid()` adalah untuk melakukan validasi pada _forms_ sehingga data yang dimasukkan memenuhi kriteria yang sudah ditentukan dalam _form fields_. 

Method `is_valid()` mengecek apakah data yang dimasukkan sudah sesuai dengan aturan-aturan yang kita tuliskan pada _form fields_, misalnya seperti **field mana saja yang harus diisi, tipe data apa yang digunakan pada suatu variabel, dan aturan validasi lainnya seperti nilai maksimum atau panjang string minimum.**  

Jika data valid, maka method `is_valid()` 
mereturn `True` dan akan mengisi dictionary `cleaned_data` yang berisi data yang sudah divalidasi dan dikonversi ke tipe data yang sesuai. 

Jika data tidak valid, maka method `is_valid()`  akan mereturn `False` dan kesalahan validasi tersebut akan disimpan dalam atribut `form.errors` sehingga kita bisa melihat kesalahan apa yang terjadi pada data yang tidak valid tersebut.

Menurut saya, method `is_valid()` dibutuhkan karena method tersebut dapat mencegah program untuk memasukkan data yang tidak benar sehingga error-error yang diakibatkan oleh kesalahan input dalam database dapat dihindari. Selain itu, method `is_valid()` juga dapat memastikan bahwa semua nilai dalam data yang kita miliki memang sudah benar dan siap untuk diproses oleh program selanjutnya.
### 4. Mengapa kita membutuhkan  `csrf_token`  saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan  `csrf_token`  pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
`csrf_token` adalah **random token yang berfungsi untuk mencegah _Cross-Site Request Forgery Attack_**. Adanya `csrf_token` menambah proteksi terhadap forms yang disubmit oleh user agar tidak dieksploitasi oleh penyerang melalui serangan CSRF.

Kode `{% csrf_token %}`ketika kita membuat suatu form, maka program akan membuat suatu _field_ tersembunyi yang memuat suatu token yang sulit untuk ditebak. Ketika form tersebut di-_submit_, maka Django akan memeriksa apakah token yang ada dalam form sesuai dengan yang tersimpan pada sesi user. Jika token tersebut match, maka request user akan dilanjutkan atau diterima.

Jika kita tidak menggunakan `csrf_token` pada forms yang kita buat, maka seorang _hacker_ bisa saja mengeksploitasi celah tersebut dengan melakukan  _Cross-Site Request Forgery (CSRF) Attack_. CSRF terjadi ketika seorang user _logged in_ ke website Django yang kita buat. _Hacker_ nantinya akan mengirimkan link website yang jika di klik oleh user, maka link tersebut akan mengirimkan request (seperti request untuk ganti password atau melakukan transfer uang) ke website Django kita tanpa interaksi dan tanpa sepengetahuan user. Karena user sudah terautentikasi dengan website Django kita, maka request yang dikirim oleh _hacker_ tersebut akan di-_treat_ seakan request tersebut dikirim oleh user. Tanpa adanya `csrf_token`, maka Django tidak akan tahu apakah request tersebut datang dari user atau bukan. Dengan demikian, request tersebut diteruskan sehingga terjadilah CSRF Attack.

### 5. Jelaskan bagaimana cara kamu mengimplementasikan  _checklist_  di atas secara  _step-by-step_  (bukan hanya sekadar mengikuti tutorial)
**Step 1: Implementasi skeleton sebagai Kerangka Views**
1. Pertama-tama, saya membuat implementasi skeleton sebagai kerangka _views_. Langkah ini saya lakukan dengan membuat direktori _templates_ pada _root folder_ yang kemudian saya isi dengan berkas _base.html_ berisikan berikut:
	```
	{% load static %}  
	<!DOCTYPE  html>  
	<html  lang="en">  
		<head>  
			<meta  charset="UTF-8"  />  
			<meta  name="viewport"  content="width=device-width, initial-scale=1.0"  />  
			{% block meta %} {% endblock meta %}  
		</head>  
	  
		<body>  
			Z{% block content %} {% endblock content %}  
		</body>  
	</html>
	```
	`_base.html` berfungsi untuk memuat data secara dinamis dari Django ke HTML. Nantinya `{% block %}` akan diisi oleh konten berdasarkan template turunan.
2. Kedua, saya mengubah file `settings.py` yang ada pada direktori proyek saya yaitu `findyourfits`. Ubahan yang saya lakukan adalah pada variabel `TEMPLATES` yang ditambahkan sehingga menjadi seperti berikut:
	```
	TEMPLATES =  [  
		{  
			'BACKEND':  'django.template.backends.django.DjangoTemplates',  
			'DIRS':  [BASE_DIR /  'templates'],  # Tambahkan konten baris ini  
			'APP_DIRS':  True,  
			...  
		}  
	]
	```
	Bagian pada kode ini bertujuan untuk menjadikan `base.html` pada direktori `templates` terdeteksi sebagai berkas template.
3. Ketiga, saya menambahkan potongan kode berikut pada bagian atas dari `main.html`:
	```
	{% extends 'base.html' %}  
	{% block content %}
	...
	```
	Bagian kode ini bertujuan agar `main.html` menggunakan `base.html` sebagai _template_ utama.

**Step 2 : Mengubah Primary Key menjadi UUID**
Langkah ini dilakukan untuk mengubah ID yang sebelumnya berupa integer dan selalu dimulai dari 1 dan di-_increment_, menjadi suatu ID yang digenerate oleh Django. Berikut adalah langkah-langkah yang saya lakukan untuk menerapkan step ini:
1. Pertama-tama, saya membuka `models.py` yang terletak pada subdirektori `main`. Kemudian saya mengimport library `uuid` dan menambahkan variabel `id` sehingga kode pada `models.py` menjadi seperti berikut:
```
import  uuid
from  django.db  import  models

class  ProductEntry(models.Model):
	id  =  models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) # tambahkan baris ini
	name  =  models.CharField(max_length=200)
	price  =  models.IntegerField()
	stock  =  models.IntegerField() # tambahan
	condition  =  models.TextField() # used or new
	description  =  models.TextField() # tambahan
```

2.  Kemudian saya melakukan migration untuk menyimpan perubahan pada `models.py` dengan menjalankan kode berikut:
	```
	python3 manage.py makemigrations  
	python3 manage.py migrate
	```
**Step 3: Membuat Form Input Data dan Menampilkan Produk yang dijual pada HTML**
Pada langkah ini, saya membuat _form_ yang digunakan sebagai input data berisikan produk yang ingin dijual beserta atribut-atributnya yaitu nama produk, harga, stok, kondisi, dan deskripsi produk. Nantinya data produk yang saya masukkan dalam _form_ akan ditampilkan pada halaman utama **findyourfits**. Berikut adalah cara saya mengimplementasikan step ini:
3. Pertama-tama, saya menambahkan file `forms.py` pada direktori `main` yang berfungsi untuk membuat struktur _form_ yang digunakan untuk menerima data produk baru. Berikut adalah kode pada `forms.py`:
	```
	from  django.forms  import  ModelForm
	from  main.models  import  ProductEntry

	class  ProductEntryForm(ModelForm):
		class  Meta:
			model  =  ProductEntry
			fields  = ["name", "price", "stock", "condition", "description"]
	```
4. Kedua, saya menambahkan kode `views.py` pada direktori main dengan mengimport class yang ada dalam `forms.py` yaitu `ProductEntryForm` dan class yang ada dalam `models.py` yaitu `ProductEntry` seperti berikut:
	```
	from  django.shortcuts  import  render, redirect
	from  main.forms  import  ProductEntryForm
	from  main.models  import  ProductEntry
	```
5. Ketiga, saya membuat fungsi bernama `sell_product_entry` pada `views.py`yang menerima parameter `request`. Fungsi ini bertujuan untuk membuat _form_ yang dapat menambahkan data produk ke list produk yang tersedia. Berikut adalah isi dari fungsi `sell_product_entry`:
```
def  sell_product_entry(request):
	form  =  ProductEntryForm(request.POST or  None)
	if  form.is_valid() and  request.method ==  "POST":
		form.save()
		return  redirect('main:show_main')
	context  = {'form': form}
	return  render(request, "sell_product_entry.html", context)
```
6. Keempat, saya mengubah fungsi `show_main` yang terletak pada `views.py` dengan variabel `product_entries` yang berguna untuk mengambil seluruh objek `ProductEntry` yang tersimpan dalam database. Kemudian saya menambahkan variabel `product_entries` ke dalam`context`.
7. Kelima, saya membuka file `urls.py` pada direktori maindan mengimport fungsi `sell_product_entry` dan menambahkan `urlpatterns` yaitu `sell-product-entry`untuk mengakses fungsi yang sudah di-_import_. 
8. Keenam, saya membuat berkas HTML baru dengan nama `sell_product_entry.html` pada direktori `main/templates`. Berkas HTML tersebut berguna untuk menampilkan form yang bisa digunakan user untuk menambahkan produk yang ingin dijual.
9. Terakhir, saya menambahkan kode pada `main.html` yang akan menampilkan tombol `Jual Produk` dan menampilkan tabel berisi produk apa saja yang sudah ada di dalam _database_ beserta atribut-atributnya seperti nama produk, harga, stok, kondisi, dan deskripsi.
> Setelah menyelesaikan ketiga step ini, maka checklist pertama yaitu membuat input form untuk menambahkan objek sudah selesai dan bisa dijalankan.
>
**Step 4: Membuat Fungsi untuk Mengembalikan Data dalam Bentuk XML, JSON, XML by ID, dan JSON by ID beserta routing URL untuk masing-masing fungsi.**
10. Pertama-tama, saya membuka berkas `views.py` dan melakukan import modul `HttpResponse` dan `Serializer` pada bagian atas seperti berikut: 
	```
	from django.http import HttpResponse  
	from django.core import serializers
	``` 
 2. Kedua, saya membuat fungsi `show_xml`, `show_json`, `show_xml_by_id`, dan `show_json_by_id` yang keduanya menerima parameter `request` dan menambahkan variabel `data` yang berfungsi untuk menyimpan hasil _query_ dari seluruh data yang ada pada `ProductEntry`. Untuk fungsi `show_xml_by_id` dan `show_json_by_id`, hasil _query_ yang disimpan adalah objek data dengan ID yang diminta oleh user.
 3. Ketiga, saya menambahkan _return function_ berupa `HttpResponse` yang berisi parameter dari hasil _query_ yang sudah diserialisasi menjadi XML atau JSON. Berikut adalah kode dari keempat function:
	```
	def  show_xml(request):
		data  =  ProductEntry.objects.all()
		return  HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
	def  show_json(request):
		data  =  ProductEntry.objects.all()
		return  HttpResponse(serializers.serialize("json", data), content_type="application/json")
	def  show_xml_by_id(request, id):
		data  =  ProductEntry.objects.filter(pk=id)
		return  HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
	def  show_json_by_id(request, id):
		data  =  ProductEntry.objects.filter(pk=id)
		return  HttpResponse(serializers.serialize("json", data), content_type="application/json")
	```
 4. Keempat, saya membuka `urls.py` pada direktori `main` dan meng-_import_ keempat fungsi yang saya buat pada langkah sebelumnya.
 5. Terakhir, saya menambahkan 4 buah _path_ URL ke dalam variabel `urlpatterns` pada `urls.py` yang berfungsi untuk mengakses fungsi yang sudah saya import tadi. Tambahan kodenya adalah sebagai berikut:
	 ```
	 urlpatterns = [
		...
		path('xml/', show_xml, name='show_xml'),
		path('json/', show_json, name='show_json'),
		path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
		path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
	]
	 ```
> Setelah menjalankan langkah ini, maka checklist kedua dan ketiga yaitu membuat views beserta routing URL untuk melihat objek yang sudah ditambahkan dalam format XML, JSON, XML by ID, dan JSON by ID.

**Dokumentasi Postman**
11. XML
<img width="1797" alt="image" src="https://github.com/user-attachments/assets/b9d0d02f-8a6b-4ea0-9b91-4ee08975473b"> 
12. JSON
<img width="1795" alt="image" src="https://github.com/user-attachments/assets/e6a0ec41-ec40-4212-9d37-530f23fab771">
13. XML by ID
<img width="1799" alt="image" src="https://github.com/user-attachments/assets/d6a2a68a-5316-4cc1-82a4-5f7c34e85d92">
14. JSON by ID 
<img width="1795" alt="image" src="https://github.com/user-attachments/assets/3f6411f9-3117-47db-9417-91d78a4e4786">