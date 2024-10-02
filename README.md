# **README**
Ini adalah repositori untuk tugas PBP 2025 milik Daffa Desra Hastiar (2306165490) dari kelas PBP C.

Link aplikasi PWS : http://daffa-desra-findyourfits.pbp.cs.ui.ac.id/
## **TUGAS 2**
### 1) Jelaskan bagaimana cara kamu mengimplementasikan _checklist_ di atas secara _step-by-step_ (bukan hanya sekadar mengikuti tutorial)
1. **Pertama-tama, saya membuat folder lokal baru di laptop dengan nama `findyourfits`**. Setelah itu, saya membuat direktori lokal dengan nama yang sama yang kemudian saya inisiasi dengan Git. Di dalam folder tersebut, saya menambahkan file README.md pertama saya yang berisi identitas diri saya. 
2. **Kedua, saya membuat repositori Github baru bernama "findyourfits" pada akun Github saya.** Pada langkah ini, saya membuat branch utama saya yang saya namakan "main". Kemudian, saya menjalankan perintah `git remote add origin <URL_REPO_SAYA>` untuk menghubungkan repositori lokal saya dengan repositori di Github. Kemudian saya melakukan `add`,`commit`, dan `push` ke repositori saya untuk pertama kalinya.
3. **Ketiga, saya menginisiasi dan mengaktifkan _Virtual Enviroment_ pada folder `findyourfits` **. 
4. **Keempat, saya membuat berkas `requirements.txt` di dalam folder `findyourfits` yang berisi:
	```
	django  
	gunicorn  
	whitenoise  
	psycopg2-binary  
	requests  
	urllib3
	```
	yang kemudian saya install menggunakan command `pip install -r requirements.txt`. Setelah itu, saya membuat proyek baru dengan nama `findyourfits` dengan command:
	`django-admin startproject findyourfits .`
5. **Kelima, saya membuat berkas `.gitignore` dengan isi yang sesuai pada Tutorial 0.** Setelah itu, saya melakukan Git `add`, `commit`, dan `push` ke repositori Github `findyourfits`.
6. **Keenam, saya melakukan konfigurasi untuk project `findyourfits` pada Pacil Web Service (PWS)**. Pada langkah ini, saya menambahkan project `findyourfits` melalui website **Pacil Web Service (PWS)**. Setelah itu, saya menambahkan `ALLOWED_HOSTS` pada `settings.py` di proyek Django `findyourfits` seperti berikut:
`ALLOWED_HOSTS  = ["localhost", "127.0.0.1", "daffa-desra-findyourfits.pbp.cs.ui.ac.id"]`
Kemudian, saya mengubah nama branch utama menjadi `main` dengan perintah `git branch -M main`. Setelah itu, saya melakukan push ke repositori Github dan PWS.
7. **Ketujuh, saya membuat aplikasi `main` pada proyek `findyourfits`**. Kemudian, saya mendaftarkan aplikasi main ke dalam proyek `findmyfits` dengan cara menambahkan `main` pada berkas `settings.py` seperti berikut:
	```
	INSTALLED_APPS =  [  
	...,  
	'main'  
	]
	```
8. **Kedelapan, saya menambahkan berkas `main.html` ke dalam direktori baru bernama `templates` pada direktori aplikasi `main`**. Berikut adalah file `main.html` yang saya buat:
	```
	<h1>FindYourFits</h1>
	
	<h3>Nama Aplikasi </h3>
	<p>{{ app_name }}</p>
	<h3>Nama </h3>
	<p>{{ name }}</p>
	<h3>NPM </h3>
	<p>{{ name }}</p>
	<h3>Kelas </h3>
	<p>{{ class }}</p>
	```
9. **Kesembilan, menambahkan model `Product` ke dalam aplikasi  main.** Langkah ini saya lakukan dengan mengubah `models.py` yang ada di dalam folder `main` . Berikut adalah berkas models.py yang saya buat:
	```
	from  django.db  import  models

	# Create your models here.
	class  Product(models.Model):
		name  =  models.CharField(max_length=200)
		price  =  models.IntegerField()
		stock  =  models.IntegerField() # tambahan
		condition  =  models.TextField() # used or new
		description  =  models.TextField() # tambahan
	``` 
	Kemudian, saya membuat dan mengaplikasikan migrasi model dengan menjalankan kedua perintah berikut:
	```python manage.py makemigrations```
	```python manage.py migrate```
