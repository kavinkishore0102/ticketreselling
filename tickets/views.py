from django.shortcuts import render, redirect,get_object_or_404
from .forms import TicketForm
from .models import Ticket
from django.views.decorators.http import require_POST
import pytesseract
from PIL import Image
import re
from django.contrib import messages
from django.http import HttpResponse
from django.db import transaction
from .forms import TicketForm
from .models import Ticket, SoldTicket
from django.http import JsonResponse 
from .utils.ocr_utils import extract_text_from_image, find_total_cost

def home(request):
    tickets = Ticket.objects.all().order_by('-uploaded_at')[:8]
    return render(request, 'home.html', {'tickets': tickets}) 


def sell_ticket(request, ticket_id):
    if request.method == 'POST':
        ticket = get_object_or_404(Ticket, id=ticket_id)

        buyer_name = request.POST.get('buyer_name')
        buyer_email = request.POST.get('buyer_email')

        if not buyer_name or not buyer_email:
            return HttpResponse("Buyer details are missing!")

        try:
            with transaction.atomic():
                SoldTicket.objects.create(
                    ticket=ticket,
                    buyer_name=buyer_name,
                    buyer_email=buyer_email,
                    sale_price=ticket.price,
                    transaction_id=f"TXN{ticket.id}"
                )
                ticket.delete()
            return HttpResponse("Ticket sold successfully!")
        except Exception as e:
            return HttpResponse(f"Error: {e}")
    
    # For GET requests, show a form to submit buyer details
    return render(request, 'confirm_sale.html', {'ticket_id': ticket_id})

def upload_ticket(request):
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

def find_price(request):
    return 0



def check_ticket_price(request):
    if request.method == "POST" and request.FILES.get("ticket_image"):
        image_file = request.FILES["ticket_image"]
        image = Image.open(image_file)

        extracted_text = extract_text_from_image(image)
        total_cost = find_total_cost(extracted_text)

        if total_cost is not None:
            return JsonResponse({"success": True, "price": total_cost})
        else:
            return JsonResponse({"success": False, "error": "Could not extract price."})
    return JsonResponse({"success": False, "error": "Invalid request."})