from django.shortcuts import render, redirect
from .forms import TicketForm

def home(request):
    return render(request, 'home.html')

def sell_ticket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')  
    else:
        form = TicketForm()
    
    return render(request, 'sell.html', {'form': form})

def success_view(request):
    return render(request, 'success.html') 

def about(request):
    return render(request, 'about.html')