10. **Kesepuluh, saya melakukan konfigurasi routing URL Aplikasi `main`.** Pada langkah ini, saya menambahkan `urls.py` yang berisi:
	```
	from  django.urls  import  path
	from  main.views  import  show_main

	app_name  =  'main'
	urlpatterns  = [
		path('', show_main, name='show_main'),
	]
	```
11. **Kesebelas, saya melakukan konfigurasi routing URL Proyek**. Langkah ini saya lakukan dengan mengubah beberapa kode dalam berkas `urls.py` yang terletak di dalam direktori proyek `findyourfits`. Perubahan yang saya lakukan adalah menambahkan impor fungsi `include` dari `django.urls` dan menambahkan `path('',include('main.urls'))` dalam variabel `urlpatterns`.
12. **Keduabelas, saya melakukan testing apakah proyek Django yang saya buat sudah bisa berjalan sesuai dengan apa yang saya mau atau belum**. Langkah ini saya lakukan dengan menjalankan perintah `python manage.py runserver` pada terminal dan membuka http://localhost:8000/ pada web browser.
13. **Terakhir, saya melakukan commit dan push ke repositori Github dan ke Pacil Web Service (PWS)**



### 2) - Buatlah bagan yang berisi  _request client_  ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara  `urls.py`,  `views.py`,  `models.py`, dan berkas  `html`.
![PBP Tugas 2](https://github.com/user-attachments/assets/62d5de3e-d0b6-49c0-926f-cc6e32ae44d4)
Alur Proses:
1. User melakukan permintaan HTTP _(HTTP Request)_ berupa URL untuk meminta resource ke framework Django.
2. Framework Django mencari URL yang diminta user.
3. URL `(urls.py)` memanggil view yang sesuai dengan kode pada `views.py`.
4. View `(views.py)` akan berinteraksi dengan Model `(models.py`) untuk mengambil ataupun mengubah data dari database.
5. View `(views.py)` meng-_compile_ respons yang diberikan oleh Model `(models.py`) kembali ke Template `(template.html)`
6. Hasil akhirnya adalah respons HTTP _(HTTP Response)_ yang dikirim kembali ke user dalam bentuk _web page_ atau halaman HTML.
### 3) Jelaskan fungsi  `git`  dalam pengembangan perangkat lunak!
**Git** adalah sistem kontrol versi terdistribusi _(distributed version control)_ yang dirancang untuk melacak perubahan _source code_ selama pengembangan perangkat lunak.
**Git** memungkinkan banyak pengembang atau _developer_ untuk mengerjakan suatu proyek secara bersamaan tanpa mengganggu pekerjaans atu sama lain.
Beberapa **fitur utama** yang dimiliki **git** adalah:
1. **_Version Control_**: Git menyimpan riwayat perubahan file sehingga kita bisa saja kembali ke versi sebelumnya jika diperlukan.
2. **_Branching_ dan _Merging_**: Git memungkinkan _developer_ untuk membuat _branch_ atau cabang sehingga _developer_ bisa menambahkan fitur atau memperbaiki _bug_ secara independen. Ketika _developer_ sudah selesai, maka file atau kode yang sudah ditambahkan atau diubah pada suatu cabang bisa digabung _(merge)_ kembali ke basis kode utama _(main codebase)_
3. **Sistem Terdistribusi**: Setiap _developer_ memiliki _copy_ dari _repository_ termasuk riwayatnya dalam komputer mereka. Dengan demikian, pekerjaan _developer_ tidak terlalu bergantung terhadap server utama.
4. **Kolaborasi**: **Git** memfasilitasi kolaborasi antar-_developer_ sehingga mudah untuk membagikan perubahan, melakukan _review_ kode, dan melihat kontribusi terhadap kode.
5. **Efisiensi**: **Git** memiliki performa yang optimal, sehingga _developer_ dapat melakukan operasi seperti _commit_ perubahan, _branching_, dan _merging_ dengan cepat.
(Dikutip dari https://www.quora.com/What-is-Git-and-why-should-I-use-it)

### 4) Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
Menurut beberapa sumber yang saya baca tentang framework Django, terdapat beberapa poin yang saya anggap sebagai alasan kenapa Django digunakan sebagai framework yang dipelajari dalam mata kuliah PBP ini, yaitu:
1. **Django dibuat menggunakan Python**, sehingga sintaksnya cukup familiar setidaknya bagi saya pribadi.
2. **Django menggunakan struktur MVT _(Model-View-Template)_** yang menurut saya cukup mudah untuk dipahami bagi orang yang belum pernah melakukan web-development sebelumnya seperti saya.
3. **Framework Django dapat diakses secara gratis dan bersifat _open source_**. Selain itu, Django memiliki dokumentasi yang luas dan mudah diikuti sehingga cocok untuk kegiatan pembelajaran.
4.  **Django digunakan oleh banyak perusahaan di dunia**, diantaranya adalah Instagram, Spotify, dan YouTube. Dengan demikian, _framework_ Django sudah terbukti pengaplikasiannya di dunia sehingga bisa dijadikan sebagai framework untuk kegiatan pembelajaran.
### 5) Mengapa model pada Django disebut sebagai  _ORM_?
Karena ORM _(Object Relational Mapping)_ melakukan mapping dengan tabel-tabel dalam database dengan objek-objek dalam Python. Untuk melakukan CRUD _(Create, Read, Update, and Delete)_ pada Django, kita tidak perlu menuliskan query SQL secara langsung, melainkan kita hanya perlu melakukan perubahan terhadap suatu objek Python dengan metode yang mewakili operasi pada database. 

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

1. Pertama-tama, saya membuka berkas `views.py` dan melakukan import modul `HttpResponse` dan `Serializer` pada bagian atas seperti berikut: 
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

## **TUGAS 4**
## 1. Apa perbedaan antara  `HttpResponseRedirect()`  dan  `redirect()`?
`HttpResponseRedirect` dan `redirect()` adalah fungsi yang memiliki kegunaan yang sama, yaitu melakukan mengarahkan pengguna ke URL berbeda. Perbedaannya adalah yaitu `HttpResponseRedirect` hanya *menerima* argumen pertama yaitu URL. Sedangkan `redirect()` bisa menerima argumen berupa URL, objek, atau view.
## 2. Jelaskan cara kerja penghubungan model  `Product`  dengan  `User`!
Pada tutorial,  model `Product` dan `User` dihubungkan menggunakan relasi `ForeignKey`. Dengan menggunakan `ForeignKey`, maka setiap objek produk akan dihubungkan dengan pengguna tertentu. Model `User` sudah disediakan Django, kita hanya perlu meng-_import_ `django.contrib.auth.models from User`. Berikut adalah implementasi yang saya gunakan dalam program `models.py` yang terletak dalam direktori `main`saya:
```
...
from  django.db  import  models
from  django.contrib.auth.models  import  User
class  ProductEntry(models.Model):
	user  =  models.ForeignKey(User, on_delete=models.CASCADE)
	...
...
```
Dengan mengubah kode pada model `ProductEntry` dengan kode di atas, maka setiap `Product` yang dibuat akan dihubungkan dengan satu `User` dengan hubungan `User` adalah pemilik dari `Product`. Parameter `on_delete =models.CASCADE` berfungsi untuk menghapus `Produk` jika `User` dihapus.

## 3. Apa perbedaan antara  _authentication_  dan  _authorization_, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.
**_Authentication_** adalah proses untuk memverifikasi identitas pengguna sebelum memberikan akses,  seperti akses ke sistem, akun,  atau file. Sedangkan **_authorization_** adalah proses memberikan hak akses kepada pengguna untuk melakukan tindakan tertentu setelah mereka diotentikasi. **_Authorization_** menentukan hal apa saja yang dapat dilakukan pengguna yang telah berhasil login atau berhasil di-_autentikasi_. 

Ketika pengguna melakukan login, maka yang terjadi adalah autentikasi kemudian autorisasi. Pertama-tama, Django memeriksa apakah kombinasi username dan password yang dimasukkan pengguna sudah cocok dengan data yang tersimpan dalam database. Jika sama, maka pengguna dengan username tersebut dianggap ter-**autentikasi** (sebaliknya, jika tidak sama, maka pengguna tidak berhasil diautentikasi).  Setelah pengguna berhasil terautentikasi, maka Django akan menentukan apakah pengguna tersebut memiliki hak untuk melakukan hal tertentu, misalnya hak untuk mengakses halaman, membuka file, atau hal lainnya. Misalnya jika user adalah seorang admin, maka user bisa melihat data-data tertentu. Sedangkan jika user bukan admin, maka user tidak bisa melihat data-data tersebut. Inilah yang disebut dengan **otorisasi**.

Untuk mengimplementasikan **autentikasi dan otorisasi**, Django menyediakan beberapa fungsi bawaann. 
Untuk fungsi autentikasi, Django menyediakan metode seperti  UserCreationForm, AuthenticationForm, authenticate, login dan logout. Method `authenticate()`  dan `login` berguna untuk melakukan autentikasi dan kemudian login jika autentikasi berhasil. Method `logout()` digunakan untuk keluar dari akun suatu user.
Untuk fungsi **otorisasi**, Salah satu yang sudah diajarkan dalam tutorial adalah menggunakan decorator `@login_required` yang diletakkan pada fungsi yang ada dalam file `views.py`. Fungsi ini berguna untuk mengharuskan pengguna untuk login terlebih dahulu sebelum bisa mengakses views tersebut.
## 4. Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari  _cookies_  dan apakah semua cookies aman digunakan?
Django menggunakan mekanisme **session** yang tersimpan dalam **cookies** untuk mengingat pengguna yang telah login. Saat pengguna berhasil login, Django membuat session dan menyimpan informasi terkait di database, kemudian memberikan pengguna session ID dalam bentuk cookie di browser. Contohnya adalah seperti berikut: 
<img width="1796" alt="image" src="https://github.com/user-attachments/assets/6d5aa785-c1e1-4115-832d-cb9cfb4ffcf7">
Dari gambar tersebut, tampak bahwa terdapat data **sessionid** yang menyimpan data login dari pengguna yang digunakan Django untuk mengingat bahwa user dengan sessionid tersebut sudah login.
**Kegunaan lain dari cookies** yang sering saya gunakan diantaranya adalah untuk menyimpan preferensi pengguna yang biasa digunakan untuk _personalized experience_, misalnya ketika saya membuka web eccomerce, maka barang yang muncul adalah barang yang sering saya cari sebelumnya. Selain itu, **cookies** juga berfungsi untuk mengingat barang apa saja yang saya simpan dalam keranjang belanja dalam suatu situs e-commerce.
**Tidak semua cookies aman digunakan**. Dalam beberapa kasus yang saya baca di internet, seorang hacker pernah menggunakan cookies untuk memberikan instruksi dan perintah ke back-end suatu website. Setelah itu, hacker menyimpan dan mengambil sessionid dari user (_sesison hijacking_).  Untuk mengantisipasi hal tersebut, Django menyediakan beberapa cara agar cookies lebih aman, diantaranya adalah menggunakan HttpOnly dan Secure pada settings.py. HttpOnly digunakan agar cookies tidak bisa diakses oleh JavaScript dan Secure berfungsi agar cookies hanya dikirim melalui HTTPS.
## 5. Jelaskan bagaimana cara kamu mengimplementasikan  _checklist_  di atas secara  _step-by-step_  (bukan hanya sekadar mengikuti tutorial).
Untuk mengimplementasikan checklist, maka terdapat beberapa langkah yang saya lakukan, yaitu:
### 1. Membuat Fungsi dan Form Registrasi
Untuk mengimplementasikan fungsi ini, saya melakukan langkah-langkah berikut:
1) Menambahkan import `UserCreationForm` dan `messages` pada berkas `views.py` pada subdirektori main. Berikut adalah kodenya:
	```
	from django.contrib.auth.forms import UserCreationForm  
	from django.contrib import messages
	```
