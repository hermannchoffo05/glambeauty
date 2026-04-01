from django.shortcuts import render
from django.contrib import messages
from .models import Produit, Service
from .forms import ContactForm

def accueil(request):
    produits = Produit.objects.all()
    services = Service.objects.all()
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            messages.success(request, '✅ Votre message a été envoyé avec succès !')
            form = ContactForm()

    return render(request, 'vitrine/accueil.html', {
        'produits': produits,
        'services': services,
        'form': form,
    })