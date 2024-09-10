from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'app_name' : 'FindYourFits',
        'name': 'Daffa Desra Hastiar',
        'npm': '2306165490',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)