2) Menambahkan fungsi `register` ke dalam `views.py` dengan implementasi sebagai berikut:
	```
	def register(request):
	    form = UserCreationForm()
	    if request.method == "POST":
	        form = UserCreationForm(request.POST)
	        if form.is_valid():
	            form.save()
	            messages.success(request, 'Your account has been successfully created!')
	            return redirect('main:login')
	    context = {'form':form}
	    return render(request, 'register.html', context)
	```
3) Membuat berkas `register.html` pada direktori `main/templates` untuk membuat template untuk melakukan registrasi.
4) Mengimport fungsi `register` yang sudah dibuat dengan menambahkan kode berikut pada `urls.py`:
	```
	from main.views import register
	...
	urlpatterns =  [  
	path('register/', register, name='register'),  
	]
	```
### 2. Membuat Fungsi Login
Untuk membuat fungsi login, berikut adalah langkah-langkahnya:
1) Menambahkan import `authenticate`, `login`, dan `AuthenticationForm` untuk melakukan autentikasi dan login. Berikut adalah kodenya:
	```
	from django.contrib.auth.forms import UserCreationForm, AuthenticationForm  
	from django.contrib.auth import authenticate, login
	```
2) Menambahkan fungsi `login_user` ke `views.py` dengan implementasi sebagai berikut:
	```
	def login_user(request):
	   if request.method == 'POST':
	      form = AuthenticationForm(data=request.POST)
	      if form.is_valid():
	            user = form.get_user()
	            login(request, user)
	            return redirect('main:show_main')
	   else:
	      form = AuthenticationForm(request)
	   context = {'form': form}
	   return render(request, 'login.html', context)
	```
