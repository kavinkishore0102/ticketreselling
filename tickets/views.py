from django.shortcuts import render, redirect,get_object_or_404
from .forms import TicketForm
from .models import Ticket
from django.views.decorators.http import require_POST
import pytesseract
from PIL import Image
import re
from django.contrib import messages


def home(request):
    tickets = Ticket.objects.all().order_by('-uploaded_at')[:8]
    return render(request, 'home.html', {'tickets': tickets}) 

def sell_ticket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TicketForm()
    return render(request, 'sell.html', {'form': form})

@require_POST
def buy_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    ticket.delete()
    return redirect('home')


def success_view(request):
    return render(request, 'success.html') 

def about(request):
    return render(request, 'about.html')

def success_page(request):
    return render(request, 'tickets/success.html')