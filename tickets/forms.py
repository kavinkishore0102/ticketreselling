from django import forms
from .models import Ticket

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['ticket_image','source','destination', 'departure_date', 
                 'departure_time', 'ticket_type', 'price']
        widgets = {
            'departure_date': forms.DateInput(attrs={'type': 'date'}),
            'departure_time': forms.TimeInput(attrs={'type': 'time'}),
        }