3) Membuat berkas HTML `login.html` yang diletakkan pada direktori `main/templates` untuk menampilkan halaman login untuk user.
4) Menambahkan `urls.py` dengan import `login_user` dan path untuk melakukan login. Berikut adalah kodenya:
	```
	from main.views import login_user
	...
	urlpatterns =  [  
		...  
		path('login/', login_user, name='login'),  
	]
	```
### 3. Membuat Fungsi Logout
Mirip seperti dua langkah sebelumnya, berikut adalah langkah-langkah yang saya lakukan:
1) Menambahkan berkas `views.py` dengan import `logout` dan membuat fungsi `logout_user`. Berikut adalah kodenya:
	```
	from django.contrib.auth import logout
	...
	def  logout_user(request):  
		logout(request)  
		return redirect('main:login')
	```
2) Menambahkan logout button pada `main.html` untuk melakukan logout dengan kode berikut:
```
...
<a  href="{% url 'main:logout' %}">  
	<button>Logout</button>  
</a>
...
```
3) Menambahkan file `urls.py`  dengan import fungsi `logout` dan URL path untuk melakukan `logout`. Berikut adalah kode yang ditambahkan:
```
from main.views import logout_user
...
urlpatterns =  [  
	...  
	path('logout/', logout_user, name='logout'),  
]
```
### 4. Menggunakan Data dari Cookies
Untuk mengimplementasikan _cookies_ dengan tujuan menambahkan data _last login_, berikut adalah langkah-langkah yang saya lakukan:
1) Menambahkan import `HttpResponseRedirect`, `reverse`, dan `datetime`dan memodifikasi fungsi `login_user` untuk melihat kapan terakhir kali user melakukan login.  Berikut adalah kode yang ditambah/modifikasi:
	```
	import datetime
	from django.http import HttpResponseRedirect
	from django.urls import reverse
	...  
	if form.is_valid():  
		user = form.get_user()  
		login(request, user)  
		response = HttpResponseRedirect(reverse("main:show_main"))  
		response.set_cookie('last_login',  str(datetime.datetime.now()))  
		return response  
	...
	```
