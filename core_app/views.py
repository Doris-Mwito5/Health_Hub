from django.shortcuts import render, redirect
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from .forms import ConsultationForm
from datetime import datetime

def consultation(request):
    if request.method == 'POST':
        form = ConsultationForm(request.POST)
        if form.is_valid():
            return render(request, 'review.html', {'form': form})
    else:
        form = ConsultationForm()

    return render(request, 'consultation.html', {'form': form})

from django.shortcuts import render, redirect
from .models import Consultation
from .forms import ConsultationForm

def submit_consultation(request):
    if request.method == 'POST':
        form = ConsultationForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('review')
    else:
        form = ConsultationForm()

    return render(request, 'consultation.html', {'form': form})

def review(request):
    consultations = Consultation.objects.all()
    return render(request, 'review.html', {'consultations': consultations})


def index(request):
    return render(request, 'index.html')

def services(request):
    return render(request, 'services.html')

def info(request):
    return render(request, 'info.html')

def contact(request):
    return render(request, 'contact.html')

def product(request):
    return render(request, 'product.html')

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

def inquiry(request):
    
    return render(request, 'inquiry.html')

def submit_inquiry(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message', '')
        
        return HttpResponse("Inqury submitted successfully!")
    return render(request, 'inquiry.html')


