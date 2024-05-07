from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse

def submit_consultation(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message', '')
        
        return HttpResponse("Request submitted successfully!")
    return render(request, 'consultation.html')
def index(request):
    return render(request, 'index.html')

def services(request):
    return render(request, 'services.html')

def consultation(request):
    return render(request, 'consultation.html')

def search(request):
    query = request.GET.get('q', '')
    context = {
        'query': query,
    }
    return render(request, 'search_results.html', context)

def info(request):
    return render(request, 'info.html')

def contact(request):
    return render(request, 'contact.html')

def product(request):
    return render(request, 'product.html')

# core/views.py

from django.shortcuts import render

def about_us(request):
    context = {
        'title': 'About Us',
        'mission': 'Our mission statement goes here...',
        'vision': 'Our vision statement goes here...',
        'team': [
            {'name': 'John Doe', 'position': 'Founder & CEO'},
            {'name': 'Jane Smith', 'position': 'COO'},
        ]
    }
    return render(request, 'about_us.html', context)