2) Mengubah fungsi `show_main`  agar dapat menampilkan informasi _cookies_ dengan menambahkan variabel context dengan kode berikut:
	```
	context - {
	'last_login': request.COOKIES['last_login']
	}
	```
3) Mengubah fungsi `logout_user`  agar dapat menghapus cookie `last_login` yang tersimpan dalam browser. Berikut adalah kodenya setelah diubah:
	```
	def logout_user(request):
	    logout(request)
	    response = HttpResponseRedirect(reverse('main:login'))
	    response.delete_cookie('last_login')
	    return response
	```
4) Menambahkan kode `main.html` untuk menampilkan sesi terakhir login yang tersimpan dalam cookies. Berikut adalah kodenya:
	```
	...  
	<h5>Sesi terakhir login: {{ last_login }}</h5>  
	...
	```
### 5. Menghubungkan Model `ProductEntry` dengan `User`
Untuk menghubungkan model `ProductEntry` dengan `User`, berikut adalah langkah-langkah yang saya lakukan:
1) Menambahkan kode `models.py`, yaitu  pada model `ProductEntry` agar dapat menyimpan `User` sebagai pemilik dari product tersebut.  Berikut adalah kode yang ditambahkan:
	```
	from django.contrib.auth.models import User  
	...
	class  MoodEntry(models.Model):  
		user = models.ForeignKey(User, on_delete=models.CASCADE)  
	...
	```
2) Mengubah kode `views.py`, yaitu pada `sell_product_entry` agar mengubah attribut user pada form yang dibuat menjadi user yang sedang login, Berikut adalah tambahan kodenya:
	```
	def  sell_product_entry(request):
		form  =  ProductEntryForm(request.POST or  None)
		if  form.is_valid() and  request.method ==  "POST":
			product_entry  =  form.save(commit=False)
			product_entry.user =  request.user
			product_entry.save()
			return  redirect('main:show_main')

	context  = {'form': form}
	return  render(request, "sell_product_entry.html", context)
	```
