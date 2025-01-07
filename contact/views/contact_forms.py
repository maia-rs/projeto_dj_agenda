from typing import Any, Dict
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from contact.models import Contact
from contact.forms import ContactForm


@login_required(login_url='contact:login')

def create(request):
    form_action = reverse('contact:create')
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.owner = request.user
            contact.save()
            return redirect('contact:update', contact_id=contact.pk)  # Redirecione para uma página de sucesso após salvar

        context = {
            'form': form,  # Use o formulário com erros para exibir novamente
            'form_action': form_action,
        }
        return render(
            request,
            'contact/create.html',
            context
        )
    
    context = {
        'form': ContactForm(),
        'form_action': form_action,  # Adicionado form_action no contexto GET também
    }
    
    return render(
        request,
        'contact/create.html',
        context
    )

@login_required(login_url='contact:login')

def update(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id, show=True, owner=request.user)
    form_action = reverse('contact:update', args=(contact_id,))
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES, instance=contact)  # Adicione instance para atualizar o contato
        if form.is_valid():
            contact = form.save()
            return redirect('contact:update', contact_id=contact.pk)  # Redirecione para a mesma página após salvar

        context = {
            'form': form,  # Use o formulário com erros para exibir novamente
            'form_action': form_action,
        }
        return render(
            request,
            'contact/create.html',
            context
        )
    
    context = {
        'form': ContactForm(instance=contact),
        'form_action': form_action,  # Adicionado form_action no contexto GET também
    }
    
    return render(
        request,
        'contact/create.html',
        context
    )
@login_required(login_url='contact:login')

def delete(request, contact_id):
    contact = get_object_or_404(
        Contact, pk=contact_id, show=True, owner=request.user
    )
    confirmation = request.POST.get('confirmation', 'no')

    if confirmation == 'yes':
        contact.delete()
        return redirect('contact:index')

    return render(
        request,
        'contact/contact.html',
        {
            'contact': contact,
            'confirmation': confirmation,
        }
    )