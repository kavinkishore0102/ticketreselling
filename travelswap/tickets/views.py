from django.shortcuts import render, redirect
from .forms import TicketForm

def sell_ticket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = TicketForm()
    
    return render(request, 'tickets/sell.html', {'form': form})

def success_view(request):
    return render(request, 'tickets/success.html')