3) Mengubah value dari `show_main` agar menampilkan nama sesuai user dan produk yang hanya dimiliki oleh user tersebut. Ubahan kodenya adalah menjadi seperti berikut:
	```
	def  show_main(request):
		product_entries  =  ProductEntry.objects.filter(user=request.user)
		context  = {
			'user_name': request.user.username,
		...
		}
	```

# **TUGAS 5**
## 1. Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
Jika suatu elemen HTML memiliki beberapa CSS selector yang berlaku, maka urutan prioritas atau specificity dalam pengambilan selector ditentukan oleh specificity score dan aturan berikut (dari yang paling diutamakan):
1. **Inline Styles**
Inline Styles adalah penggunaan css yang digunakan untuk menerapkan styling untuk satu elemen. Selector ini memiliki prioritas paling tinggi. Contoh penggunaan:
	```
	<div style="color: red;></div>
	```
2. **ID Selector**
ID selector adalah selector digunakan untuk memberikan style berdasarkan ID. Contoh penggunaan:
	```
	#header { 
	color: blue; 
	font-size: 16px; 
	}
	```
3. **Class, Pseudo-class, dan Attribute Selector**
**Class selector** adalah selector yang menargetkan elemen berdasarkan class. Contoh penerapan:
	```
	.highlight { 
		background-color: yellow; 
		font-weight: bold; 
	}
	```
	 **Pseudo-class selector** adalah selector yang menargetkan elemen berdasarkan kondisi atau interaksi tertentu.
	 ```
	 a:hover { 
		 color: red;
	 }
	 ```
	 **Attribute selector** adalah selector yang menargetkan elemen berdasarkan atribut HTML dan nilainya. Contoh penerapan:
	```
	input[type="text"] {
		border: 1px 
		solid blue;
	}
	```
4. Element dan Pseudo-element Selector
Element dan Pseudo-Element selector adalah selector yang menargetkan elemen berdasarkan nama elemen HTML  (seperti `div`, `p`) atau pseudo-elemen  (seperti `::before`, `::after`). Contoh penerapan:
	```
	p { 
		font-size: 16px; 
	}
	```
	Selain urutan prioritas di atas, kita bisa menghitung specificity suatu selector. Untuk menghitungnya,  kita bisa menggunakan aturan berikut:
	* Mulai value dari 0.
	* Tambahkan 1000 setiap Inline Style
	* Tambahkan 100 setiap ID value
	* Tambahkan 10 setiap class atau pseudo-class value
	* Tambahkan 1 setiap element atau pseudo element selector.
	* Aturan specificity bisa dioverride menggunakan `!important`

	Selector yang memiliki value tertinggi akan digunakan. Jika specificitynya sama, maka yang ditulis paling akhir akan dipilih.

## 2. Mengapa  _responsive design_  menjadi konsep yang penting dalam pengembangan aplikasi  _web_? Berikan contoh aplikasi yang sudah dan belum menerapkan  _responsive design_!
  
** RWD atau responsive web design** adalah pendekatan dalam pengembangan web yang membuat website dapat menyesuaikan tampilannya di berbagai jenis layar dan ukuran perangkat. **Tujuan utama RWD** adalah memastikan konten dan elemen website mudah dibaca sekaligus dinavigasi tanpa perlu terlalu sering men-scroll halaman, baik saat diakses melalui desktop, tablet, maupun smartphone.

Pendekatan responsive design penting dalam web development karena beberapa hal berikut:
* Pengalaman User: Dengan responsive design, user akan memiliki pengalaman yang optimal dan konsisten dalam semua perangkat sehingga navigasi menjadi lebih nyaman. Hal ini dapat meningkatkan kepuasan user dalam menggunakan web.
* SEO: Website yang responsif berpotensi untuk memiliki prioritas lebih tinggi dalam ranking hasil pencarian, misalnya pada Google, terutama pada mobile.
* Efisiensi Biaya dan Waktu: Dengan menggunakan responsive design, maka pengembang tidak perlu mengelola website secara terpisah untuk desktop dan mobile, melainkan mengelola satu website yang bapat disesuaikan dengan semua perangkat sehingga mengurangi waktu dan biaya maintenance.

Beberapa contoh aplikasi yang sudah menerapkan responsive design diantaranya adalah **Tokopedia, Shopee, dan YouTube**. Aplikasi-aplikasi tersebut dapat dibuka baik melalui web pada mobile ataupun desktop.

