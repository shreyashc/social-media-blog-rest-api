from django.shortcuts import render


def home(request):
    context = {
        'BASE_URL': "https://hcblogapi.herokuapp.com"
    }
    return render(request, 'index.html', context)