Beberapa contoh aplikasi yang tidak menerapkan responsive design biasanya adalah aplikasi yang sudah outdated dan tidak diupdate. Aplikasi yang tidak menerapkan responsive design sudah jarang ditemukan. Contoh website yang tidak memiliki responsive design dapat diakses dengan link berikut: 
https://dequeuniversity.com/library/responsive/1-non-responsive

## 3. Jelaskan perbedaan antara  _margin_,  _border_, dan  _padding_, serta cara untuk mengimplementasikan ketiga hal tersebut!
Dalam CSS, margin, border, dan padding adalah tiga properti yang digunakan untuk mengatur ruang di sekitar elemen HTML. Ketiganya memiliki fungsi yang berbeda.
1. Margin: Margin adalah ruang kosong di luar elemen HTML. Margin digunakan untuk memberikan jarak antara elemen satu dengan elemen lainnya. Contoh implementasi:
	```
	.element {
	    margin: 30px;
	}
	```
2. Border: Border adalah garis yang mengelilingi suatu elemen HTML. Border berada diantara padding dan margin. Border bisa mempengaruhi tinggi dan lebar elemen. Digunakan untuk membuat outline atau kotak disekitar elemen. Contoh implementasi:
	```
	.element {
		border: 5px solid green;
	}
	```
3. Padding: Padding adalah ruang kosong di dalam elemen HTML yang berada diantara konten (seperti teks atau gambar) dengan border elemen tersebut. Padding memberikan ruang kosong antara konten dengan border elemen. Contoh implementasi:
	```
	.element {
		padding: 20px;
	}
	```

## 4. Jelaskan konsep  _flex box_  dan  _grid layout_  beserta kegunaannya!
1. Flexbox (Flexible Box) Layout
Flexbox adalah model tata letak satu dimensi yang dirancang untuk mengelola tata letak di satu baris atau di satu kolom pada satu waktu. Flexbox mengatur flex items di dalam flex container secara fleksibel dengan memungkinkan penyesuaian ukuran, posisi, dan distribusi ruang antar elemen secara dinamis dan responsif.
Fungsi utama flexbox:
* Memungkinkan pengaturan elemen secara vertikal dan horizontal di dalam container
* Dapat secara otomatis mendistribusikan ruang kosong antar elemen dan mengatur lebar elemen di dalam flex box berdasarkan ukuran/proporsi yang diinginkan
* Memungkinkan pengaturan tampilan pada berbagai ukuran layar.

	Contoh implementasi:
	```
	.flex-container {
		display: flex; 
		justify-content: space-between;  
		align-items: center; 
		height: 200px; 
		background-color: lightgray;
	}
	.flex-item { 
		background-color: lightcoral; 
		padding: 20px; 
		margin: 5px; 
		flex: 1;
	}
	```
2. Grid Layout
Grid layout adalah sistem tata letak dua dimensi yang memungkinkan penempatan elemen dalam baris dan kolom secara bersamaan. Grid layout memungkinkan kita untuk membuat tata letak dengan kontrol yang lebih besar terhadap posisi elemen.
Fungsi utama grid layout:
* Mengatur tata letak elemen-elemen di dalam sebuah grid, baik secara vertikal ataupun horizontal
* Membantu membuat grid responsif yang berubah ukuran sesuai dengan ukuran layar
* Memberikan kontrol penuh atas jumlah baris dan kolom, dan ukuran masing-masing baris dan kolom tersebut.

	Contoh implementasi:
	```
	.grid-container { 
		display: grid; 
		grid-template-columns: 
		auto auto auto; gap: 10px; 
		background-color: lightgray; 
		padding: 10px; 
	} 
	.grid-item { 
		background-color: lightcoral; 
		padding: 20px; 
		text-align: center; 
	}
	```
Flexbox dan grid layout dapat digunakan sesuai dengan kebutuhan. Jika ingin membuat layout satu dimensi dan mendistribusikan elemen secara rata, maka kita bisa menggunakan flexbox. Sedangkan jika kita ingin mengatur layout dua dimensi dengan kontrol yang lebih spesifik, kita bisa menggunakan grid layout.
## 5. Jelaskan bagaimana cara kamu mengimplementasikan  _checklist_  di atas secara  _step-by-step_  (bukan hanya sekadar mengikuti tutorial)!
### 1. Mengimplementasi fungsi hapus dan tambah product
Berikut adalah implementasi yang saya lakukan untuk membuat fungsi hapus dan tambah product:
Pada `views.py`:
Menambahkan untuk mengimplementasikan fungsi `edit_product` dan `hapus_product`
```
def edit_product(request, id):
	product  =  ProductEntry.objects.get(pk  =  id)
	form  =  ProductEntryForm(request.POST or  None, instance=product)
	if  form.is_valid() and  request.method ==  "POST":
		form.save()
		return  HttpResponseRedirect(reverse('main:show_main'))
	context  = {'form': form}
	return  render(request, "edit_product.html", context)

def hapus_product(request, id):
	product  =  ProductEntry.objects.get(pk  =  id)
	product.delete()
	return  HttpResponseRedirect(reverse('main:show_main'))
```
Pada `urls.py`:
Menambahkan url routing untuk fungsi `edit_product` dan `hapus_product`
```
from  main.views  import  ..., edit_product, hapus_product

url_patterns = [
	...
	path('edit_product/<uuid:id>', edit_product, name='edit_product'),
	path('delete/<uuid:id>', hapus_product, name='hapus_product')
]
```
### 2. Kustomisasi halaman login
<p align="center">
	<img width="1797" alt="image" src="https://github.com/user-attachments/assets/ca537aab-0e8d-4a0c-9f73-36a8ef21edd6">
	<img width="493" alt="image" src="https://github.com/user-attachments/assets/a17afbb8-c654-4187-9a79-47812dda142c">
</p>
Untuk mengimplementasikan login page di atas, saya menggunakan Tailwind CSS untuk styling dan layouting. Terdapat beberapa elemen yang saya tambahkan, yaitu:

* Background berwarna cyan gradasi
* Container putih dan rounded
* Welcome message
* Styling untuk input
* Tombol login
* Tombol registrasi

### 3. Kustomisasi halaman register
<p align="center">
	<img width="490" alt="image" src="https://github.com/user-attachments/assets/5299b409-4c69-4892-85f7-1245457efec6">
	<img width="1794" alt="image" src="https://github.com/user-attachments/assets/5c6f206f-590b-40e3-953d-72d563fa21ff">
</p>
Pada halaman register, yang saya tambahkan mirip seperti pada login page. Perbedaan hanya terletak pada header, field, button daftar dan tombol login.

### 4. Kustomisasi halaman tambah product dan edit product
<p align="center">
	<img width="1796" alt="image" src="https://github.com/user-attachments/assets/b0cb5bac-1cb6-4ba8-bca0-2add754b95e1">
	<img width="1795" alt="image" src="https://github.com/user-attachments/assets/6fa47dd6-0b72-4c35-a85f-767e0a58f69b">
	<img width="510" alt="image" src="https://github.com/user-attachments/assets/d52d9434-d104-4e91-afb5-13a133773979">
	<img width="508" alt="image" src="https://github.com/user-attachments/assets/577c6d8b-3908-4d1e-b298-db798b89be44">
</p>
Untuk mengimplementasikan halaman tambah produk dan edit deskripsi produk, terdapat beberapa hal yang saya lakukan:

* Menambahkan navbar
* Memnambahkan container untuk tempat fields dari form
* Membuat header sesuai dengan nama form (Form Tambah Produk atau Edit Deskripsi Produk)
* Melakukan styling untuk button
* Membuat warna gradasi untuk header dan container form
* Menambahkan placeholder untuk setiap fields

### 5. Kustomisasi homepage dengan daftar product dan membuat navbar
<img width="509" alt="image" src="https://github.com/user-attachments/assets/451a3508-aa4f-4c7f-9898-5e97495684a2">
<img width="511" alt="image" src="https://github.com/user-attachments/assets/a0732e6e-f280-4ebc-bb7c-5b373d697b7d">
<img width="1798" alt="image" src="https://github.com/user-attachments/assets/7c77864a-906d-4912-8e0f-7f2ff7060045">
<img width="1799" alt="image" src="https://github.com/user-attachments/assets/5c2344be-32ac-4cb7-9721-66336288f096">

Untuk mengimplementasikan desain homepage did atas, terdapat beberapa hal yang saya tambahkan:

* Card untuk container data pengguna dan last login
* Container untuk list produk yang berisi card_product.html dari tiap produk yang dimiliki pengguna
* Card product yang berisi attribut dari produk dan tombol edit dan hapus produk
* Navbar responsif yang bisa digunakan untuk masuk ke halaman homepage atau tambah produk.
* Semua desain bersifat responsif sehingga dapat menyesuaikan dengan ukuran layar dari pengguna